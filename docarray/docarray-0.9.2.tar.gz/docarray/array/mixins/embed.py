import warnings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...types import T, AnyDNN


class EmbedMixin:
    """Helper functions for embedding with a model"""

    def embed(
        self: 'T',
        embed_model: 'AnyDNN',
        device: str = 'cpu',
        batch_size: int = 256,
        to_numpy: bool = False,
    ) -> 'T':
        """Fill :attr:`.embedding` of Documents inplace by using `embed_model`

        :param embed_model: the embedding model written in Keras/Pytorch/Paddle
        :param device: the computational device for `embed_model`, can be either
            `cpu` or `cuda`.
        :param batch_size: number of Documents in a batch for embedding
        :param to_numpy: if to store embeddings back to Document in ``numpy.ndarray`` or original framework format.
        :return: itself after modified.
        """

        fm = get_framework(embed_model)
        getattr(self, f'_set_embeddings_{fm}')(
            embed_model, device, batch_size, to_numpy
        )
        return self

    def _set_embeddings_keras(
        self: 'T',
        embed_model: 'AnyDNN',
        device: str = 'cpu',
        batch_size: int = 256,
        to_numpy: bool = False,
    ):
        import tensorflow as tf

        device = tf.device('/GPU:0') if device == 'cuda' else tf.device('/CPU:0')
        with device:
            for b_ids in self.batch_ids(batch_size):
                r = embed_model(self[b_ids, 'tensor'], training=False)
                if not isinstance(r, tf.Tensor):
                    # NOTE: Transformers has own output class.
                    from transformers.modeling_outputs import ModelOutput

                    r = r.pooler_output  # type: ModelOutput

                self[b_ids, 'embedding'] = r.numpy() if to_numpy else r

    def _set_embeddings_torch(
        self: 'T',
        embed_model: 'AnyDNN',
        device: str = 'cpu',
        batch_size: int = 256,
        to_numpy: bool = False,
    ):
        import torch

        embed_model = embed_model.to(device)
        is_training_before = embed_model.training
        embed_model.eval()
        with torch.inference_mode():
            for b_ids in self.batch_ids(batch_size):
                batch_inputs = torch.tensor(self[b_ids, 'tensor'], device=device)
                r = embed_model(batch_inputs)
                if isinstance(r, torch.Tensor):
                    r = r.cpu().detach()
                else:
                    # NOTE: Transformers has own output class.
                    from transformers.modeling_outputs import ModelOutput

                    r = r.pooler_output.cpu().detach()  # type: ModelOutput
                self[b_ids, 'embedding'] = r.numpy() if to_numpy else r

        if is_training_before:
            embed_model.train()

    def _set_embeddings_paddle(
        self: 'T',
        embed_model,
        device: str = 'cpu',
        batch_size: int = 256,
        to_numpy: bool = False,
    ):
        import paddle

        is_training_before = embed_model.training
        embed_model.to(device=device)
        embed_model.eval()
        for b_ids in self.batch_ids(batch_size):
            batch_inputs = paddle.to_tensor(self[b_ids, 'tensor'], place=device)
            r = embed_model(batch_inputs)
            self[b_ids, 'embedding'] = r.numpy() if to_numpy else r

        if is_training_before:
            embed_model.train()

    def _set_embeddings_onnx(
        self: 'T',
        embed_model,
        device: str = 'cpu',
        batch_size: int = 256,
        *args,
        **kwargs,
    ):
        # embed_model is always an onnx.InferenceSession
        if device != 'cpu':
            import onnxruntime as ort

            support_device = ort.get_device()
            if device.lower().strip() != support_device.lower().strip():
                warnings.warn(
                    f'Your installed `onnxruntime` supports `{support_device}`, but you give {device}'
                )

        for b_ids in self.batch_ids(batch_size):
            self[b_ids, 'embedding'] = embed_model.run(
                None, {embed_model.get_inputs()[0].name: self[b_ids, 'tensor']}
            )[0]


def get_framework(dnn_model) -> str:
    """Return the framework that powers a DNN model.

    .. note::
        This is not a solid implementation. It is based on ``__module__`` name,
        the key idea is to tell ``dnn_model`` without actually importing the
        framework.

    :param dnn_model: a DNN model
    :return: `keras`, `torch`, `paddle` or ValueError

    """
    import importlib.util

    if importlib.util.find_spec('torch'):
        import torch

        if isinstance(dnn_model, torch.nn.Module):
            return 'torch'

    if importlib.util.find_spec('paddle'):
        import paddle

        if isinstance(dnn_model, paddle.nn.Layer):
            return 'paddle'

    if importlib.util.find_spec('tensorflow'):
        from tensorflow import keras

        if isinstance(dnn_model, keras.layers.Layer):
            return 'keras'

    if importlib.util.find_spec('onnx'):
        from onnxruntime import InferenceSession

        if isinstance(dnn_model, InferenceSession):
            return 'onnx'

    raise ValueError(f'can not determine the backend of {dnn_model!r}')
