# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "ConversationModel",
        "ConversationModelEvaluation",
        "EvaluationConfig",
        "InputDataset",
        "ArticleSuggestionModelMetadata",
        "SmartReplyModelMetadata",
        "SmartReplyMetrics",
        "CreateConversationModelRequest",
        "GetConversationModelRequest",
        "ListConversationModelsRequest",
        "ListConversationModelsResponse",
        "DeleteConversationModelRequest",
        "DeployConversationModelRequest",
        "UndeployConversationModelRequest",
        "GetConversationModelEvaluationRequest",
        "ListConversationModelEvaluationsRequest",
        "ListConversationModelEvaluationsResponse",
        "CreateConversationModelEvaluationRequest",
        "CreateConversationModelOperationMetadata",
        "DeployConversationModelOperationMetadata",
        "UndeployConversationModelOperationMetadata",
        "DeleteConversationModelOperationMetadata",
        "CreateConversationModelEvaluationOperationMetadata",
    },
)


class ConversationModel(proto.Message):
    r"""Represents a conversation model.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            ConversationModel resource name. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>``
        display_name (str):
            Required. The display name of the model. At
            most 64 bytes long.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this model.
        datasets (Sequence[google.cloud.dialogflow_v2.types.InputDataset]):
            Required. Datasets used to create model.
        state (google.cloud.dialogflow_v2.types.ConversationModel.State):
            Output only. State of the model. A model can
            only serve prediction requests after it gets
            deployed.
        language_code (str):
            Language code for the conversation model. If not specified,
            the language is en-US. Language at ConversationModel should
            be set for all non en-us languages. This should be a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag. Example: "en-US".
        article_suggestion_model_metadata (google.cloud.dialogflow_v2.types.ArticleSuggestionModelMetadata):
            Metadata for article suggestion models.

            This field is a member of `oneof`_ ``model_metadata``.
        smart_reply_model_metadata (google.cloud.dialogflow_v2.types.SmartReplyModelMetadata):
            Metadata for smart reply models.

            This field is a member of `oneof`_ ``model_metadata``.
    """

    class State(proto.Enum):
        r"""State of the model."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        UNDEPLOYED = 2
        DEPLOYING = 3
        DEPLOYED = 4
        UNDEPLOYING = 5
        DELETING = 6
        FAILED = 7
        PENDING = 8

    class ModelType(proto.Enum):
        r"""Model type."""
        MODEL_TYPE_UNSPECIFIED = 0
        SMART_REPLY_DUAL_ENCODER_MODEL = 2
        SMART_REPLY_BERT_MODEL = 6

    name = proto.Field(proto.STRING, number=1,)
    display_name = proto.Field(proto.STRING, number=2,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    datasets = proto.RepeatedField(proto.MESSAGE, number=4, message="InputDataset",)
    state = proto.Field(proto.ENUM, number=7, enum=State,)
    language_code = proto.Field(proto.STRING, number=19,)
    article_suggestion_model_metadata = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="model_metadata",
        message="ArticleSuggestionModelMetadata",
    )
    smart_reply_model_metadata = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="model_metadata",
        message="SmartReplyModelMetadata",
    )


class ConversationModelEvaluation(proto.Message):
    r"""Represents evaluation result of a conversation model.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the evaluation. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>/evaluations/<Evaluation ID>``
        display_name (str):
            Optional. The display name of the model
            evaluation. At most 64 bytes long.
        evaluation_config (google.cloud.dialogflow_v2.types.EvaluationConfig):
            Optional. The configuration of the evaluation
            task.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this model.
        smart_reply_metrics (google.cloud.dialogflow_v2.types.SmartReplyMetrics):
            Output only. Only available when model is for
            smart reply.

            This field is a member of `oneof`_ ``metrics``.
    """

    name = proto.Field(proto.STRING, number=1,)
    display_name = proto.Field(proto.STRING, number=2,)
    evaluation_config = proto.Field(
        proto.MESSAGE, number=6, message="EvaluationConfig",
    )
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    smart_reply_metrics = proto.Field(
        proto.MESSAGE, number=5, oneof="metrics", message="SmartReplyMetrics",
    )


class EvaluationConfig(proto.Message):
    r"""The configuration for model evaluation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        datasets (Sequence[google.cloud.dialogflow_v2.types.InputDataset]):
            Required. Datasets used for evaluation.
        smart_reply_config (google.cloud.dialogflow_v2.types.EvaluationConfig.SmartReplyConfig):
            Configuration for smart reply model
            evalution.

            This field is a member of `oneof`_ ``model_specific_config``.
        smart_compose_config (google.cloud.dialogflow_v2.types.EvaluationConfig.SmartComposeConfig):
            Configuration for smart compose model
            evalution.

            This field is a member of `oneof`_ ``model_specific_config``.
    """

    class SmartReplyConfig(proto.Message):
        r"""Smart reply specific configuration for evaluation job.

        Attributes:
            allowlist_document (str):
                The allowlist document resource name. Format:
                ``projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
                Only used for smart reply model.
            max_result_count (int):
                Required. The model to be evaluated can return multiple
                results with confidence score on each query. These results
                will be sorted by the descending order of the scores and we
                only keep the first max_result_count results as the final
                results to evaluate.
        """

        allowlist_document = proto.Field(proto.STRING, number=1,)
        max_result_count = proto.Field(proto.INT32, number=2,)

    class SmartComposeConfig(proto.Message):
        r"""Smart compose specific configuration for evaluation job.

        Attributes:
            allowlist_document (str):
                The allowlist document resource name. Format:
                ``projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
                Only used for smart compose model.
            max_result_count (int):
                Required. The model to be evaluated can return multiple
                results with confidence score on each query. These results
                will be sorted by the descending order of the scores and we
                only keep the first max_result_count results as the final
                results to evaluate.
        """

        allowlist_document = proto.Field(proto.STRING, number=1,)
        max_result_count = proto.Field(proto.INT32, number=2,)

    datasets = proto.RepeatedField(proto.MESSAGE, number=3, message="InputDataset",)
    smart_reply_config = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="model_specific_config",
        message=SmartReplyConfig,
    )
    smart_compose_config = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="model_specific_config",
        message=SmartComposeConfig,
    )


class InputDataset(proto.Message):
    r"""InputDataset used to create model or do evaluation.
    NextID:5

    Attributes:
        dataset (str):
            Required. ConversationDataset resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>``
    """

    dataset = proto.Field(proto.STRING, number=1,)


class ArticleSuggestionModelMetadata(proto.Message):
    r"""Metadata for article suggestion models.

    Attributes:
        training_model_type (google.cloud.dialogflow_v2.types.ConversationModel.ModelType):
            Optional. Type of the article suggestion model. If not
            provided, model_type is used.
    """

    training_model_type = proto.Field(
        proto.ENUM, number=3, enum="ConversationModel.ModelType",
    )


class SmartReplyModelMetadata(proto.Message):
    r"""Metadata for smart reply models.

    Attributes:
        training_model_type (google.cloud.dialogflow_v2.types.ConversationModel.ModelType):
            Optional. Type of the smart reply model. If not provided,
            model_type is used.
    """

    training_model_type = proto.Field(
        proto.ENUM, number=6, enum="ConversationModel.ModelType",
    )


class SmartReplyMetrics(proto.Message):
    r"""The evaluation metrics for smart reply model.

    Attributes:
        allowlist_coverage (float):
            Percentage of target participant messages in the evaluation
            dataset for which similar messages have appeared at least
            once in the allowlist. Should be [0, 1].
        top_n_metrics (Sequence[google.cloud.dialogflow_v2.types.SmartReplyMetrics.TopNMetrics]):
            Metrics of top n smart replies, sorted by [TopNMetric.n][].
        conversation_count (int):
            Total number of conversations used to
            generate this metric.
    """

    class TopNMetrics(proto.Message):
        r"""Evaluation metrics when retrieving ``n`` smart replies with the
        model.

        Attributes:
            n (int):
                Number of retrieved smart replies. For example, when ``n``
                is 3, this evaluation contains metrics for when Dialogflow
                retrieves 3 smart replies with the model.
            recall (float):
                Defined as
                ``number of queries whose top n smart replies have at least one similar (token match similarity above the defined threshold) reply as the real reply``
                divided by
                ``number of queries with at least one smart reply``. Value
                ranges from 0.0 to 1.0 inclusive.
        """

        n = proto.Field(proto.INT32, number=1,)
        recall = proto.Field(proto.FLOAT, number=2,)

    allowlist_coverage = proto.Field(proto.FLOAT, number=1,)
    top_n_metrics = proto.RepeatedField(proto.MESSAGE, number=2, message=TopNMetrics,)
    conversation_count = proto.Field(proto.INT64, number=3,)


class CreateConversationModelRequest(proto.Message):
    r"""The request message for
    [ConversationModels.CreateConversationModel][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModel]

    Attributes:
        parent (str):
            The project to create conversation model for. Format:
            ``projects/<Project ID>``
        conversation_model (google.cloud.dialogflow_v2.types.ConversationModel):
            Required. The conversation model to create.
    """

    parent = proto.Field(proto.STRING, number=1,)
    conversation_model = proto.Field(
        proto.MESSAGE, number=2, message="ConversationModel",
    )


class GetConversationModelRequest(proto.Message):
    r"""The request message for
    [ConversationModels.GetConversationModel][google.cloud.dialogflow.v2.ConversationModels.GetConversationModel]

    Attributes:
        name (str):
            Required. The conversation model to retrieve. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>``
    """

    name = proto.Field(proto.STRING, number=1,)


class ListConversationModelsRequest(proto.Message):
    r"""The request message for
    [ConversationModels.ListConversationModels][google.cloud.dialogflow.v2.ConversationModels.ListConversationModels]

    Attributes:
        parent (str):
            Required. The project to list all conversation models for.
            Format: ``projects/<Project ID>``
        page_size (int):
            Optional. Maximum number of conversation
            models to return in a single page. By default
            100 and at most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)


