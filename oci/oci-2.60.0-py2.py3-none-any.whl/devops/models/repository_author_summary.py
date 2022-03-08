# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryAuthorSummary(object):
    """
    Object containing summary of authors in a repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryAuthorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param author_name:
            The value to assign to the author_name property of this RepositoryAuthorSummary.
        :type author_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RepositoryAuthorSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RepositoryAuthorSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'author_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'author_name': 'authorName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._author_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def author_name(self):
        """
        **[Required]** Gets the author_name of this RepositoryAuthorSummary.
        Author name.


        :return: The author_name of this RepositoryAuthorSummary.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """
        Sets the author_name of this RepositoryAuthorSummary.
        Author name.


        :param author_name: The author_name of this RepositoryAuthorSummary.
        :type: str
        """
        self._author_name = author_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RepositoryAuthorSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RepositoryAuthorSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RepositoryAuthorSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RepositoryAuthorSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RepositoryAuthorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RepositoryAuthorSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RepositoryAuthorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RepositoryAuthorSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
