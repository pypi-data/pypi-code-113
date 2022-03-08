# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ColumnArgs', 'Column']

@pulumi.input_type
class ColumnArgs:
    def __init__(__self__, *,
                 dataset: pulumi.Input[str],
                 key_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Column resource.
        :param pulumi.Input[str] dataset: The dataset this column is added to.
        :param pulumi.Input[str] key_name: The name of the column. Must be unique per dataset.
        :param pulumi.Input[str] description: A description that is shown in the UI.
        :param pulumi.Input[bool] hidden: Whether this column should be hidden in the query builder and sample data. Defaults to false.
        :param pulumi.Input[str] type: The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
        """
        pulumi.set(__self__, "dataset", dataset)
        pulumi.set(__self__, "key_name", key_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if hidden is not None:
            pulumi.set(__self__, "hidden", hidden)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[str]:
        """
        The dataset this column is added to.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[str]:
        """
        The name of the column. Must be unique per dataset.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description that is shown in the UI.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this column should be hidden in the query builder and sample data. Defaults to false.
        """
        return pulumi.get(self, "hidden")

    @hidden.setter
    def hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hidden", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _ColumnState:
    def __init__(__self__, *,
                 dataset: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Column resources.
        :param pulumi.Input[str] dataset: The dataset this column is added to.
        :param pulumi.Input[str] description: A description that is shown in the UI.
        :param pulumi.Input[bool] hidden: Whether this column should be hidden in the query builder and sample data. Defaults to false.
        :param pulumi.Input[str] key_name: The name of the column. Must be unique per dataset.
        :param pulumi.Input[str] type: The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
        """
        if dataset is not None:
            pulumi.set(__self__, "dataset", dataset)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if hidden is not None:
            pulumi.set(__self__, "hidden", hidden)
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[str]]:
        """
        The dataset this column is added to.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description that is shown in the UI.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this column should be hidden in the query builder and sample data. Defaults to false.
        """
        return pulumi.get(self, "hidden")

    @hidden.setter
    def hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hidden", value)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the column. Must be unique per dataset.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Column(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        config = pulumi.Config()
        dataset = config.require("dataset")
        duration_ms = honeycomb.Column("durationMs",
            key_name="duration_ms_log10",
            type="float",
            description="Duration of the trace",
            dataset=dataset)
        ```

        ## Import

        Columns can be imported using a combination of the dataset name and their key name, e.g.

        ```sh
         $ pulumi import honeycomb:index/column:Column my_column my-dataset/duration_ms
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dataset: The dataset this column is added to.
        :param pulumi.Input[str] description: A description that is shown in the UI.
        :param pulumi.Input[bool] hidden: Whether this column should be hidden in the query builder and sample data. Defaults to false.
        :param pulumi.Input[str] key_name: The name of the column. Must be unique per dataset.
        :param pulumi.Input[str] type: The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ColumnArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        config = pulumi.Config()
        dataset = config.require("dataset")
        duration_ms = honeycomb.Column("durationMs",
            key_name="duration_ms_log10",
            type="float",
            description="Duration of the trace",
            dataset=dataset)
        ```

        ## Import

        Columns can be imported using a combination of the dataset name and their key name, e.g.

        ```sh
         $ pulumi import honeycomb:index/column:Column my_column my-dataset/duration_ms
        ```

        :param str resource_name: The name of the resource.
        :param ColumnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ColumnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ColumnArgs.__new__(ColumnArgs)

            if dataset is None and not opts.urn:
                raise TypeError("Missing required property 'dataset'")
            __props__.__dict__["dataset"] = dataset
            __props__.__dict__["description"] = description
            __props__.__dict__["hidden"] = hidden
            if key_name is None and not opts.urn:
                raise TypeError("Missing required property 'key_name'")
            __props__.__dict__["key_name"] = key_name
            __props__.__dict__["type"] = type
        super(Column, __self__).__init__(
            'honeycomb:index/column:Column',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dataset: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            hidden: Optional[pulumi.Input[bool]] = None,
            key_name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Column':
        """
        Get an existing Column resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dataset: The dataset this column is added to.
        :param pulumi.Input[str] description: A description that is shown in the UI.
        :param pulumi.Input[bool] hidden: Whether this column should be hidden in the query builder and sample data. Defaults to false.
        :param pulumi.Input[str] key_name: The name of the column. Must be unique per dataset.
        :param pulumi.Input[str] type: The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ColumnState.__new__(_ColumnState)

        __props__.__dict__["dataset"] = dataset
        __props__.__dict__["description"] = description
        __props__.__dict__["hidden"] = hidden
        __props__.__dict__["key_name"] = key_name
        __props__.__dict__["type"] = type
        return Column(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[str]:
        """
        The dataset this column is added to.
        """
        return pulumi.get(self, "dataset")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description that is shown in the UI.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hidden(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this column should be hidden in the query builder and sample data. Defaults to false.
        """
        return pulumi.get(self, "hidden")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[str]:
        """
        The name of the column. Must be unique per dataset.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
        """
        return pulumi.get(self, "type")

