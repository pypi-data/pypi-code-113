from mdlu.transforms import NNUnetNormalization as _NNUnetNormalization

from shape.transforms.mixin import TransformShapeValidationMixin


# Need to subclass from TransformShapeValidationMixin as that one fixes kwargs
class NNUnetNormalization(_NNUnetNormalization, TransformShapeValidationMixin):
    pass
