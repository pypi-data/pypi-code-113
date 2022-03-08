# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetTlsPlatformCertificateIdsResult',
    'AwaitableGetTlsPlatformCertificateIdsResult',
    'get_tls_platform_certificate_ids',
]

@pulumi.output_type
class GetTlsPlatformCertificateIdsResult:
    """
    A collection of values returned by getTlsPlatformCertificateIds.
    """
    def __init__(__self__, id=None, ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        List of IDs corresponding to Platform TLS certificates.
        """
        return pulumi.get(self, "ids")


class AwaitableGetTlsPlatformCertificateIdsResult(GetTlsPlatformCertificateIdsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTlsPlatformCertificateIdsResult(
            id=self.id,
            ids=self.ids)


def get_tls_platform_certificate_ids(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTlsPlatformCertificateIdsResult:
    """
    Use this data source to get the IDs of available Platform TLS Certificates for use with other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fastly as fastly

    example_tls_platform_certificate_ids = fastly.get_tls_platform_certificate_ids()
    example_tls_platform_certificate = fastly.get_tls_platform_certificate(id=example_tls_platform_certificate_ids.ids[0])
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('fastly:index/getTlsPlatformCertificateIds:getTlsPlatformCertificateIds', __args__, opts=opts, typ=GetTlsPlatformCertificateIdsResult).value

    return AwaitableGetTlsPlatformCertificateIdsResult(
        id=__ret__.id,
        ids=__ret__.ids)