class ListConversationModelsResponse(proto.Message):
    r"""The response message for
    [ConversationModels.ListConversationModels][google.cloud.dialogflow.v2.ConversationModels.ListConversationModels]

    Attributes:
        conversation_models (Sequence[google.cloud.dialogflow_v2.types.ConversationModel]):
            The list of models to return.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    conversation_models = proto.RepeatedField(
        proto.MESSAGE, number=1, message="ConversationModel",
    )
    next_page_token = proto.Field(proto.STRING, number=2,)


class DeleteConversationModelRequest(proto.Message):
    r"""The request message for
    [ConversationModels.DeleteConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeleteConversationModel]

    Attributes:
        name (str):
            Required. The conversation model to delete. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>``
    """

    name = proto.Field(proto.STRING, number=1,)


class DeployConversationModelRequest(proto.Message):
    r"""The request message for
    [ConversationModels.DeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeployConversationModel]

    Attributes:
        name (str):
            Required. The conversation model to deploy. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>``
    """

    name = proto.Field(proto.STRING, number=1,)


class UndeployConversationModelRequest(proto.Message):
    r"""The request message for
    [ConversationModels.UndeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.UndeployConversationModel]

    Attributes:
        name (str):
            Required. The conversation model to undeploy. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>``
    """

    name = proto.Field(proto.STRING, number=1,)


class GetConversationModelEvaluationRequest(proto.Message):
    r"""The request message for
    [ConversationModels.GetConversationModelEvaluation][google.cloud.dialogflow.v2.ConversationModels.GetConversationModelEvaluation]

    Attributes:
        name (str):
            Required. The conversation model evaluation resource name.
            Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>/evaluations/<Evaluation ID>``
    """

    name = proto.Field(proto.STRING, number=1,)


class ListConversationModelEvaluationsRequest(proto.Message):
    r"""The request message for
    [ConversationModels.ListConversationModelEvaluations][google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations]

    Attributes:
        parent (str):
            Required. The conversation model resource name. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model ID>``
        page_size (int):
            Optional. Maximum number of evaluations to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)


