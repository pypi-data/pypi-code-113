# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JWK(object):
    """
    JWK model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JWK object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param n:
            The value to assign to the n property of this JWK.
        :type n: str

        :param e:
            The value to assign to the e property of this JWK.
        :type e: str

        :param kid:
            The value to assign to the kid property of this JWK.
        :type kid: str

        :param use:
            The value to assign to the use property of this JWK.
        :type use: str

        :param alg:
            The value to assign to the alg property of this JWK.
        :type alg: str

        :param kty:
            The value to assign to the kty property of this JWK.
        :type kty: str

        """
        self.swagger_types = {
            'n': 'str',
            'e': 'str',
            'kid': 'str',
            'use': 'str',
            'alg': 'str',
            'kty': 'str'
        }

        self.attribute_map = {
            'n': 'n',
            'e': 'e',
            'kid': 'kid',
            'use': 'use',
            'alg': 'alg',
            'kty': 'kty'
        }

        self._n = None
        self._e = None
        self._kid = None
        self._use = None
        self._alg = None
        self._kty = None

    @property
    def n(self):
        """
        **[Required]** Gets the n of this JWK.
        The modulus.


        :return: The n of this JWK.
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """
        Sets the n of this JWK.
        The modulus.


        :param n: The n of this JWK.
        :type: str
        """
        self._n = n

    @property
    def e(self):
        """
        **[Required]** Gets the e of this JWK.
        The exponent.


        :return: The e of this JWK.
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """
        Sets the e of this JWK.
        The exponent.


        :param e: The e of this JWK.
        :type: str
        """
        self._e = e

    @property
    def kid(self):
        """
        **[Required]** Gets the kid of this JWK.
        The key id.


        :return: The kid of this JWK.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """
        Sets the kid of this JWK.
        The key id.


        :param kid: The kid of this JWK.
        :type: str
        """
        self._kid = kid

    @property
    def use(self):
        """
        **[Required]** Gets the use of this JWK.
        The key use.


        :return: The use of this JWK.
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """
        Sets the use of this JWK.
        The key use.


        :param use: The use of this JWK.
        :type: str
        """
        self._use = use

    @property
    def alg(self):
        """
        **[Required]** Gets the alg of this JWK.
        The algorithm.


        :return: The alg of this JWK.
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """
        Sets the alg of this JWK.
        The algorithm.


        :param alg: The alg of this JWK.
        :type: str
        """
        self._alg = alg

    @property
    def kty(self):
        """
        **[Required]** Gets the kty of this JWK.
        The key type.


        :return: The kty of this JWK.
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """
        Sets the kty of this JWK.
        The key type.


        :param kty: The kty of this JWK.
        :type: str
        """
        self._kty = kty

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
