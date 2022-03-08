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
from ory_client.model.admin_create_identity_import_credentials_oidc import AdminCreateIdentityImportCredentialsOidc
from ory_client.model.admin_create_identity_import_credentials_password import AdminCreateIdentityImportCredentialsPassword
globals()['AdminCreateIdentityImportCredentialsOidc'] = AdminCreateIdentityImportCredentialsOidc
globals()['AdminCreateIdentityImportCredentialsPassword'] = AdminCreateIdentityImportCredentialsPassword
from ory_client.model.admin_identity_import_credentials import AdminIdentityImportCredentials


class TestAdminIdentityImportCredentials(unittest.TestCase):
    """AdminIdentityImportCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdminIdentityImportCredentials(self):
        """Test AdminIdentityImportCredentials"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AdminIdentityImportCredentials()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
