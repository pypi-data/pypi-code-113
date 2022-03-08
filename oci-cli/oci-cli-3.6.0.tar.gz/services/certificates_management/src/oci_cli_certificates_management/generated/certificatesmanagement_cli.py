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


@cli.command(cli_util.override('certs_mgmt.certs_mgmt_root_group.command_name', 'certs-mgmt'), cls=CommandGroupWithAlias, help=cli_util.override('certs_mgmt.certs_mgmt_root_group.help', """API for managing certificates."""), short_help=cli_util.override('certs_mgmt.certs_mgmt_root_group.short_help', """Certificates Service Management API"""))
@cli_util.help_option_group
def certs_mgmt_root_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_version_group.command_name', 'certificate-version'), cls=CommandGroupWithAlias, help="""The details of the certificate version. This object does not contain the certificate contents.""")
@cli_util.help_option_group
def certificate_version_group():
    pass


@click.command(cli_util.override('certs_mgmt.ca_bundle_summary_group.command_name', 'ca-bundle-summary'), cls=CommandGroupWithAlias, help="""CA bundle metadata. This summary object does not contain the CA bundle certificates.""")
@cli_util.help_option_group
def ca_bundle_summary_group():
    pass


@click.command(cli_util.override('certs_mgmt.association_summary_group.command_name', 'association-summary'), cls=CommandGroupWithAlias, help="""The details of the association.""")
@cli_util.help_option_group
def association_summary_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_authority_group.command_name', 'certificate-authority'), cls=CommandGroupWithAlias, help="""The metadata details of the certificate authority (CA). This object does not contain the CA contents.""")
@cli_util.help_option_group
def certificate_authority_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_group.command_name', 'certificate'), cls=CommandGroupWithAlias, help="""The details of the certificate. This object does not contain the certificate contents.""")
@cli_util.help_option_group
def certificate_group():
    pass


@click.command(cli_util.override('certs_mgmt.association_group.command_name', 'association'), cls=CommandGroupWithAlias, help="""The details of the association.""")
@cli_util.help_option_group
def association_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_authority_version_group.command_name', 'certificate-authority-version'), cls=CommandGroupWithAlias, help="""The metadata details of the certificate authority (CA) version. This object does not contain the CA contents.""")
@cli_util.help_option_group
def certificate_authority_version_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_version_summary_group.command_name', 'certificate-version-summary'), cls=CommandGroupWithAlias, help="""The details of the certificate version. This object does not contain the certificate contents.""")
@cli_util.help_option_group
def certificate_version_summary_group():
    pass


@click.command(cli_util.override('certs_mgmt.ca_bundle_group.command_name', 'ca-bundle'), cls=CommandGroupWithAlias, help="""CA bundle metadata. This object does not contain the CA bundle certificates.""")
@cli_util.help_option_group
def ca_bundle_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_authority_version_summary_group.command_name', 'certificate-authority-version-summary'), cls=CommandGroupWithAlias, help="""The metadata details of the certificate authority (CA) version. This summary object does not contain the CA contents.""")
@cli_util.help_option_group
def certificate_authority_version_summary_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_summary_group.command_name', 'certificate-summary'), cls=CommandGroupWithAlias, help="""The details of the certificate. This object does not contain the certificate contents.""")
@cli_util.help_option_group
def certificate_summary_group():
    pass


@click.command(cli_util.override('certs_mgmt.certificate_authority_summary_group.command_name', 'certificate-authority-summary'), cls=CommandGroupWithAlias, help="""The metadata details of the certificate authority (CA). This summary object does not contain the CA contents.""")
@cli_util.help_option_group
def certificate_authority_summary_group():
    pass