class ListConversationModelEvaluationsResponse(proto.Message):
    r"""The response message for
    [ConversationModels.ListConversationModelEvaluations][google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations]

    Attributes:
        conversation_model_evaluations (Sequence[google.cloud.dialogflow_v2.types.ConversationModelEvaluation]):
            The list of evaluations to return.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    conversation_model_evaluations = proto.RepeatedField(
        proto.MESSAGE, number=1, message="ConversationModelEvaluation",
    )
    next_page_token = proto.Field(proto.STRING, number=2,)


class CreateConversationModelEvaluationRequest(proto.Message):
    r"""The request message for
    [ConversationModels.CreateConversationModelEvaluation][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluation]

    Attributes:
        parent (str):
            Required. The conversation model resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationModels/<Conversation Model ID>``
        conversation_model_evaluation (google.cloud.dialogflow_v2.types.ConversationModelEvaluation):
            Required. The conversation model evaluation
            to be created.
    """

    parent = proto.Field(proto.STRING, number=1,)
    conversation_model_evaluation = proto.Field(
        proto.MESSAGE, number=2, message="ConversationModelEvaluation",
    )


class CreateConversationModelOperationMetadata(proto.Message):
    r"""Metadata for a
    [ConversationModels.CreateConversationModel][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModel]
    operation.

    Attributes:
        conversation_model (str):
            The resource name of the conversation model. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model Id>``
        state (google.cloud.dialogflow_v2.types.CreateConversationModelOperationMetadata.State):
            State of CreateConversationModel operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the request to create
            conversation model is submitted. The time is
            measured on server side.
    """

    class State(proto.Enum):
        r"""State of CreateConversationModel operation."""
        STATE_UNSPECIFIED = 0
        PENDING = 1
        SUCCEEDED = 2
        FAILED = 3
        CANCELLED = 4
        CANCELLING = 5
        TRAINING = 6

    conversation_model = proto.Field(proto.STRING, number=1,)
    state = proto.Field(proto.ENUM, number=2, enum=State,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)


class DeployConversationModelOperationMetadata(proto.Message):
    r"""Metadata for a
    [ConversationModels.DeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeployConversationModel]
    operation.

    Attributes:
        conversation_model (str):
            The resource name of the conversation model. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model Id>``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when request to deploy conversation
            model was submitted. The time is measured on
            server side.
    """

    conversation_model = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)


class UndeployConversationModelOperationMetadata(proto.Message):
    r"""Metadata for a
    [ConversationModels.UndeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.UndeployConversationModel]
    operation.

    Attributes:
        conversation_model (str):
            The resource name of the conversation model. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model Id>``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the request to undeploy
            conversation model was submitted. The time is
            measured on server side.
    """

    conversation_model = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)


class DeleteConversationModelOperationMetadata(proto.Message):
    r"""Metadata for a
    [ConversationModels.DeleteConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeleteConversationModel]
    operation.

    Attributes:
        conversation_model (str):
            The resource name of the conversation model. Format:
            ``projects/<Project ID>/conversationModels/<Conversation Model Id>``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when delete conversation model
            request was created. The time is measured on
            server side.
    """

    conversation_model = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)


class CreateConversationModelEvaluationOperationMetadata(proto.Message):
    r"""Metadata for a
    [ConversationModels.CreateConversationModelEvaluation][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluation]
    operation.

    Attributes:
        conversation_model_evaluation (str):
            The resource name of the conversation model. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationModels/<Conversation Model Id>/evaluations/<Evaluation Id>``
        conversation_model (str):
            The resource name of the conversation model. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationModels/<Conversation Model Id>``
        state (google.cloud.dialogflow_v2.types.CreateConversationModelEvaluationOperationMetadata.State):
            State of CreateConversationModel operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the request to create
            conversation model was submitted. The time is
            measured on server side.
    """

    class State(proto.Enum):
        r"""State of CreateConversationModel operation."""
        STATE_UNSPECIFIED = 0
        INITIALIZING = 1
        RUNNING = 2
        CANCELLED = 3
        SUCCEEDED = 4
        FAILED = 5

    conversation_model_evaluation = proto.Field(proto.STRING, number=1,)
    conversation_model = proto.Field(proto.STRING, number=4,)
    state = proto.Field(proto.ENUM, number=2, enum=State,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)


__all__ = tuple(sorted(__protobuf__.manifest))
