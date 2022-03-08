# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployArtifactSource(object):
    """
    Specifies source of an artifact.
    """

    #: A constant which can be used with the deploy_artifact_source_type property of a DeployArtifactSource.
    #: This constant has a value of "INLINE"
    DEPLOY_ARTIFACT_SOURCE_TYPE_INLINE = "INLINE"

    #: A constant which can be used with the deploy_artifact_source_type property of a DeployArtifactSource.
    #: This constant has a value of "OCIR"
    DEPLOY_ARTIFACT_SOURCE_TYPE_OCIR = "OCIR"

    #: A constant which can be used with the deploy_artifact_source_type property of a DeployArtifactSource.
    #: This constant has a value of "GENERIC_ARTIFACT"
    DEPLOY_ARTIFACT_SOURCE_TYPE_GENERIC_ARTIFACT = "GENERIC_ARTIFACT"

    def __init__(self, **kwargs):
        """
        Initializes a new DeployArtifactSource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.GenericDeployArtifactSource`
        * :class:`~oci.devops.models.OcirDeployArtifactSource`
        * :class:`~oci.devops.models.InlineDeployArtifactSource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_source_type:
            The value to assign to the deploy_artifact_source_type property of this DeployArtifactSource.
            Allowed values for this property are: "INLINE", "OCIR", "GENERIC_ARTIFACT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deploy_artifact_source_type: str

        """
        self.swagger_types = {
            'deploy_artifact_source_type': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_source_type': 'deployArtifactSourceType'
        }

        self._deploy_artifact_source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deployArtifactSourceType']

        if type == 'GENERIC_ARTIFACT':
            return 'GenericDeployArtifactSource'

        if type == 'OCIR':
            return 'OcirDeployArtifactSource'

        if type == 'INLINE':
            return 'InlineDeployArtifactSource'
        else:
            return 'DeployArtifactSource'

    @property
    def deploy_artifact_source_type(self):
        """
        **[Required]** Gets the deploy_artifact_source_type of this DeployArtifactSource.
        Specifies types of artifact sources.

        Allowed values for this property are: "INLINE", "OCIR", "GENERIC_ARTIFACT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deploy_artifact_source_type of this DeployArtifactSource.
        :rtype: str
        """
        return self._deploy_artifact_source_type

    @deploy_artifact_source_type.setter
    def deploy_artifact_source_type(self, deploy_artifact_source_type):
        """
        Sets the deploy_artifact_source_type of this DeployArtifactSource.
        Specifies types of artifact sources.


        :param deploy_artifact_source_type: The deploy_artifact_source_type of this DeployArtifactSource.
        :type: str
        """
        allowed_values = ["INLINE", "OCIR", "GENERIC_ARTIFACT"]
        if not value_allowed_none_or_none_sentinel(deploy_artifact_source_type, allowed_values):
            deploy_artifact_source_type = 'UNKNOWN_ENUM_VALUE'
        self._deploy_artifact_source_type = deploy_artifact_source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
