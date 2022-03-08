# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OntologyClass(object):
    """
    Images and ImageObjects can be labeled with an OntologyClass.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OntologyClass object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this OntologyClass.
        :type name: str

        :param parent_names:
            The value to assign to the parent_names property of this OntologyClass.
        :type parent_names: list[str]

        :param synonym_names:
            The value to assign to the synonym_names property of this OntologyClass.
        :type synonym_names: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'parent_names': 'list[str]',
            'synonym_names': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'parent_names': 'parentNames',
            'synonym_names': 'synonymNames'
        }

        self._name = None
        self._parent_names = None
        self._synonym_names = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OntologyClass.
        Name of the label.


        :return: The name of this OntologyClass.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OntologyClass.
        Name of the label.


        :param name: The name of this OntologyClass.
        :type: str
        """
        self._name = name

    @property
    def parent_names(self):
        """
        Gets the parent_names of this OntologyClass.
        Parents of the label.


        :return: The parent_names of this OntologyClass.
        :rtype: list[str]
        """
        return self._parent_names

    @parent_names.setter
    def parent_names(self, parent_names):
        """
        Sets the parent_names of this OntologyClass.
        Parents of the label.


        :param parent_names: The parent_names of this OntologyClass.
        :type: list[str]
        """
        self._parent_names = parent_names

    @property
    def synonym_names(self):
        """
        Gets the synonym_names of this OntologyClass.
        Synonyms of the label.


        :return: The synonym_names of this OntologyClass.
        :rtype: list[str]
        """
        return self._synonym_names

    @synonym_names.setter
    def synonym_names(self, synonym_names):
        """
        Sets the synonym_names of this OntologyClass.
        Synonyms of the label.


        :param synonym_names: The synonym_names of this OntologyClass.
        :type: list[str]
        """
        self._synonym_names = synonym_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
