# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

"""
Push Bodhi updates from testing to stable.
"""

import logging
import os

import click

from packit.cli.types import LocalProjectParameter
from packit.cli.utils import cover_packit_exception
from packit.cli.utils import get_packit_api
from packit.config import pass_config, get_context_settings

logger = logging.getLogger(__name__)


@click.command("push-updates", context_settings=get_context_settings())
@click.option("--update-alias", help="For example FEDORA-2019-ee5674e22c", default=None)
@click.argument("path_or_url", type=LocalProjectParameter(), default=os.path.curdir)
@pass_config
@cover_packit_exception
def push_updates(update_alias, config, path_or_url):
    """
    Find all Bodhi updates that have been in testing for more than 'Stable days' (7 by default)
    and push them to stable.

    """
    api = get_packit_api(config=config, local_project=path_or_url)
    api.push_updates(update_alias)
