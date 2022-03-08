# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('health_checks.health_checks_root_group.command_name', 'health-checks'), cls=CommandGroupWithAlias, help=cli_util.override('health_checks.health_checks_root_group.help', """API for the Health Checks service. Use this API to manage endpoint probes and monitors.
For more information, see
[Overview of the Health Checks Service]."""), short_help=cli_util.override('health_checks.health_checks_root_group.short_help', """Health Checks API"""))
@cli_util.help_option_group
def health_checks_root_group():
    pass


@click.command(cli_util.override('health_checks.ping_monitor_group.command_name', 'ping-monitor'), cls=CommandGroupWithAlias, help="""A summary containing all of the mutable and immutable properties for a ping monitor.""")
@cli_util.help_option_group
def ping_monitor_group():
    pass


@click.command(cli_util.override('health_checks.ping_probe_group.command_name', 'ping-probe'), cls=CommandGroupWithAlias, help="""This model contains all of the mutable and immutable properties for a ping probe.""")
@cli_util.help_option_group
def ping_probe_group():
    pass


@click.command(cli_util.override('health_checks.health_checks_vantage_point_group.command_name', 'health-checks-vantage-point'), cls=CommandGroupWithAlias, help="""Information about a vantage point.""")
@cli_util.help_option_group
def health_checks_vantage_point_group():
    pass


@click.command(cli_util.override('health_checks.http_monitor_group.command_name', 'http-monitor'), cls=CommandGroupWithAlias, help="""This model contains all of the mutable and immutable properties for an HTTP monitor.""")
@cli_util.help_option_group
def http_monitor_group():
    pass


@click.command(cli_util.override('health_checks.http_probe_result_group.command_name', 'http-probe-result'), cls=CommandGroupWithAlias, help="""The results returned by running an HTTP probe.  All times and durations are returned in milliseconds. All times are relative to the POSIX epoch (1970-01-01T00:00Z). Time properties conform to W3C Resource Timing. For more information, see [PerformanceResourceTiming] interface.""")
@cli_util.help_option_group
def http_probe_result_group():
    pass


@click.command(cli_util.override('health_checks.ping_probe_result_group.command_name', 'ping-probe-result'), cls=CommandGroupWithAlias, help="""The results returned by running a ping probe.  All times and durations are returned in milliseconds. All times are relative to the POSIX epoch (1970-01-01T00:00Z).""")
@cli_util.help_option_group
def ping_probe_result_group():
    pass


@click.command(cli_util.override('health_checks.http_probe_group.command_name', 'http-probe'), cls=CommandGroupWithAlias, help="""A summary that contains all of the mutable and immutable properties for an HTTP probe.""")
@cli_util.help_option_group
def http_probe_group():
    pass


health_checks_root_group.add_command(ping_monitor_group)
health_checks_root_group.add_command(ping_probe_group)
health_checks_root_group.add_command(health_checks_vantage_point_group)
health_checks_root_group.add_command(http_monitor_group)
health_checks_root_group.add_command(http_probe_result_group)
health_checks_root_group.add_command(ping_probe_result_group)
health_checks_root_group.add_command(http_probe_group)


@http_monitor_group.command(name=cli_util.override('health_checks.change_http_monitor_compartment.command_name', 'change-compartment'), help=u"""Moves a monitor into a different compartment. When provided, `If-Match` is checked against ETag values of the resource. \n[Command Reference](changeHttpMonitorCompartment)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_http_monitor_compartment(ctx, from_json, monitor_id, compartment_id, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.change_http_monitor_compartment(
        monitor_id=monitor_id,
        change_http_monitor_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ping_monitor_group.command(name=cli_util.override('health_checks.change_ping_monitor_compartment.command_name', 'change-compartment'), help=u"""Moves a monitor into a different compartment. When provided, `If-Match` is checked against ETag values of the resource. \n[Command Reference](changePingMonitorCompartment)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ping_monitor_compartment(ctx, from_json, monitor_id, compartment_id, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.change_ping_monitor_compartment(
        monitor_id=monitor_id,
        change_ping_monitor_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@http_monitor_group.command(name=cli_util.override('health_checks.create_http_monitor.command_name', 'create'), help=u"""Creates an HTTP monitor. Vantage points will be automatically selected if not specified, and probes will be initiated from each vantage point to each of the targets at the frequency specified by `intervalInSeconds`. \n[Command Reference](createHttpMonitor)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--targets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of targets (hostnames or IP addresses) of the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protocol', required=True, type=custom_types.CliCaseInsensitiveChoice(["HTTP", "HTTPS"]), help=u"""""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly and mutable name suitable for display in a user interface.""")
@cli_util.option('--interval-in-seconds', required=True, type=click.INT, help=u"""The monitor interval in seconds. Valid values: 10, 30, and 60.""")
@cli_util.option('--vantage-point-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of names of vantage points from which to execute the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--port', type=click.INT, help=u"""The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.""")
@cli_util.option('--method', type=custom_types.CliCaseInsensitiveChoice(["GET", "HEAD"]), help=u"""""")
@cli_util.option('--path', help=u"""The optional URL path to probe, including query parameters.""")
@cli_util.option('--headers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A dictionary of HTTP request headers.

*Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Enables or disables the monitor. Set to 'true' to launch monitoring.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.  For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'headers': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'headers': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'healthchecks', 'class': 'HttpMonitor'})
@cli_util.wrap_exceptions
def create_http_monitor(ctx, from_json, compartment_id, targets, protocol, display_name, interval_in_seconds, vantage_point_names, port, timeout_in_seconds, method, path, headers, is_enabled, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['targets'] = cli_util.parse_json_parameter("targets", targets)
    _details['protocol'] = protocol
    _details['displayName'] = display_name
    _details['intervalInSeconds'] = interval_in_seconds

    if vantage_point_names is not None:
        _details['vantagePointNames'] = cli_util.parse_json_parameter("vantage_point_names", vantage_point_names)

    if port is not None:
        _details['port'] = port

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if method is not None:
        _details['method'] = method

    if path is not None:
        _details['path'] = path

    if headers is not None:
        _details['headers'] = cli_util.parse_json_parameter("headers", headers)

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.create_http_monitor(
        create_http_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@http_probe_group.command(name=cli_util.override('health_checks.create_on_demand_http_probe.command_name', 'create-on-demand'), help=u"""Creates an on-demand HTTP probe. The location response header contains the URL for fetching the probe results.

*Note:* On-demand probe configurations are not saved. \n[Command Reference](createOnDemandHttpProbe)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--targets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of targets (hostnames or IP addresses) of the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protocol', required=True, type=custom_types.CliCaseInsensitiveChoice(["HTTP", "HTTPS"]), help=u"""""")
@cli_util.option('--vantage-point-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of names of vantage points from which to execute the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--port', type=click.INT, help=u"""The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.""")
@cli_util.option('--method', type=custom_types.CliCaseInsensitiveChoice(["GET", "HEAD"]), help=u"""""")
@cli_util.option('--path', help=u"""The optional URL path to probe, including query parameters.""")
@cli_util.option('--headers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A dictionary of HTTP request headers.

*Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'headers': {'module': 'healthchecks', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'headers': {'module': 'healthchecks', 'class': 'dict(str, string)'}}, output_type={'module': 'healthchecks', 'class': 'HttpProbe'})
@cli_util.wrap_exceptions
def create_on_demand_http_probe(ctx, from_json, compartment_id, targets, protocol, vantage_point_names, port, timeout_in_seconds, method, path, headers):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['targets'] = cli_util.parse_json_parameter("targets", targets)
    _details['protocol'] = protocol

    if vantage_point_names is not None:
        _details['vantagePointNames'] = cli_util.parse_json_parameter("vantage_point_names", vantage_point_names)

    if port is not None:
        _details['port'] = port

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if method is not None:
        _details['method'] = method

    if path is not None:
        _details['path'] = path

    if headers is not None:
        _details['headers'] = cli_util.parse_json_parameter("headers", headers)

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.create_on_demand_http_probe(
        create_on_demand_http_probe_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ping_probe_group.command(name=cli_util.override('health_checks.create_on_demand_ping_probe.command_name', 'create-on-demand'), help=u"""Creates an on-demand ping probe. The location response header contains the URL for fetching probe results.

*Note:* The on-demand probe configuration is not saved. \n[Command Reference](createOnDemandPingProbe)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--targets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of targets (hostnames or IP addresses) of the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protocol', required=True, type=custom_types.CliCaseInsensitiveChoice(["ICMP", "TCP"]), help=u"""""")
@cli_util.option('--vantage-point-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of names of vantage points from which to execute the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--port', type=click.INT, help=u"""The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.""")
@json_skeleton_utils.get_cli_json_input_option({'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}}, output_type={'module': 'healthchecks', 'class': 'PingProbe'})
@cli_util.wrap_exceptions
def create_on_demand_ping_probe(ctx, from_json, compartment_id, targets, protocol, vantage_point_names, port, timeout_in_seconds):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['targets'] = cli_util.parse_json_parameter("targets", targets)
    _details['protocol'] = protocol

    if vantage_point_names is not None:
        _details['vantagePointNames'] = cli_util.parse_json_parameter("vantage_point_names", vantage_point_names)

    if port is not None:
        _details['port'] = port

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.create_on_demand_ping_probe(
        create_on_demand_ping_probe_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ping_monitor_group.command(name=cli_util.override('health_checks.create_ping_monitor.command_name', 'create'), help=u"""Creates a ping monitor. Vantage points will be automatically selected if not specified, and probes will be initiated from each vantage point to each of the targets at the frequency specified by `intervalInSeconds`. \n[Command Reference](createPingMonitor)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--targets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of targets (hostnames or IP addresses) of the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protocol', required=True, type=custom_types.CliCaseInsensitiveChoice(["ICMP", "TCP"]), help=u"""""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly and mutable name suitable for display in a user interface.""")
@cli_util.option('--interval-in-seconds', required=True, type=click.INT, help=u"""The monitor interval in seconds. Valid values: 10, 30, and 60.""")
@cli_util.option('--vantage-point-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of names of vantage points from which to execute the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--port', type=click.INT, help=u"""The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Enables or disables the monitor. Set to 'true' to launch monitoring.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.  For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'healthchecks', 'class': 'PingMonitor'})
@cli_util.wrap_exceptions
def create_ping_monitor(ctx, from_json, compartment_id, targets, protocol, display_name, interval_in_seconds, vantage_point_names, port, timeout_in_seconds, is_enabled, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['targets'] = cli_util.parse_json_parameter("targets", targets)
    _details['protocol'] = protocol
    _details['displayName'] = display_name
    _details['intervalInSeconds'] = interval_in_seconds

    if vantage_point_names is not None:
        _details['vantagePointNames'] = cli_util.parse_json_parameter("vantage_point_names", vantage_point_names)

    if port is not None:
        _details['port'] = port

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.create_ping_monitor(
        create_ping_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@http_monitor_group.command(name=cli_util.override('health_checks.delete_http_monitor.command_name', 'delete'), help=u"""Deletes the HTTP monitor and its configuration. All future probes of this monitor are stopped. Results associated with the monitor are not deleted. \n[Command Reference](deleteHttpMonitor)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_http_monitor(ctx, from_json, monitor_id, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.delete_http_monitor(
        monitor_id=monitor_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ping_monitor_group.command(name=cli_util.override('health_checks.delete_ping_monitor.command_name', 'delete'), help=u"""Deletes the ping monitor and its configuration. All future probes of this monitor are stopped. Results associated with the monitor are not deleted. \n[Command Reference](deletePingMonitor)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ping_monitor(ctx, from_json, monitor_id, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.delete_ping_monitor(
        monitor_id=monitor_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@http_monitor_group.command(name=cli_util.override('health_checks.get_http_monitor.command_name', 'get'), help=u"""Gets the configuration for the specified monitor. \n[Command Reference](getHttpMonitor)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'healthchecks', 'class': 'HttpMonitor'})
@cli_util.wrap_exceptions
def get_http_monitor(ctx, from_json, monitor_id, if_none_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.get_http_monitor(
        monitor_id=monitor_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ping_monitor_group.command(name=cli_util.override('health_checks.get_ping_monitor.command_name', 'get'), help=u"""Gets the configuration for the specified ping monitor. \n[Command Reference](getPingMonitor)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'healthchecks', 'class': 'PingMonitor'})
@cli_util.wrap_exceptions
def get_ping_monitor(ctx, from_json, monitor_id, if_none_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.get_ping_monitor(
        monitor_id=monitor_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@health_checks_vantage_point_group.command(name=cli_util.override('health_checks.list_health_checks_vantage_points.command_name', 'list'), help=u"""Gets information about all vantage points available to the user. \n[Command Reference](listHealthChecksVantagePoints)""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "displayName"]), help=u"""The field to sort by when listing vantage points.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Controls the sort order of results.""")
@cli_util.option('--name', help=u"""Filters results that exactly match the `name` field.""")
@cli_util.option('--display-name', help=u"""Filters results that exactly match the `displayName` field.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'healthchecks', 'class': 'list[HealthChecksVantagePointSummary]'})
@cli_util.wrap_exceptions
def list_health_checks_vantage_points(ctx, from_json, all_pages, page_size, limit, page, sort_by, sort_order, name, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_health_checks_vantage_points,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_health_checks_vantage_points,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_health_checks_vantage_points(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@http_monitor_group.command(name=cli_util.override('health_checks.list_http_monitors.command_name', 'list'), help=u"""Gets a list of HTTP monitors. \n[Command Reference](listHttpMonitors)""")
@cli_util.option('--compartment-id', required=True, help=u"""Filters results by compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "displayName", "timeCreated"]), help=u"""The field to sort by when listing monitors.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Controls the sort order of results.""")
@cli_util.option('--display-name', help=u"""Filters results that exactly match the `displayName` field.""")
@cli_util.option('--home-region', help=u"""Filters results that match the `homeRegion`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'healthchecks', 'class': 'list[HttpMonitorSummary]'})
@cli_util.wrap_exceptions
def list_http_monitors(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, display_name, home_region):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if home_region is not None:
        kwargs['home_region'] = home_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_http_monitors,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_http_monitors,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_http_monitors(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@http_probe_result_group.command(name=cli_util.override('health_checks.list_http_probe_results.command_name', 'list'), help=u"""Gets the HTTP probe results for the specified probe or monitor, where the `probeConfigurationId` is the OCID of either a monitor or an on-demand probe. \n[Command Reference](listHttpProbeResults)""")
@cli_util.option('--probe-configuration-id', required=True, help=u"""The OCID of a monitor or on-demand probe.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--start-time-greater-than-or-equal-to', help=u"""Returns results with a `startTime` equal to or greater than the specified value.""")
@cli_util.option('--start-time-less-than-or-equal-to', help=u"""Returns results with a `startTime` equal to or less than the specified value.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Controls the sort order of results.""")
@cli_util.option('--target', help=u"""Filters results that match the `target`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'healthchecks', 'class': 'list[HttpProbeResultSummary]'})
@cli_util.wrap_exceptions
def list_http_probe_results(ctx, from_json, all_pages, page_size, probe_configuration_id, limit, page, start_time_greater_than_or_equal_to, start_time_less_than_or_equal_to, sort_order, target):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(probe_configuration_id, six.string_types) and len(probe_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --probe-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if start_time_greater_than_or_equal_to is not None:
        kwargs['start_time_greater_than_or_equal_to'] = start_time_greater_than_or_equal_to
    if start_time_less_than_or_equal_to is not None:
        kwargs['start_time_less_than_or_equal_to'] = start_time_less_than_or_equal_to
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if target is not None:
        kwargs['target'] = target
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_http_probe_results,
            probe_configuration_id=probe_configuration_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_http_probe_results,
            limit,
            page_size,
            probe_configuration_id=probe_configuration_id,
            **kwargs
        )
    else:
        result = client.list_http_probe_results(
            probe_configuration_id=probe_configuration_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ping_monitor_group.command(name=cli_util.override('health_checks.list_ping_monitors.command_name', 'list'), help=u"""Gets a list of configured ping monitors.

Results are paginated based on `page` and `limit`.  The `opc-next-page` header provides a URL for fetching the next page. \n[Command Reference](listPingMonitors)""")
@cli_util.option('--compartment-id', required=True, help=u"""Filters results by compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "displayName", "timeCreated"]), help=u"""The field to sort by when listing monitors.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Controls the sort order of results.""")
@cli_util.option('--display-name', help=u"""Filters results that exactly match the `displayName` field.""")
@cli_util.option('--home-region', help=u"""Filters results that match the `homeRegion`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'healthchecks', 'class': 'list[PingMonitorSummary]'})
@cli_util.wrap_exceptions
def list_ping_monitors(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, display_name, home_region):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if home_region is not None:
        kwargs['home_region'] = home_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ping_monitors,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ping_monitors,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_ping_monitors(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ping_probe_result_group.command(name=cli_util.override('health_checks.list_ping_probe_results.command_name', 'list'), help=u"""Returns the results for the specified probe, where the `probeConfigurationId` is the OCID of either a monitor or an on-demand probe.

Results are paginated based on `page` and `limit`.  The `opc-next-page` header provides a URL for fetching the next page.  Use `sortOrder` to set the order of the results.  If `sortOrder` is unspecified, results are sorted in ascending order by `startTime`. \n[Command Reference](listPingProbeResults)""")
@cli_util.option('--probe-configuration-id', required=True, help=u"""The OCID of a monitor or on-demand probe.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--start-time-greater-than-or-equal-to', help=u"""Returns results with a `startTime` equal to or greater than the specified value.""")
@cli_util.option('--start-time-less-than-or-equal-to', help=u"""Returns results with a `startTime` equal to or less than the specified value.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Controls the sort order of results.""")
@cli_util.option('--target', help=u"""Filters results that match the `target`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'healthchecks', 'class': 'list[PingProbeResultSummary]'})
@cli_util.wrap_exceptions
def list_ping_probe_results(ctx, from_json, all_pages, page_size, probe_configuration_id, limit, page, start_time_greater_than_or_equal_to, start_time_less_than_or_equal_to, sort_order, target):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(probe_configuration_id, six.string_types) and len(probe_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --probe-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if start_time_greater_than_or_equal_to is not None:
        kwargs['start_time_greater_than_or_equal_to'] = start_time_greater_than_or_equal_to
    if start_time_less_than_or_equal_to is not None:
        kwargs['start_time_less_than_or_equal_to'] = start_time_less_than_or_equal_to
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if target is not None:
        kwargs['target'] = target
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ping_probe_results,
            probe_configuration_id=probe_configuration_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ping_probe_results,
            limit,
            page_size,
            probe_configuration_id=probe_configuration_id,
            **kwargs
        )
    else:
        result = client.list_ping_probe_results(
            probe_configuration_id=probe_configuration_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@http_monitor_group.command(name=cli_util.override('health_checks.update_http_monitor.command_name', 'update'), help=u"""Updates the configuration of the specified HTTP monitor. Only the fields specified in the request body will be updated; all other configuration properties will remain unchanged. \n[Command Reference](updateHttpMonitor)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--targets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of targets (hostnames or IP addresses) of the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vantage-point-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of names of vantage points from which to execute the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--port', type=click.INT, help=u"""The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["HTTP", "HTTPS"]), help=u"""""")
@cli_util.option('--method', type=custom_types.CliCaseInsensitiveChoice(["GET", "HEAD"]), help=u"""""")
@cli_util.option('--path', help=u"""The optional URL path to probe, including query parameters.""")
@cli_util.option('--headers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A dictionary of HTTP request headers.

*Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly and mutable name suitable for display in a user interface.""")
@cli_util.option('--interval-in-seconds', type=click.INT, help=u"""The monitor interval in seconds. Valid values: 10, 30, and 60.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Enables or disables the monitor. Set to 'true' to launch monitoring.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.  For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'headers': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'headers': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'healthchecks', 'class': 'HttpMonitor'})
@cli_util.wrap_exceptions
def update_http_monitor(ctx, from_json, force, monitor_id, targets, vantage_point_names, port, timeout_in_seconds, protocol, method, path, headers, display_name, interval_in_seconds, is_enabled, freeform_tags, defined_tags, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')
    if not force:
        if targets or vantage_point_names or headers or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to targets and vantage-point-names and headers and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if targets is not None:
        _details['targets'] = cli_util.parse_json_parameter("targets", targets)

    if vantage_point_names is not None:
        _details['vantagePointNames'] = cli_util.parse_json_parameter("vantage_point_names", vantage_point_names)

    if port is not None:
        _details['port'] = port

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if protocol is not None:
        _details['protocol'] = protocol

    if method is not None:
        _details['method'] = method

    if path is not None:
        _details['path'] = path

    if headers is not None:
        _details['headers'] = cli_util.parse_json_parameter("headers", headers)

    if display_name is not None:
        _details['displayName'] = display_name

    if interval_in_seconds is not None:
        _details['intervalInSeconds'] = interval_in_seconds

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.update_http_monitor(
        monitor_id=monitor_id,
        update_http_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ping_monitor_group.command(name=cli_util.override('health_checks.update_ping_monitor.command_name', 'update'), help=u"""Updates the configuration of the specified ping monitor. Only the fields specified in the request body will be updated; all other configuration properties will remain unchanged. \n[Command Reference](updatePingMonitor)""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of a monitor.""")
@cli_util.option('--targets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of targets (hostnames or IP addresses) of the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vantage-point-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of names of vantage points from which to execute the probe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--port', type=click.INT, help=u"""The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["ICMP", "TCP"]), help=u"""""")
@cli_util.option('--display-name', help=u"""A user-friendly and mutable name suitable for display in a user interface.""")
@cli_util.option('--interval-in-seconds', type=click.INT, help=u"""The monitor interval in seconds. Valid values: 10, 30, and 60.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Enables or disables the monitor. Set to 'true' to launch monitoring.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.  For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'targets': {'module': 'healthchecks', 'class': 'list[string]'}, 'vantage-point-names': {'module': 'healthchecks', 'class': 'list[string]'}, 'freeform-tags': {'module': 'healthchecks', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'healthchecks', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'healthchecks', 'class': 'PingMonitor'})
@cli_util.wrap_exceptions
def update_ping_monitor(ctx, from_json, force, monitor_id, targets, vantage_point_names, port, timeout_in_seconds, protocol, display_name, interval_in_seconds, is_enabled, freeform_tags, defined_tags, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')
    if not force:
        if targets or vantage_point_names or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to targets and vantage-point-names and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if targets is not None:
        _details['targets'] = cli_util.parse_json_parameter("targets", targets)

    if vantage_point_names is not None:
        _details['vantagePointNames'] = cli_util.parse_json_parameter("vantage_point_names", vantage_point_names)

    if port is not None:
        _details['port'] = port

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if protocol is not None:
        _details['protocol'] = protocol

    if display_name is not None:
        _details['displayName'] = display_name

    if interval_in_seconds is not None:
        _details['intervalInSeconds'] = interval_in_seconds

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('healthchecks', 'health_checks', ctx)
    result = client.update_ping_monitor(
        monitor_id=monitor_id,
        update_ping_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
