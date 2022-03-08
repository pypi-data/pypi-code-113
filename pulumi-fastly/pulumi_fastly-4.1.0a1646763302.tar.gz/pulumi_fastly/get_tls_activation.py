# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetTlsActivationResult',
    'AwaitableGetTlsActivationResult',
    'get_tls_activation',
    'get_tls_activation_output',
]

@pulumi.output_type
class GetTlsActivationResult:
    """
    A collection of values returned by getTlsActivation.
    """
    def __init__(__self__, certificate_id=None, configuration_id=None, created_at=None, domain=None, id=None):
        if certificate_id and not isinstance(certificate_id, str):
            raise TypeError("Expected argument 'certificate_id' to be a str")
        pulumi.set(__self__, "certificate_id", certificate_id)
        if configuration_id and not isinstance(configuration_id, str):
            raise TypeError("Expected argument 'configuration_id' to be a str")
        pulumi.set(__self__, "configuration_id", configuration_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> str:
        """
        ID of the TLS Certificate used.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> str:
        """
        ID of the TLS Configuration used.
        """
        return pulumi.get(self, "configuration_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Timestamp (GMT) when TLS was enabled.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def domain(self) -> str:
        """
        Domain that TLS was enabled on.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fastly Activation ID. Conflicts with all other filters.
        """
        return pulumi.get(self, "id")


class AwaitableGetTlsActivationResult(GetTlsActivationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTlsActivationResult(
            certificate_id=self.certificate_id,
            configuration_id=self.configuration_id,
            created_at=self.created_at,
            domain=self.domain,
            id=self.id)


def get_tls_activation(certificate_id: Optional[str] = None,
                       configuration_id: Optional[str] = None,
                       domain: Optional[str] = None,
                       id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTlsActivationResult:
    """
    Use this data source to get information on a TLS activation, including the certificate used, and the domain on which TLS was enabled.

    > **Warning:** The data source's filters are applied using an **AND** boolean operator, so depending on the combination
    of filters, they may become mutually exclusive. The exception to this is `id` which must not be specified in combination
    with any of the others.

    > **Note:** If more or less than a single match is returned by the search, this provider will fail. Ensure that your search is specific enough to return a single key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fastly as fastly

    example = fastly.get_tls_activation(domain="example.com")
    ```


    :param str certificate_id: ID of the TLS Certificate used.
    :param str configuration_id: ID of the TLS Configuration used.
    :param str domain: Domain that TLS was enabled on.
    :param str id: Fastly Activation ID. Conflicts with all other filters.
    """
    __args__ = dict()
    __args__['certificateId'] = certificate_id
    __args__['configurationId'] = configuration_id
    __args__['domain'] = domain
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('fastly:index/getTlsActivation:getTlsActivation', __args__, opts=opts, typ=GetTlsActivationResult).value

    return AwaitableGetTlsActivationResult(
        certificate_id=__ret__.certificate_id,
        configuration_id=__ret__.configuration_id,
        created_at=__ret__.created_at,
        domain=__ret__.domain,
        id=__ret__.id)


@_utilities.lift_output_func(get_tls_activation)
def get_tls_activation_output(certificate_id: Optional[pulumi.Input[Optional[str]]] = None,
                              configuration_id: Optional[pulumi.Input[Optional[str]]] = None,
                              domain: Optional[pulumi.Input[Optional[str]]] = None,
                              id: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTlsActivationResult]:
    """
    Use this data source to get information on a TLS activation, including the certificate used, and the domain on which TLS was enabled.

    > **Warning:** The data source's filters are applied using an **AND** boolean operator, so depending on the combination
    of filters, they may become mutually exclusive. The exception to this is `id` which must not be specified in combination
    with any of the others.

    > **Note:** If more or less than a single match is returned by the search, this provider will fail. Ensure that your search is specific enough to return a single key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fastly as fastly

    example = fastly.get_tls_activation(domain="example.com")
    ```


    :param str certificate_id: ID of the TLS Certificate used.
    :param str configuration_id: ID of the TLS Configuration used.
    :param str domain: Domain that TLS was enabled on.
    :param str id: Fastly Activation ID. Conflicts with all other filters.
    """
    ...
