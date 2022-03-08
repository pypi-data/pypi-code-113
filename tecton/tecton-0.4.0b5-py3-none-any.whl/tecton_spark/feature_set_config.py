from typing import List
from typing import Optional
from typing import Tuple

import attr

from tecton_proto.data.feature_service_pb2 import FeatureSetItem
from tecton_spark.fco_container import FcoContainer
from tecton_spark.feature_definition_wrapper import FeatureDefinitionWrapper as FeatureDefinition
from tecton_spark.id_helper import IdHelper


@attr.s(frozen=True, auto_attribs=True)
class _Key(object):
    name: str
    namespace: str


@attr.s(frozen=True, auto_attribs=True)
class FeatureDefinitionAndJoinConfig(object):
    """
    A feature definition and its associated join configuration.

    :param feature_definition: FeatureView/FeatureTable object.
    :param join_keys: The mapping from FeatureService's join keys to FeatureView/FeatureTable's join keys.
    :param namespace: The namespace.
    """

    feature_definition: FeatureDefinition
    name: str
    join_keys: List[Tuple[str, str]]
    namespace: str
    features: List[str]

    @classmethod
    def _from_proto(cls, feature_set_item: FeatureSetItem, fco_container: FcoContainer):
        """
        :param feature_set_item: FSI proto
        :param fco_container: Contains all FSI dependencies (transitively), e.g., FV, Entities, DS-es, Transformations
        """

        join_keys = [(i.spine_column_name, i.package_column_name) for i in feature_set_item.join_configuration_items]
        fv_proto = fco_container.get_by_id(IdHelper.to_string(feature_set_item.feature_view_id))
        feature_definition = FeatureDefinition(fv_proto, fco_container)
        return FeatureDefinitionAndJoinConfig(
            feature_definition=feature_definition,
            name=feature_definition.name,
            join_keys=join_keys,
            namespace=feature_set_item.namespace,
            features=list(feature_set_item.feature_columns),
        )

    def _key(self) -> _Key:
        return _Key(namespace=self.namespace or "", name=self.name)


class FeatureSetConfig(object):
    """
    Config used to create a :class:`FeatureService`.
    """

    # This stores all the features + all the odfv dependent features
    _definitions_and_configs: List[FeatureDefinitionAndJoinConfig]

    def __init__(self):
        """
        Initialize a new FeatureSetConfig.
        """

        self._definitions_and_configs = []

    def _add(
        self,
        fd: FeatureDefinition,
        namespace: Optional[str] = None,
    ):
        if namespace is None:
            namespace = fd.name

        fd_and_config = FeatureSetConfig._make_definition_and_config(fd, namespace=namespace)
        self._definitions_and_configs.append(fd_and_config)

    @property  # type: ignore
    def feature_definitions(self) -> List[FeatureDefinition]:
        """
        Returns the FeatureViews/FeatureTables enclosed in this FeatureSetConfig.
        """
        return [config.feature_definition for config in self._get_feature_definitions_and_join_configs()]

    @property  # type: ignore
    def features(self) -> List[str]:
        """
        Returns the features generated by the enclosed feature definitions.
        """
        return [
            features
            for config in self._get_feature_definitions_and_join_configs()
            for features in FeatureSetConfig._get_full_feature_names(config)
        ]

    @staticmethod
    def _get_full_feature_names(config: FeatureDefinitionAndJoinConfig):
        return [config.namespace + "." + feature if config.namespace else feature for feature in config.features]

    @staticmethod
    def _make_definition_and_config(fd: FeatureDefinition, namespace: str) -> FeatureDefinitionAndJoinConfig:
        join_keys = [(join_key, join_key) for join_key in fd.join_keys]
        features = fd.features

        return FeatureDefinitionAndJoinConfig(
            feature_definition=fd, name=fd.name, join_keys=join_keys, namespace=namespace, features=features
        )

    def _get_feature_definitions_and_join_configs(self) -> List[FeatureDefinitionAndJoinConfig]:
        """
        Returns a list of all feature definitions and their configs in the insertion order.
        """
        return self._definitions_and_configs

    @classmethod
    def _from_protos(cls, feature_set_items, fco_container: FcoContainer):
        """
        :param feature_set_items: FSI protos
        :param fco_container: Contains all FSI dependencies (transitively), e.g., FVs, Entities, DS-es, Transformations
        """
        config = FeatureSetConfig()
        config._definitions_and_configs = [
            FeatureDefinitionAndJoinConfig._from_proto(p, fco_container) for p in feature_set_items
        ]
        return config
