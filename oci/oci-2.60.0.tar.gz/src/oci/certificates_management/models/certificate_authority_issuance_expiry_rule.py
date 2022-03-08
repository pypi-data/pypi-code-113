# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .certificate_authority_rule import CertificateAuthorityRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateAuthorityIssuanceExpiryRule(CertificateAuthorityRule):
    """
    A rule that enforces how long certificates or certificate authorities (CAs) issued by this particular CA are valid.
    You must include either or both `leafCertificateMaxValidityDuration` and `certificateAuthorityMaxValidityDuration`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateAuthorityIssuanceExpiryRule object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates_management.models.CertificateAuthorityIssuanceExpiryRule.rule_type` attribute
        of this class is ``CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rule_type:
            The value to assign to the rule_type property of this CertificateAuthorityIssuanceExpiryRule.
            Allowed values for this property are: "CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE"
        :type rule_type: str

        :param leaf_certificate_max_validity_duration:
            The value to assign to the leaf_certificate_max_validity_duration property of this CertificateAuthorityIssuanceExpiryRule.
        :type leaf_certificate_max_validity_duration: str

        :param certificate_authority_max_validity_duration:
            The value to assign to the certificate_authority_max_validity_duration property of this CertificateAuthorityIssuanceExpiryRule.
        :type certificate_authority_max_validity_duration: str

        """
        self.swagger_types = {
            'rule_type': 'str',
            'leaf_certificate_max_validity_duration': 'str',
            'certificate_authority_max_validity_duration': 'str'
        }

        self.attribute_map = {
            'rule_type': 'ruleType',
            'leaf_certificate_max_validity_duration': 'leafCertificateMaxValidityDuration',
            'certificate_authority_max_validity_duration': 'certificateAuthorityMaxValidityDuration'
        }

        self._rule_type = None
        self._leaf_certificate_max_validity_duration = None
        self._certificate_authority_max_validity_duration = None
        self._rule_type = 'CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE'

    @property
    def leaf_certificate_max_validity_duration(self):
        """
        Gets the leaf_certificate_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        A property indicating the maximum validity duration, in days, of leaf certificates issued by this CA.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :return: The leaf_certificate_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        :rtype: str
        """
        return self._leaf_certificate_max_validity_duration

    @leaf_certificate_max_validity_duration.setter
    def leaf_certificate_max_validity_duration(self, leaf_certificate_max_validity_duration):
        """
        Sets the leaf_certificate_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        A property indicating the maximum validity duration, in days, of leaf certificates issued by this CA.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :param leaf_certificate_max_validity_duration: The leaf_certificate_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        :type: str
        """
        self._leaf_certificate_max_validity_duration = leaf_certificate_max_validity_duration

    @property
    def certificate_authority_max_validity_duration(self):
        """
        Gets the certificate_authority_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        A property indicating the maximum validity duration, in days, of subordinate CA's issued by this CA.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :return: The certificate_authority_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        :rtype: str
        """
        return self._certificate_authority_max_validity_duration

    @certificate_authority_max_validity_duration.setter
    def certificate_authority_max_validity_duration(self, certificate_authority_max_validity_duration):
        """
        Sets the certificate_authority_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        A property indicating the maximum validity duration, in days, of subordinate CA's issued by this CA.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :param certificate_authority_max_validity_duration: The certificate_authority_max_validity_duration of this CertificateAuthorityIssuanceExpiryRule.
        :type: str
        """
        self._certificate_authority_max_validity_duration = certificate_authority_max_validity_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