certs_mgmt_root_group.add_command(certificate_version_group)
certs_mgmt_root_group.add_command(ca_bundle_summary_group)
certs_mgmt_root_group.add_command(association_summary_group)
certs_mgmt_root_group.add_command(certificate_authority_group)
certs_mgmt_root_group.add_command(certificate_group)
certs_mgmt_root_group.add_command(association_group)
certs_mgmt_root_group.add_command(certificate_authority_version_group)
certs_mgmt_root_group.add_command(certificate_version_summary_group)
certs_mgmt_root_group.add_command(ca_bundle_group)
certs_mgmt_root_group.add_command(certificate_authority_version_summary_group)
certs_mgmt_root_group.add_command(certificate_summary_group)
certs_mgmt_root_group.add_command(certificate_authority_summary_group)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.cancel_certificate_authority_deletion.command_name', 'cancel-certificate-authority-deletion'), help=u"""Cancels the scheduled deletion of the specified certificate authority (CA). \n[Command Reference](cancelCertificateAuthorityDeletion)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_certificate_authority_deletion(ctx, from_json, certificate_authority_id, if_match):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.cancel_certificate_authority_deletion(
        certificate_authority_id=certificate_authority_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_version_group.command(name=cli_util.override('certs_mgmt.cancel_certificate_authority_version_deletion.command_name', 'cancel-certificate-authority-version-deletion'), help=u"""Cancels the scheduled deletion of the specified certificate authority (CA) version. Canceling a scheduled deletion restores the CA version's lifecycle state to what it was before its scheduled deletion. \n[Command Reference](cancelCertificateAuthorityVersionDeletion)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--certificate-authority-version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_certificate_authority_version_deletion(ctx, from_json, certificate_authority_id, certificate_authority_version_number, if_match):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    if isinstance(certificate_authority_version_number, six.string_types) and len(certificate_authority_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.cancel_certificate_authority_version_deletion(
        certificate_authority_id=certificate_authority_id,
        certificate_authority_version_number=certificate_authority_version_number,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.cancel_certificate_deletion.command_name', 'cancel-certificate-deletion'), help=u"""Cancels the pending deletion of the specified certificate. Canceling a scheduled deletion restores the certificate's lifecycle state to what it was before you scheduled the certificate for deletion. \n[Command Reference](cancelCertificateDeletion)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_certificate_deletion(ctx, from_json, certificate_id, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.cancel_certificate_deletion(
        certificate_id=certificate_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_version_group.command(name=cli_util.override('certs_mgmt.cancel_certificate_version_deletion.command_name', 'cancel-certificate-version-deletion'), help=u"""Cancels the scheduled deletion of the specified certificate version. \n[Command Reference](cancelCertificateVersionDeletion)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--certificate-version-number', required=True, type=click.INT, help=u"""The version number of the certificate.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_certificate_version_deletion(ctx, from_json, certificate_id, certificate_version_number, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    if isinstance(certificate_version_number, six.string_types) and len(certificate_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.cancel_certificate_version_deletion(
        certificate_id=certificate_id,
        certificate_version_number=certificate_version_number,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ca_bundle_group.command(name=cli_util.override('certs_mgmt.change_ca_bundle_compartment.command_name', 'change-compartment'), help=u"""Moves a CA bundle to a different compartment in the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When provided, if-match is checked against the ETag values of the secret. \n[Command Reference](changeCaBundleCompartment)""")
@cli_util.option('--ca-bundle-id', required=True, help=u"""The OCID of the CA bundle.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the CA bundle should move.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ca_bundle_compartment(ctx, from_json, ca_bundle_id, compartment_id, if_match):

    if isinstance(ca_bundle_id, six.string_types) and len(ca_bundle_id.strip()) == 0:
        raise click.UsageError('Parameter --ca-bundle-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.change_ca_bundle_compartment(
        ca_bundle_id=ca_bundle_id,
        change_ca_bundle_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.change_certificate_authority_compartment.command_name', 'change-compartment'), help=u"""Moves a certificate authority (CA) to a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When provided, If-Match is checked against the ETag values of the source. \n[Command Reference](changeCertificateAuthorityCompartment)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the CA should move.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_certificate_authority_compartment(ctx, from_json, certificate_authority_id, compartment_id, if_match):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.change_certificate_authority_compartment(
        certificate_authority_id=certificate_authority_id,
        change_certificate_authority_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.change_certificate_compartment.command_name', 'change-compartment'), help=u"""Moves a certificate to a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When provided, if-match is checked against the ETag values of the secret. \n[Command Reference](changeCertificateCompartment)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the certificate should move.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_certificate_compartment(ctx, from_json, certificate_id, compartment_id, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.change_certificate_compartment(
        certificate_id=certificate_id,
        change_certificate_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ca_bundle_group.command(name=cli_util.override('certs_mgmt.create_ca_bundle.command_name', 'create'), help=u"""Creates a new CA bundle according to the details of the request. \n[Command Reference](createCaBundle)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the CA bundle. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for the CA bundle.""")
@cli_util.option('--ca-bundle-pem', required=True, help=u"""Certificates (in PEM format) to include in the CA bundle.""")
@cli_util.option('--description', help=u"""A brief description of the CA bundle.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'certificates_management', 'class': 'CaBundle'})
@cli_util.wrap_exceptions
def create_ca_bundle(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, ca_bundle_pem, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['caBundlePem'] = ca_bundle_pem

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_ca_bundle(
        create_ca_bundle_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ca_bundle') and callable(getattr(client, 'get_ca_bundle')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ca_bundle(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.create_certificate.command_name', 'create'), help=u"""Creates a new certificate according to the details of the request. \n[Command Reference](createCertificate)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the certificate.""")
@cli_util.option('--certificate-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'certificate-config': {'module': 'certificates_management', 'class': 'CreateCertificateConfigDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'certificate-config': {'module': 'certificates_management', 'class': 'CreateCertificateConfigDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, certificate_config, description, certificate_rules, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['certificateConfig'] = cli_util.parse_json_parameter("certificate_config", certificate_config)

    if description is not None:
        _details['description'] = description

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_certificate(
        create_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details.command_name', 'create-certificate-create-certificate-managed-externally-issued-by-internal-ca-config-details'), help=u"""Creates a new certificate according to the details of the request. \n[Command Reference](createCertificate)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the certificate.""")
@cli_util.option('--certificate-config-issuer-certificate-authority-id', required=True, help=u"""The OCID of the private CA.""")
@cli_util.option('--certificate-config-csr-pem', required=True, help=u"""The certificate signing request (in PEM format).""")
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-config-version-name', help=u"""A name for the certificate. When the value is not null, a name is unique across versions of a given certificate.""")
@cli_util.option('--certificate-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, certificate_config_issuer_certificate_authority_id, certificate_config_csr_pem, description, certificate_rules, freeform_tags, defined_tags, certificate_config_version_name, certificate_config_validity):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateConfig'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['certificateConfig']['issuerCertificateAuthorityId'] = certificate_config_issuer_certificate_authority_id
    _details['certificateConfig']['csrPem'] = certificate_config_csr_pem

    if description is not None:
        _details['description'] = description

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_config_version_name is not None:
        _details['certificateConfig']['versionName'] = certificate_config_version_name

    if certificate_config_validity is not None:
        _details['certificateConfig']['validity'] = cli_util.parse_json_parameter("certificate_config_validity", certificate_config_validity)

    _details['certificateConfig']['configType'] = 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_certificate(
        create_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.create_certificate_create_certificate_issued_by_internal_ca_config_details.command_name', 'create-certificate-create-certificate-issued-by-internal-ca-config-details'), help=u"""Creates a new certificate according to the details of the request. \n[Command Reference](createCertificate)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the certificate.""")
@cli_util.option('--certificate-config-certificate-profile-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN"]), help=u"""The name of the profile used to create the certificate, which depends on the type of certificate you need.""")
@cli_util.option('--certificate-config-issuer-certificate-authority-id', required=True, help=u"""The OCID of the private CA.""")
@cli_util.option('--certificate-config-subject', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-config-version-name', help=u"""A name for the certificate. When the value is not null, a name is unique across versions of a given certificate.""")
@cli_util.option('--certificate-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-config-subject-alternative-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of subject alternative names.

This option is a JSON list with items of type CertificateSubjectAlternativeName.  For documentation on CertificateSubjectAlternativeName please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateSubjectAlternativeName.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-config-key-algorithm', type=custom_types.CliCaseInsensitiveChoice(["RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"]), help=u"""The algorithm to use to create key pairs.""")
@cli_util.option('--certificate-config-signature-algorithm', type=custom_types.CliCaseInsensitiveChoice(["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]), help=u"""The algorithm to use to sign the public key certificate.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}, 'certificate-config-subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}, 'certificate-config-subject-alternative-names': {'module': 'certificates_management', 'class': 'list[CertificateSubjectAlternativeName]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}, 'certificate-config-subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}, 'certificate-config-subject-alternative-names': {'module': 'certificates_management', 'class': 'list[CertificateSubjectAlternativeName]'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate_create_certificate_issued_by_internal_ca_config_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, certificate_config_certificate_profile_type, certificate_config_issuer_certificate_authority_id, certificate_config_subject, description, certificate_rules, freeform_tags, defined_tags, certificate_config_version_name, certificate_config_validity, certificate_config_subject_alternative_names, certificate_config_key_algorithm, certificate_config_signature_algorithm):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateConfig'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['certificateConfig']['certificateProfileType'] = certificate_config_certificate_profile_type
    _details['certificateConfig']['issuerCertificateAuthorityId'] = certificate_config_issuer_certificate_authority_id
    _details['certificateConfig']['subject'] = cli_util.parse_json_parameter("certificate_config_subject", certificate_config_subject)

    if description is not None:
        _details['description'] = description

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_config_version_name is not None:
        _details['certificateConfig']['versionName'] = certificate_config_version_name

    if certificate_config_validity is not None:
        _details['certificateConfig']['validity'] = cli_util.parse_json_parameter("certificate_config_validity", certificate_config_validity)

    if certificate_config_subject_alternative_names is not None:
        _details['certificateConfig']['subjectAlternativeNames'] = cli_util.parse_json_parameter("certificate_config_subject_alternative_names", certificate_config_subject_alternative_names)

    if certificate_config_key_algorithm is not None:
        _details['certificateConfig']['keyAlgorithm'] = certificate_config_key_algorithm

    if certificate_config_signature_algorithm is not None:
        _details['certificateConfig']['signatureAlgorithm'] = certificate_config_signature_algorithm

    _details['certificateConfig']['configType'] = 'ISSUED_BY_INTERNAL_CA'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_certificate(
        create_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.create_certificate_create_certificate_by_importing_config_details.command_name', 'create-certificate-create-certificate-by-importing-config-details'), help=u"""Creates a new certificate according to the details of the request. \n[Command Reference](createCertificate)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the certificate.""")
@cli_util.option('--certificate-config-cert-chain-pem', required=True, help=u"""The certificate chain (in PEM format) for the imported certificate.""")
@cli_util.option('--certificate-config-private-key-pem', required=True, help=u"""The private key (in PEM format) for the imported certificate.""")
@cli_util.option('--certificate-config-certificate-pem', required=True, help=u"""The certificate (in PEM format) for the imported certificate.""")
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-config-version-name', help=u"""A name for the certificate. When the value is not null, a name is unique across versions of a given certificate.""")
@cli_util.option('--certificate-config-private-key-pem-passphrase', help=u"""An optional passphrase for the private key.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate_create_certificate_by_importing_config_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, certificate_config_cert_chain_pem, certificate_config_private_key_pem, certificate_config_certificate_pem, description, certificate_rules, freeform_tags, defined_tags, certificate_config_version_name, certificate_config_private_key_pem_passphrase):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateConfig'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['certificateConfig']['certChainPem'] = certificate_config_cert_chain_pem
    _details['certificateConfig']['privateKeyPem'] = certificate_config_private_key_pem
    _details['certificateConfig']['certificatePem'] = certificate_config_certificate_pem

    if description is not None:
        _details['description'] = description

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_config_version_name is not None:
        _details['certificateConfig']['versionName'] = certificate_config_version_name

    if certificate_config_private_key_pem_passphrase is not None:
        _details['certificateConfig']['privateKeyPemPassphrase'] = certificate_config_private_key_pem_passphrase

    _details['certificateConfig']['configType'] = 'IMPORTED'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_certificate(
        create_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.create_certificate_authority.command_name', 'create'), help=u"""Creates a new certificate authority (CA) according to the details of the request. \n[Command Reference](createCertificateAuthority)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment in which you want to create the CA.""")
@cli_util.option('--certificate-authority-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', required=True, help=u"""The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.""")
@cli_util.option('--description', help=u"""A brief description of the CA.""")
@cli_util.option('--certificate-authority-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules that control how the CA is used and managed.

This option is a JSON list with items of type CertificateAuthorityRule.  For documentation on CertificateAuthorityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateAuthorityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-revocation-list-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-authority-config': {'module': 'certificates_management', 'class': 'CreateCertificateAuthorityConfigDetails'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-authority-config': {'module': 'certificates_management', 'class': 'CreateCertificateAuthorityConfigDetails'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def create_certificate_authority(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, certificate_authority_config, kms_key_id, description, certificate_authority_rules, certificate_revocation_list_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['certificateAuthorityConfig'] = cli_util.parse_json_parameter("certificate_authority_config", certificate_authority_config)
    _details['kmsKeyId'] = kms_key_id

    if description is not None:
        _details['description'] = description

    if certificate_authority_rules is not None:
        _details['certificateAuthorityRules'] = cli_util.parse_json_parameter("certificate_authority_rules", certificate_authority_rules)

    if certificate_revocation_list_details is not None:
        _details['certificateRevocationListDetails'] = cli_util.parse_json_parameter("certificate_revocation_list_details", certificate_revocation_list_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_certificate_authority(
        create_certificate_authority_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate_authority') and callable(getattr(client, 'get_certificate_authority')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate_authority(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.create_certificate_authority_create_root_ca_by_generating_internally_config_details.command_name', 'create-certificate-authority-create-root-ca-by-generating-internally-config-details'), help=u"""Creates a new certificate authority (CA) according to the details of the request. \n[Command Reference](createCertificateAuthority)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment in which you want to create the CA.""")
@cli_util.option('--kms-key-id', required=True, help=u"""The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.""")
@cli_util.option('--certificate-authority-config-subject', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the CA.""")
@cli_util.option('--certificate-authority-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules that control how the CA is used and managed.

This option is a JSON list with items of type CertificateAuthorityRule.  For documentation on CertificateAuthorityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateAuthorityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-revocation-list-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-authority-config-version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@cli_util.option('--certificate-authority-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-authority-config-signing-algorithm', type=custom_types.CliCaseInsensitiveChoice(["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]), help=u"""The algorithm used to sign public key certificates that the CA issues.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}, 'certificate-authority-config-subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}, 'certificate-authority-config-subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def create_certificate_authority_create_root_ca_by_generating_internally_config_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, kms_key_id, certificate_authority_config_subject, description, certificate_authority_rules, certificate_revocation_list_details, freeform_tags, defined_tags, certificate_authority_config_version_name, certificate_authority_config_validity, certificate_authority_config_signing_algorithm):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateAuthorityConfig'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['kmsKeyId'] = kms_key_id
    _details['certificateAuthorityConfig']['subject'] = cli_util.parse_json_parameter("certificate_authority_config_subject", certificate_authority_config_subject)

    if description is not None:
        _details['description'] = description

    if certificate_authority_rules is not None:
        _details['certificateAuthorityRules'] = cli_util.parse_json_parameter("certificate_authority_rules", certificate_authority_rules)

    if certificate_revocation_list_details is not None:
        _details['certificateRevocationListDetails'] = cli_util.parse_json_parameter("certificate_revocation_list_details", certificate_revocation_list_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_authority_config_version_name is not None:
        _details['certificateAuthorityConfig']['versionName'] = certificate_authority_config_version_name

    if certificate_authority_config_validity is not None:
        _details['certificateAuthorityConfig']['validity'] = cli_util.parse_json_parameter("certificate_authority_config_validity", certificate_authority_config_validity)

    if certificate_authority_config_signing_algorithm is not None:
        _details['certificateAuthorityConfig']['signingAlgorithm'] = certificate_authority_config_signing_algorithm

    _details['certificateAuthorityConfig']['configType'] = 'ROOT_CA_GENERATED_INTERNALLY'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_certificate_authority(
        create_certificate_authority_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate_authority') and callable(getattr(client, 'get_certificate_authority')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate_authority(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details.command_name', 'create-certificate-authority-create-subordinate-ca-issued-by-internal-ca-config-details'), help=u"""Creates a new certificate authority (CA) according to the details of the request. \n[Command Reference](createCertificateAuthority)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment in which you want to create the CA.""")
@cli_util.option('--kms-key-id', required=True, help=u"""The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.""")
@cli_util.option('--certificate-authority-config-issuer-certificate-authority-id', required=True, help=u"""The OCID of the private CA.""")
@cli_util.option('--certificate-authority-config-subject', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the CA.""")
@cli_util.option('--certificate-authority-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules that control how the CA is used and managed.

This option is a JSON list with items of type CertificateAuthorityRule.  For documentation on CertificateAuthorityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateAuthorityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-revocation-list-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-authority-config-version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@cli_util.option('--certificate-authority-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-authority-config-signing-algorithm', type=custom_types.CliCaseInsensitiveChoice(["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]), help=u"""The algorithm used to sign public key certificates that the CA issues.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}, 'certificate-authority-config-subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}, 'certificate-authority-config-subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, kms_key_id, certificate_authority_config_issuer_certificate_authority_id, certificate_authority_config_subject, description, certificate_authority_rules, certificate_revocation_list_details, freeform_tags, defined_tags, certificate_authority_config_version_name, certificate_authority_config_validity, certificate_authority_config_signing_algorithm):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateAuthorityConfig'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['kmsKeyId'] = kms_key_id
    _details['certificateAuthorityConfig']['issuerCertificateAuthorityId'] = certificate_authority_config_issuer_certificate_authority_id
    _details['certificateAuthorityConfig']['subject'] = cli_util.parse_json_parameter("certificate_authority_config_subject", certificate_authority_config_subject)

    if description is not None:
        _details['description'] = description

    if certificate_authority_rules is not None:
        _details['certificateAuthorityRules'] = cli_util.parse_json_parameter("certificate_authority_rules", certificate_authority_rules)

    if certificate_revocation_list_details is not None:
        _details['certificateRevocationListDetails'] = cli_util.parse_json_parameter("certificate_revocation_list_details", certificate_revocation_list_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_authority_config_version_name is not None:
        _details['certificateAuthorityConfig']['versionName'] = certificate_authority_config_version_name

    if certificate_authority_config_validity is not None:
        _details['certificateAuthorityConfig']['validity'] = cli_util.parse_json_parameter("certificate_authority_config_validity", certificate_authority_config_validity)

    if certificate_authority_config_signing_algorithm is not None:
        _details['certificateAuthorityConfig']['signingAlgorithm'] = certificate_authority_config_signing_algorithm

    _details['certificateAuthorityConfig']['configType'] = 'SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.create_certificate_authority(
        create_certificate_authority_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate_authority') and callable(getattr(client, 'get_certificate_authority')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate_authority(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ca_bundle_group.command(name=cli_util.override('certs_mgmt.delete_ca_bundle.command_name', 'delete'), help=u"""Deletes the specified CA bundle. \n[Command Reference](deleteCaBundle)""")
@cli_util.option('--ca-bundle-id', required=True, help=u"""The OCID of the CA bundle.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ca_bundle(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ca_bundle_id, if_match):

    if isinstance(ca_bundle_id, six.string_types) and len(ca_bundle_id.strip()) == 0:
        raise click.UsageError('Parameter --ca-bundle-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.delete_ca_bundle(
        ca_bundle_id=ca_bundle_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ca_bundle') and callable(getattr(client, 'get_ca_bundle')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_ca_bundle(ca_bundle_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@association_group.command(name=cli_util.override('certs_mgmt.get_association.command_name', 'get'), help=u"""Gets details about the specified association. \n[Command Reference](getAssociation)""")
@cli_util.option('--association-id', required=True, help=u"""The OCID of an association between a certificate-related resource and another Oracle Cloud Infrastructure resource.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'Association'})
@cli_util.wrap_exceptions
def get_association(ctx, from_json, association_id):

    if isinstance(association_id, six.string_types) and len(association_id.strip()) == 0:
        raise click.UsageError('Parameter --association-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.get_association(
        association_id=association_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ca_bundle_group.command(name=cli_util.override('certs_mgmt.get_ca_bundle.command_name', 'get'), help=u"""Gets details about the specified CA bundle. \n[Command Reference](getCaBundle)""")
@cli_util.option('--ca-bundle-id', required=True, help=u"""The OCID of the CA bundle.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CaBundle'})
@cli_util.wrap_exceptions
def get_ca_bundle(ctx, from_json, ca_bundle_id):

    if isinstance(ca_bundle_id, six.string_types) and len(ca_bundle_id.strip()) == 0:
        raise click.UsageError('Parameter --ca-bundle-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.get_ca_bundle(
        ca_bundle_id=ca_bundle_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.get_certificate.command_name', 'get'), help=u"""Gets details about the specified certificate. \n[Command Reference](getCertificate)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def get_certificate(ctx, from_json, certificate_id):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.get_certificate(
        certificate_id=certificate_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.get_certificate_authority.command_name', 'get'), help=u"""Gets details about the specified certificate authority (CA). \n[Command Reference](getCertificateAuthority)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def get_certificate_authority(ctx, from_json, certificate_authority_id):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.get_certificate_authority(
        certificate_authority_id=certificate_authority_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_version_group.command(name=cli_util.override('certs_mgmt.get_certificate_authority_version.command_name', 'get'), help=u"""Gets details about the specified certificate authority (CA) version. \n[Command Reference](getCertificateAuthorityVersion)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--certificate-authority-version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthorityVersion'})
@cli_util.wrap_exceptions
def get_certificate_authority_version(ctx, from_json, certificate_authority_id, certificate_authority_version_number):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    if isinstance(certificate_authority_version_number, six.string_types) and len(certificate_authority_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-version-number cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.get_certificate_authority_version(
        certificate_authority_id=certificate_authority_id,
        certificate_authority_version_number=certificate_authority_version_number,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_version_group.command(name=cli_util.override('certs_mgmt.get_certificate_version.command_name', 'get'), help=u"""Gets details about the specified version of a certificate. \n[Command Reference](getCertificateVersion)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--certificate-version-number', required=True, type=click.INT, help=u"""The version number of the certificate.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateVersion'})
@cli_util.wrap_exceptions
def get_certificate_version(ctx, from_json, certificate_id, certificate_version_number):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    if isinstance(certificate_version_number, six.string_types) and len(certificate_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-version-number cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.get_certificate_version(
        certificate_id=certificate_id,
        certificate_version_number=certificate_version_number,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@association_summary_group.command(name=cli_util.override('certs_mgmt.list_associations.command_name', 'list-associations'), help=u"""Lists all associations that match the query parameters. Optionally, you can use the parameter `FilterByAssociationIdQueryParam` to limit the result set to a single item that matches the specified association. \n[Command Reference](listAssociations)""")
@cli_util.option('--compartment-id', help=u"""A filter that returns only resources that match the given compartment OCID.""")
@cli_util.option('--certificates-resource-id', help=u"""A filter that returns only resources that match the given OCID of a certificate-related resource.""")
@cli_util.option('--associated-resource-id', help=u"""A filter that returns only resources that match the given OCID of an associated Oracle Cloud Infrastructure resource.""")
@cli_util.option('--association-id', help=u"""The OCID of the association. If the parameter is set to null, the service lists all associations.""")
@cli_util.option('--name', help=u"""A filter that returns only resources that match the specified name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending. The default order for `NAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--association-type', type=custom_types.CliCaseInsensitiveChoice(["CERTIFICATE", "CERTIFICATE_AUTHORITY", "CA_BUNDLE"]), help=u"""Type of associations to list. If the parameter is set to null, the service lists all types of associations.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'AssociationCollection'})
@cli_util.wrap_exceptions
def list_associations(ctx, from_json, all_pages, page_size, compartment_id, certificates_resource_id, associated_resource_id, association_id, name, sort_by, sort_order, limit, page, association_type):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if certificates_resource_id is not None:
        kwargs['certificates_resource_id'] = certificates_resource_id
    if associated_resource_id is not None:
        kwargs['associated_resource_id'] = associated_resource_id
    if association_id is not None:
        kwargs['association_id'] = association_id
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if association_type is not None:
        kwargs['association_type'] = association_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_associations,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_associations,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_associations(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ca_bundle_summary_group.command(name=cli_util.override('certs_mgmt.list_ca_bundles.command_name', 'list-ca-bundles'), help=u"""Lists all CA bundles that match the query parameters. Optionally, you can use the parameter `FilterByCaBundleIdQueryParam` to limit the result set to a single item that matches the specified CA bundle. \n[Command Reference](listCaBundles)""")
@cli_util.option('--compartment-id', help=u"""A filter that returns only resources that match the given compartment OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns only resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--name', help=u"""A filter that returns only resources that match the specified name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending. The default order for `NAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--ca-bundle-id', help=u"""The OCID of the CA bundle.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CaBundleCollection'})
@cli_util.wrap_exceptions
def list_ca_bundles(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, name, sort_by, sort_order, limit, page, ca_bundle_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if ca_bundle_id is not None:
        kwargs['ca_bundle_id'] = ca_bundle_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ca_bundles,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ca_bundles,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_ca_bundles(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@certificate_authority_summary_group.command(name=cli_util.override('certs_mgmt.list_certificate_authorities.command_name', 'list-certificate-authorities'), help=u"""Lists all certificate authorities (CAs) in the specified compartment. Optionally, you can use the parameter `FilterByCertificateAuthorityIdQueryParam` to limit the results to a single item that matches the specified CA. \n[Command Reference](listCertificateAuthorities)""")
@cli_util.option('--compartment-id', help=u"""A filter that returns only resources that match the given compartment OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), help=u"""A filter that returns only resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--name', help=u"""A filter that returns only resources that match the specified name.""")
@cli_util.option('--issuer-certificate-authority-id', help=u"""The OCID of the certificate authority (CA). If the parameter is set to null, the service lists all CAs.""")
@cli_util.option('--certificate-authority-id', help=u"""The OCID of the certificate authority (CA). If the parameter is set to null, the service lists all CAs.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "EXPIRATIONDATE", "TIMECREATED"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `EXPIRATIONDATE` and 'TIMECREATED' is descending. The default order for `NAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthorityCollection'})
@cli_util.wrap_exceptions
def list_certificate_authorities(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, name, issuer_certificate_authority_id, certificate_authority_id, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if name is not None:
        kwargs['name'] = name
    if issuer_certificate_authority_id is not None:
        kwargs['issuer_certificate_authority_id'] = issuer_certificate_authority_id
    if certificate_authority_id is not None:
        kwargs['certificate_authority_id'] = certificate_authority_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_certificate_authorities,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_certificate_authorities,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_certificate_authorities(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@certificate_authority_version_summary_group.command(name=cli_util.override('certs_mgmt.list_certificate_authority_versions.command_name', 'list-certificate-authority-versions'), help=u"""Lists all versions for the specified certificate authority (CA). Optionally, you can use the parameter `FilterByVersionNumberQueryParam` to limit the results to a single item that matches the specified version number. \n[Command Reference](listCertificateAuthorityVersions)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--version-number', type=click.INT, help=u"""A filter that returns only resources that match the specified version number. The default value is 0, which means that this filter is not applied.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["VERSION_NUMBER"]), help=u"""The field to sort by. You can specify only one sort order. The default order for 'VERSION_NUMBER' is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthorityVersionCollection'})
@cli_util.wrap_exceptions
def list_certificate_authority_versions(ctx, from_json, all_pages, page_size, certificate_authority_id, version_number, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    kwargs = {}
    if version_number is not None:
        kwargs['version_number'] = version_number
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_certificate_authority_versions,
            certificate_authority_id=certificate_authority_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_certificate_authority_versions,
            limit,
            page_size,
            certificate_authority_id=certificate_authority_id,
            **kwargs
        )
    else:
        result = client.list_certificate_authority_versions(
            certificate_authority_id=certificate_authority_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@certificate_version_summary_group.command(name=cli_util.override('certs_mgmt.list_certificate_versions.command_name', 'list-certificate-versions'), help=u"""Lists all certificate versions for the specified certificate. Optionally, you can use the parameter `FilterByVersionNumberQueryParam` to limit the result set to a single item that matches the specified version number. \n[Command Reference](listCertificateVersions)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--version-number', type=click.INT, help=u"""A filter that returns only resources that match the specified version number. The default value is 0, which means that this filter is not applied.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["VERSION_NUMBER"]), help=u"""The field to sort by. You can specify only one sort order. The default order for 'VERSION_NUMBER' is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateVersionCollection'})
@cli_util.wrap_exceptions
def list_certificate_versions(ctx, from_json, all_pages, page_size, certificate_id, version_number, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if version_number is not None:
        kwargs['version_number'] = version_number
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_certificate_versions,
            certificate_id=certificate_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_certificate_versions,
            limit,
            page_size,
            certificate_id=certificate_id,
            **kwargs
        )
    else:
        result = client.list_certificate_versions(
            certificate_id=certificate_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@certificate_summary_group.command(name=cli_util.override('certs_mgmt.list_certificates.command_name', 'list-certificates'), help=u"""Lists all certificates that match the query parameters. Optionally, you can use the parameter `FilterByCertificateIdQueryParam` to limit the result set to a single item that matches the specified certificate. \n[Command Reference](listCertificates)""")
@cli_util.option('--compartment-id', help=u"""A filter that returns only resources that match the given compartment OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), help=u"""A filter that returns only resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--name', help=u"""A filter that returns only resources that match the specified name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "EXPIRATIONDATE", "TIMECREATED"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `EXPIRATIONDATE` and 'TIMECREATED' is descending. The default order for `NAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--issuer-certificate-authority-id', help=u"""The OCID of the certificate authority (CA). If the parameter is set to null, the service lists all CAs.""")
@cli_util.option('--certificate-id', help=u"""The OCID of the certificate. If the parameter is set to null, the service lists all certificates.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateCollection'})
@cli_util.wrap_exceptions
def list_certificates(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, name, sort_by, sort_order, limit, page, issuer_certificate_authority_id, certificate_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if issuer_certificate_authority_id is not None:
        kwargs['issuer_certificate_authority_id'] = issuer_certificate_authority_id
    if certificate_id is not None:
        kwargs['certificate_id'] = certificate_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_certificates,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_certificates,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_certificates(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@certificate_authority_version_group.command(name=cli_util.override('certs_mgmt.revoke_certificate_authority_version.command_name', 'revoke'), help=u"""Revokes a certificate authority (CA) version. \n[Command Reference](revokeCertificateAuthorityVersion)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--certificate-authority-version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA).""")
@cli_util.option('--revocation-reason', type=custom_types.CliCaseInsensitiveChoice(["UNSPECIFIED", "KEY_COMPROMISE", "CA_COMPROMISE", "AFFILIATION_CHANGED", "SUPERSEDED", "CESSATION_OF_OPERATION", "PRIVILEGE_WITHDRAWN", "AA_COMPROMISE"]), help=u"""The reason the certificate or certificate authority was revoked.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def revoke_certificate_authority_version(ctx, from_json, certificate_authority_id, certificate_authority_version_number, revocation_reason, if_match):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    if isinstance(certificate_authority_version_number, six.string_types) and len(certificate_authority_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if revocation_reason is not None:
        _details['revocationReason'] = revocation_reason

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.revoke_certificate_authority_version(
        certificate_authority_id=certificate_authority_id,
        certificate_authority_version_number=certificate_authority_version_number,
        revoke_certificate_authority_version_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_version_group.command(name=cli_util.override('certs_mgmt.revoke_certificate_version.command_name', 'revoke'), help=u"""Revokes the specified certificate version. \n[Command Reference](revokeCertificateVersion)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--certificate-version-number', required=True, type=click.INT, help=u"""The version number of the certificate.""")
@cli_util.option('--revocation-reason', type=custom_types.CliCaseInsensitiveChoice(["UNSPECIFIED", "KEY_COMPROMISE", "CA_COMPROMISE", "AFFILIATION_CHANGED", "SUPERSEDED", "CESSATION_OF_OPERATION", "PRIVILEGE_WITHDRAWN", "AA_COMPROMISE"]), help=u"""The reason that the certificate or certificate authority was revoked.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def revoke_certificate_version(ctx, from_json, certificate_id, certificate_version_number, revocation_reason, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    if isinstance(certificate_version_number, six.string_types) and len(certificate_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if revocation_reason is not None:
        _details['revocationReason'] = revocation_reason

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.revoke_certificate_version(
        certificate_id=certificate_id,
        certificate_version_number=certificate_version_number,
        revoke_certificate_version_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.schedule_certificate_authority_deletion.command_name', 'schedule-certificate-authority-deletion'), help=u"""Schedules the deletion of the specified certificate authority (CA). This sets the lifecycle state of the CA to `PENDING_DELETION` and then deletes it after the specified retention period ends. If needed, you can determine the status of the deletion by using `GetCertificateAuthority`. \n[Command Reference](scheduleCertificateAuthorityDeletion)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property indicating when to delete the CA, expressed in [RFC 3339] timestamp format. Example: `2019-04-03T21:10:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_certificate_authority_deletion(ctx, from_json, certificate_authority_id, time_of_deletion, if_match):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.schedule_certificate_authority_deletion(
        certificate_authority_id=certificate_authority_id,
        schedule_certificate_authority_deletion_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_version_group.command(name=cli_util.override('certs_mgmt.schedule_certificate_authority_version_deletion.command_name', 'schedule-certificate-authority-version-deletion'), help=u"""Schedules the deletion of the specified certificate authority (CA) version. This sets the lifecycle state of the CA version to `PENDING_DELETION` and then deletes it after the specified retention period ends. If needed, you can determine the status of the deletion by using `GetCertificateAuthorityVersion`. \n[Command Reference](scheduleCertificateAuthorityVersionDeletion)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--certificate-authority-version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA).""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property indicating when to delete the CA version, expressed in [RFC 3339] timestamp format. Example: `2019-04-03T21:10:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_certificate_authority_version_deletion(ctx, from_json, certificate_authority_id, certificate_authority_version_number, time_of_deletion, if_match):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    if isinstance(certificate_authority_version_number, six.string_types) and len(certificate_authority_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.schedule_certificate_authority_version_deletion(
        certificate_authority_id=certificate_authority_id,
        certificate_authority_version_number=certificate_authority_version_number,
        schedule_certificate_authority_version_deletion_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.schedule_certificate_deletion.command_name', 'schedule-certificate-deletion'), help=u"""Schedules the deletion of the specified certificate. This sets the lifecycle state of the certificate to `PENDING_DELETION` and then deletes it after the specified retention period ends. You can subsequently use `GetCertificate` to determine the current deletion status. \n[Command Reference](scheduleCertificateDeletion)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property indicating when to delete the certificate version, expressed in [RFC 3339] timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_certificate_deletion(ctx, from_json, certificate_id, time_of_deletion, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.schedule_certificate_deletion(
        certificate_id=certificate_id,
        schedule_certificate_deletion_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_version_group.command(name=cli_util.override('certs_mgmt.schedule_certificate_version_deletion.command_name', 'schedule-certificate-version-deletion'), help=u"""Schedules the deletion of the specified certificate version. This sets the lifecycle state of the certificate version to `PENDING_DELETION` and then deletes it after the specified retention period ends. You can only delete a certificate version if the certificate version rotation state is marked as `DEPRECATED`.

You can subsequently use `GetCertificateVersion` to determine the current certificate version deletion status. \n[Command Reference](scheduleCertificateVersionDeletion)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--certificate-version-number', required=True, type=click.INT, help=u"""The version number of the certificate.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property that indicates when to delete the certificate version, expressed in [RFC 3339] timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_certificate_version_deletion(ctx, from_json, certificate_id, certificate_version_number, time_of_deletion, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    if isinstance(certificate_version_number, six.string_types) and len(certificate_version_number.strip()) == 0:
        raise click.UsageError('Parameter --certificate-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.schedule_certificate_version_deletion(
        certificate_id=certificate_id,
        certificate_version_number=certificate_version_number,
        schedule_certificate_version_deletion_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ca_bundle_group.command(name=cli_util.override('certs_mgmt.update_ca_bundle.command_name', 'update'), help=u"""Updates the properties of a CA bundle. \n[Command Reference](updateCaBundle)""")
@cli_util.option('--ca-bundle-id', required=True, help=u"""The OCID of the CA bundle.""")
@cli_util.option('--description', help=u"""A brief description of the CA bundle.""")
@cli_util.option('--ca-bundle-pem', help=u"""Certificates (in PEM format) to include in the CA bundle.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'certificates_management', 'class': 'CaBundle'})
@cli_util.wrap_exceptions
def update_ca_bundle(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ca_bundle_id, description, ca_bundle_pem, freeform_tags, defined_tags, if_match):

    if isinstance(ca_bundle_id, six.string_types) and len(ca_bundle_id.strip()) == 0:
        raise click.UsageError('Parameter --ca-bundle-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if ca_bundle_pem is not None:
        _details['caBundlePem'] = ca_bundle_pem

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_ca_bundle(
        ca_bundle_id=ca_bundle_id,
        update_ca_bundle_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ca_bundle') and callable(getattr(client, 'get_ca_bundle')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ca_bundle(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.update_certificate.command_name', 'update'), help=u"""Updates the properties of a certificate. \n[Command Reference](updateCertificate)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Makes this version the current version. This property cannot be updated in combination with any other properties.""")
@cli_util.option('--certificate-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-config': {'module': 'certificates_management', 'class': 'UpdateCertificateConfigDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-config': {'module': 'certificates_management', 'class': 'UpdateCertificateConfigDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_id, description, current_version_number, certificate_config, freeform_tags, defined_tags, certificate_rules, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')
    if not force:
        if certificate_config or freeform_tags or defined_tags or certificate_rules:
            if not click.confirm("WARNING: Updates to certificate-config and freeform-tags and defined-tags and certificate-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if certificate_config is not None:
        _details['certificateConfig'] = cli_util.parse_json_parameter("certificate_config", certificate_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_certificate(
        certificate_id=certificate_id,
        update_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.update_certificate_update_certificate_by_importing_config_details.command_name', 'update-certificate-update-certificate-by-importing-config-details'), help=u"""Updates the properties of a certificate. \n[Command Reference](updateCertificate)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--certificate-config-cert-chain-pem', required=True, help=u"""The certificate chain (in PEM format) for the imported certificate.""")
@cli_util.option('--certificate-config-private-key-pem', required=True, help=u"""The private key (in PEM format) for the imported certificate.""")
@cli_util.option('--certificate-config-certificate-pem', required=True, help=u"""The certificate (in PEM format) for the imported certificate.""")
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Makes this version the current version. This property cannot be updated in combination with any other properties.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--certificate-config-version-name', help=u"""A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.""")
@cli_util.option('--certificate-config-stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--certificate-config-private-key-pem-passphrase', help=u"""An optional passphrase for the private key.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate_update_certificate_by_importing_config_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_id, certificate_config_cert_chain_pem, certificate_config_private_key_pem, certificate_config_certificate_pem, description, current_version_number, freeform_tags, defined_tags, certificate_rules, if_match, certificate_config_version_name, certificate_config_stage, certificate_config_private_key_pem_passphrase):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or certificate_rules:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and certificate-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateConfig'] = {}
    _details['certificateConfig']['certChainPem'] = certificate_config_cert_chain_pem
    _details['certificateConfig']['privateKeyPem'] = certificate_config_private_key_pem
    _details['certificateConfig']['certificatePem'] = certificate_config_certificate_pem

    if description is not None:
        _details['description'] = description

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    if certificate_config_version_name is not None:
        _details['certificateConfig']['versionName'] = certificate_config_version_name

    if certificate_config_stage is not None:
        _details['certificateConfig']['stage'] = certificate_config_stage

    if certificate_config_private_key_pem_passphrase is not None:
        _details['certificateConfig']['privateKeyPemPassphrase'] = certificate_config_private_key_pem_passphrase

    _details['certificateConfig']['configType'] = 'IMPORTED'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_certificate(
        certificate_id=certificate_id,
        update_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.update_certificate_update_certificate_issued_by_internal_ca_config_details.command_name', 'update-certificate-update-certificate-issued-by-internal-ca-config-details'), help=u"""Updates the properties of a certificate. \n[Command Reference](updateCertificate)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Makes this version the current version. This property cannot be updated in combination with any other properties.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--certificate-config-version-name', help=u"""A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.""")
@cli_util.option('--certificate-config-stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--certificate-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate_update_certificate_issued_by_internal_ca_config_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_id, description, current_version_number, freeform_tags, defined_tags, certificate_rules, if_match, certificate_config_version_name, certificate_config_stage, certificate_config_validity):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or certificate_rules:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and certificate-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateConfig'] = {}

    if description is not None:
        _details['description'] = description

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    if certificate_config_version_name is not None:
        _details['certificateConfig']['versionName'] = certificate_config_version_name

    if certificate_config_stage is not None:
        _details['certificateConfig']['stage'] = certificate_config_stage

    if certificate_config_validity is not None:
        _details['certificateConfig']['validity'] = cli_util.parse_json_parameter("certificate_config_validity", certificate_config_validity)

    _details['certificateConfig']['configType'] = 'ISSUED_BY_INTERNAL_CA'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_certificate(
        certificate_id=certificate_id,
        update_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('certs_mgmt.update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details.command_name', 'update-certificate-update-certificate-managed-externally-issued-by-internal-ca-config-details'), help=u"""Updates the properties of a certificate. \n[Command Reference](updateCertificate)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--certificate-config-csr-pem', required=True, help=u"""The certificate signing request (in PEM format).""")
@cli_util.option('--description', help=u"""A brief description of the certificate. Avoid entering confidential information.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Makes this version the current version. This property cannot be updated in combination with any other properties.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An optional list of rules that control how the certificate is used and managed.

This option is a JSON list with items of type CertificateRule.  For documentation on CertificateRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--certificate-config-version-name', help=u"""A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.""")
@cli_util.option('--certificate-config-stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--certificate-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'certificate-config-validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_id, certificate_config_csr_pem, description, current_version_number, freeform_tags, defined_tags, certificate_rules, if_match, certificate_config_version_name, certificate_config_stage, certificate_config_validity):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or certificate_rules:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and certificate-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateConfig'] = {}
    _details['certificateConfig']['csrPem'] = certificate_config_csr_pem

    if description is not None:
        _details['description'] = description

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_rules is not None:
        _details['certificateRules'] = cli_util.parse_json_parameter("certificate_rules", certificate_rules)

    if certificate_config_version_name is not None:
        _details['certificateConfig']['versionName'] = certificate_config_version_name

    if certificate_config_stage is not None:
        _details['certificateConfig']['stage'] = certificate_config_stage

    if certificate_config_validity is not None:
        _details['certificateConfig']['validity'] = cli_util.parse_json_parameter("certificate_config_validity", certificate_config_validity)

    _details['certificateConfig']['configType'] = 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_certificate(
        certificate_id=certificate_id,
        update_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.update_certificate_authority.command_name', 'update'), help=u"""Updates the properties of the specified certificate authority (CA). \n[Command Reference](updateCertificateAuthority)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--description', help=u"""A brief description of the CA.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Makes this version the current version. This property cannot be updated in combination with any other properties.""")
@cli_util.option('--certificate-authority-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-revocation-list-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-authority-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules that control how the CA is used and managed.

This option is a JSON list with items of type CertificateAuthorityRule.  For documentation on CertificateAuthorityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateAuthorityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-authority-config': {'module': 'certificates_management', 'class': 'UpdateCertificateAuthorityConfigDetails'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-authority-config': {'module': 'certificates_management', 'class': 'UpdateCertificateAuthorityConfigDetails'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def update_certificate_authority(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_authority_id, description, current_version_number, certificate_authority_config, certificate_revocation_list_details, freeform_tags, defined_tags, certificate_authority_rules, if_match):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')
    if not force:
        if certificate_authority_config or certificate_revocation_list_details or freeform_tags or defined_tags or certificate_authority_rules:
            if not click.confirm("WARNING: Updates to certificate-authority-config and certificate-revocation-list-details and freeform-tags and defined-tags and certificate-authority-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if certificate_authority_config is not None:
        _details['certificateAuthorityConfig'] = cli_util.parse_json_parameter("certificate_authority_config", certificate_authority_config)

    if certificate_revocation_list_details is not None:
        _details['certificateRevocationListDetails'] = cli_util.parse_json_parameter("certificate_revocation_list_details", certificate_revocation_list_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_authority_rules is not None:
        _details['certificateAuthorityRules'] = cli_util.parse_json_parameter("certificate_authority_rules", certificate_authority_rules)

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_certificate_authority(
        certificate_authority_id=certificate_authority_id,
        update_certificate_authority_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate_authority') and callable(getattr(client, 'get_certificate_authority')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate_authority(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details.command_name', 'update-certificate-authority-update-subordinate-ca-issued-by-internal-ca-config-details'), help=u"""Updates the properties of the specified certificate authority (CA). \n[Command Reference](updateCertificateAuthority)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--description', help=u"""A brief description of the CA.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Makes this version the current version. This property cannot be updated in combination with any other properties.""")
@cli_util.option('--certificate-revocation-list-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-authority-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules that control how the CA is used and managed.

This option is a JSON list with items of type CertificateAuthorityRule.  For documentation on CertificateAuthorityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateAuthorityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--certificate-authority-config-version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@cli_util.option('--certificate-authority-config-stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the CA. The default is `PENDING`, meaning that the CA is staged and available for use. A CA version that you mark as `CURRENT` is currently in use, but you don't yet want to rotate it into current, active use. For example, you might create or update a CA and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--certificate-authority-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_authority_id, description, current_version_number, certificate_revocation_list_details, freeform_tags, defined_tags, certificate_authority_rules, if_match, certificate_authority_config_version_name, certificate_authority_config_stage, certificate_authority_config_validity):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')
    if not force:
        if certificate_revocation_list_details or freeform_tags or defined_tags or certificate_authority_rules:
            if not click.confirm("WARNING: Updates to certificate-revocation-list-details and freeform-tags and defined-tags and certificate-authority-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateAuthorityConfig'] = {}

    if description is not None:
        _details['description'] = description

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if certificate_revocation_list_details is not None:
        _details['certificateRevocationListDetails'] = cli_util.parse_json_parameter("certificate_revocation_list_details", certificate_revocation_list_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_authority_rules is not None:
        _details['certificateAuthorityRules'] = cli_util.parse_json_parameter("certificate_authority_rules", certificate_authority_rules)

    if certificate_authority_config_version_name is not None:
        _details['certificateAuthorityConfig']['versionName'] = certificate_authority_config_version_name

    if certificate_authority_config_stage is not None:
        _details['certificateAuthorityConfig']['stage'] = certificate_authority_config_stage

    if certificate_authority_config_validity is not None:
        _details['certificateAuthorityConfig']['validity'] = cli_util.parse_json_parameter("certificate_authority_config_validity", certificate_authority_config_validity)

    _details['certificateAuthorityConfig']['configType'] = 'SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_certificate_authority(
        certificate_authority_id=certificate_authority_id,
        update_certificate_authority_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate_authority') and callable(getattr(client, 'get_certificate_authority')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate_authority(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_authority_group.command(name=cli_util.override('certs_mgmt.update_certificate_authority_update_root_ca_by_generating_internally_config_details.command_name', 'update-certificate-authority-update-root-ca-by-generating-internally-config-details'), help=u"""Updates the properties of the specified certificate authority (CA). \n[Command Reference](updateCertificateAuthority)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--description', help=u"""A brief description of the CA.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Makes this version the current version. This property cannot be updated in combination with any other properties.""")
@cli_util.option('--certificate-revocation-list-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-authority-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules that control how the CA is used and managed.

This option is a JSON list with items of type CertificateAuthorityRule.  For documentation on CertificateAuthorityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateAuthorityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--certificate-authority-config-version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@cli_util.option('--certificate-authority-config-stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the CA. The default is `PENDING`, meaning that the CA is staged and available for use. A CA version that you mark as `CURRENT` is currently in use, but you don't yet want to rotate it into current, active use. For example, you might create or update a CA and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--certificate-authority-config-validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-authority-config-validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def update_certificate_authority_update_root_ca_by_generating_internally_config_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_authority_id, description, current_version_number, certificate_revocation_list_details, freeform_tags, defined_tags, certificate_authority_rules, if_match, certificate_authority_config_version_name, certificate_authority_config_stage, certificate_authority_config_validity):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')
    if not force:
        if certificate_revocation_list_details or freeform_tags or defined_tags or certificate_authority_rules:
            if not click.confirm("WARNING: Updates to certificate-revocation-list-details and freeform-tags and defined-tags and certificate-authority-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateAuthorityConfig'] = {}

    if description is not None:
        _details['description'] = description

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if certificate_revocation_list_details is not None:
        _details['certificateRevocationListDetails'] = cli_util.parse_json_parameter("certificate_revocation_list_details", certificate_revocation_list_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if certificate_authority_rules is not None:
        _details['certificateAuthorityRules'] = cli_util.parse_json_parameter("certificate_authority_rules", certificate_authority_rules)

    if certificate_authority_config_version_name is not None:
        _details['certificateAuthorityConfig']['versionName'] = certificate_authority_config_version_name

    if certificate_authority_config_stage is not None:
        _details['certificateAuthorityConfig']['stage'] = certificate_authority_config_stage

    if certificate_authority_config_validity is not None:
        _details['certificateAuthorityConfig']['validity'] = cli_util.parse_json_parameter("certificate_authority_config_validity", certificate_authority_config_validity)

    _details['certificateAuthorityConfig']['configType'] = 'ROOT_CA_GENERATED_INTERNALLY'

    client = cli_util.build_client('certificates_management', 'certificates_management', ctx)
    result = client.update_certificate_authority(
        certificate_authority_id=certificate_authority_id,
        update_certificate_authority_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate_authority') and callable(getattr(client, 'get_certificate_authority')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate_authority(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
