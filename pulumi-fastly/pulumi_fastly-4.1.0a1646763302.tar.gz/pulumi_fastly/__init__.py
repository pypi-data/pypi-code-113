# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .get_datacenters import *
from .get_fastly_ip_ranges import *
from .get_tls_activation import *
from .get_tls_activation_ids import *
from .get_tls_certificate import *
from .get_tls_certificate_ids import *
from .get_tls_configuration import *
from .get_tls_configuration_ids import *
from .get_tls_domain import *
from .get_tls_platform_certificate import *
from .get_tls_platform_certificate_ids import *
from .get_tls_private_key import *
from .get_tls_private_key_ids import *
from .get_tls_subscription import *
from .get_tls_subscription_ids import *
from .get_waf_rules import *
from .provider import *
from .service_acl_entries import *
from .service_compute import *
from .service_dictionary_items import *
from .service_dynamic_snippet_content import *
from .service_vcl import *
from .service_waf_configuration import *
from .tls_activation import *
from .tls_certificate import *
from .tls_platform_certificate import *
from .tls_private_key import *
from .tls_subscription import *
from .tls_subscription_validation import *
from .user import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_fastly.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_fastly.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "fastly",
  "mod": "index/serviceACLEntries",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/serviceACLEntries:ServiceACLEntries": "ServiceACLEntries"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/serviceCompute",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/serviceCompute:ServiceCompute": "ServiceCompute"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/serviceDictionaryItems",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/serviceDictionaryItems:ServiceDictionaryItems": "ServiceDictionaryItems"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/serviceDynamicSnippetContent",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/serviceDynamicSnippetContent:ServiceDynamicSnippetContent": "ServiceDynamicSnippetContent"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/serviceVcl",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/serviceVcl:ServiceVcl": "ServiceVcl"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/serviceWafConfiguration",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/serviceWafConfiguration:ServiceWafConfiguration": "ServiceWafConfiguration"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/tlsActivation",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/tlsActivation:TlsActivation": "TlsActivation"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/tlsCertificate",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/tlsCertificate:TlsCertificate": "TlsCertificate"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/tlsPlatformCertificate",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/tlsPlatformCertificate:TlsPlatformCertificate": "TlsPlatformCertificate"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/tlsPrivateKey",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/tlsPrivateKey:TlsPrivateKey": "TlsPrivateKey"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/tlsSubscription",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/tlsSubscription:TlsSubscription": "TlsSubscription"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/tlsSubscriptionValidation",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/tlsSubscriptionValidation:TlsSubscriptionValidation": "TlsSubscriptionValidation"
  }
 },
 {
  "pkg": "fastly",
  "mod": "index/user",
  "fqn": "pulumi_fastly",
  "classes": {
   "fastly:index/user:User": "User"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "fastly",
  "token": "pulumi:providers:fastly",
  "fqn": "pulumi_fastly",
  "class": "Provider"
 }
]
"""
)
