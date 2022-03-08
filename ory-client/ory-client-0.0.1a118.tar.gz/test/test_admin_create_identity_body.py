"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.118
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.admin_identity_import_credentials import AdminIdentityImportCredentials
from ory_client.model.identity_state import IdentityState
from ory_client.model.recovery_address import RecoveryAddress
from ory_client.model.verifiable_identity_address import VerifiableIdentityAddress
globals()['AdminIdentityImportCredentials'] = AdminIdentityImportCredentials
globals()['IdentityState'] = IdentityState
globals()['RecoveryAddress'] = RecoveryAddress
globals()['VerifiableIdentityAddress'] = VerifiableIdentityAddress
from ory_client.model.admin_create_identity_body import AdminCreateIdentityBody


class TestAdminCreateIdentityBody(unittest.TestCase):
    """AdminCreateIdentityBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdminCreateIdentityBody(self):
        """Test AdminCreateIdentityBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AdminCreateIdentityBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
