# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('honeycomb')


class _ExportableConfig(types.ModuleType):
    @property
    def api_key(self) -> Optional[str]:
        return __config__.get('apiKey')

    @property
    def api_url(self) -> Optional[str]:
        return __config__.get('apiUrl')

    @property
    def debug(self) -> Optional[bool]:
        return __config__.get_bool('debug')

