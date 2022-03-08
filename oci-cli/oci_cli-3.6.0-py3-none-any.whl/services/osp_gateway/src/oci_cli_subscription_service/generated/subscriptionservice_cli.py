# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.osp_gateway.src.oci_cli_osp_gateway.generated import osp_gateway_service_cli


@click.command(cli_util.override('subscription_service.subscription_service_root_group.command_name', 'subscription-service'), cls=CommandGroupWithAlias, help=cli_util.override('subscription_service.subscription_service_root_group.help', """This site describes all the Rest endpoints of OSP Gateway."""), short_help=cli_util.override('subscription_service.subscription_service_root_group.short_help', """OSP Gateway API"""))
@cli_util.help_option_group
def subscription_service_root_group():
    pass


@click.command(cli_util.override('subscription_service.subscription_group.command_name', 'subscription'), cls=CommandGroupWithAlias, help="""Subscription details object which extends the SubscriptionSummary""")
@cli_util.help_option_group
def subscription_group():
    pass


osp_gateway_service_cli.osp_gateway_service_group.add_command(subscription_service_root_group)
subscription_service_root_group.add_command(subscription_group)


@subscription_group.command(name=cli_util.override('subscription_service.authorize_subscription_payment.command_name', 'authorize-subscription-payment'), help=u"""PSD2 authorization for subscription payment \n[Command Reference](authorizeSubscriptionPayment)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--subscription-id', required=True, help=u"""Subscription id(OCID).""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--subscription', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--language-code', required=True, help=u"""Language code""")
@cli_util.option('--email', required=True, help=u"""User email""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'subscription': {'module': 'osp_gateway', 'class': 'Subscription'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'subscription': {'module': 'osp_gateway', 'class': 'Subscription'}}, output_type={'module': 'osp_gateway', 'class': 'AuthorizeSubscriptionPaymentReceipt'})
@cli_util.wrap_exceptions
def authorize_subscription_payment(ctx, from_json, osp_home_region, subscription_id, compartment_id, subscription, language_code, email, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['subscription'] = cli_util.parse_json_parameter("subscription", subscription)
    _details['languageCode'] = language_code
    _details['email'] = email

    client = cli_util.build_client('osp_gateway', 'subscription_service', ctx)
    result = client.authorize_subscription_payment(
        osp_home_region=osp_home_region,
        subscription_id=subscription_id,
        compartment_id=compartment_id,
        authorize_subscription_payment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('subscription_service.get_subscription.command_name', 'get'), help=u"""Get the subscription plan. \n[Command Reference](getSubscription)""")
@cli_util.option('--subscription-id', required=True, help=u"""Subscription id(OCID).""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'Subscription'})
@cli_util.wrap_exceptions
def get_subscription(ctx, from_json, subscription_id, osp_home_region, compartment_id):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osp_gateway', 'subscription_service', ctx)
    result = client.get_subscription(
        subscription_id=subscription_id,
        osp_home_region=osp_home_region,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('subscription_service.list_subscriptions.command_name', 'list'), help=u"""Get the subscription data for the compartment \n[Command Reference](listSubscriptions)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["INVOICE_NO", "REF_NO", "STATUS", "TYPE", "INVOICE_DATE", "DUE_DATE", "PAYM_REF", "TOTAL_AMOUNT", "BALANCE_DUE"]), help=u"""The field to sort by. Only one field can be selected for sorting.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use (ascending or descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'SubscriptionCollection'})
@cli_util.wrap_exceptions
def list_subscriptions(ctx, from_json, all_pages, page_size, osp_home_region, compartment_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osp_gateway', 'subscription_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subscriptions,
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subscriptions,
            limit,
            page_size,
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_subscriptions(
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('subscription_service.pay_subscription.command_name', 'pay'), help=u"""Pay a subscription \n[Command Reference](paySubscription)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--subscription-id', required=True, help=u"""Subscription id(OCID).""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--subscription', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--language-code', required=True, help=u"""Language code""")
@cli_util.option('--email', required=True, help=u"""User email""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'subscription': {'module': 'osp_gateway', 'class': 'Subscription'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'subscription': {'module': 'osp_gateway', 'class': 'Subscription'}}, output_type={'module': 'osp_gateway', 'class': 'PaySubscriptionReceipt'})
@cli_util.wrap_exceptions
def pay_subscription(ctx, from_json, osp_home_region, subscription_id, compartment_id, subscription, language_code, email, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['subscription'] = cli_util.parse_json_parameter("subscription", subscription)
    _details['languageCode'] = language_code
    _details['email'] = email

    client = cli_util.build_client('osp_gateway', 'subscription_service', ctx)
    result = client.pay_subscription(
        osp_home_region=osp_home_region,
        subscription_id=subscription_id,
        compartment_id=compartment_id,
        pay_subscription_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('subscription_service.update_subscription.command_name', 'update'), help=u"""Update plan of the subscription. \n[Command Reference](updateSubscription)""")
@cli_util.option('--subscription-id', required=True, help=u"""Subscription id(OCID).""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--subscription', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--email', required=True, help=u"""User email""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'subscription': {'module': 'osp_gateway', 'class': 'Subscription'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'subscription': {'module': 'osp_gateway', 'class': 'Subscription'}}, output_type={'module': 'osp_gateway', 'class': 'Subscription'})
@cli_util.wrap_exceptions
def update_subscription(ctx, from_json, force, subscription_id, osp_home_region, compartment_id, subscription, email, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')
    if not force:
        if subscription:
            if not click.confirm("WARNING: Updates to subscription will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['subscription'] = cli_util.parse_json_parameter("subscription", subscription)
    _details['email'] = email

    client = cli_util.build_client('osp_gateway', 'subscription_service', ctx)
    result = client.update_subscription(
        subscription_id=subscription_id,
        osp_home_region=osp_home_region,
        compartment_id=compartment_id,
        update_subscription_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
