# -*- coding: utf-8 -*-
"""
Some tools for templates
"""

from django import template

from coop_cms.templatetags.coop_utils import is_checkbox as _is_checkbox
from coop_cms.templatetags.coop_navigation import NavigationAsNestedUlNode, extract_kwargs

register = template.Library()

# Just for compatibility

@register.filter(name='is_checkbox')
def is_checkbox(field):
    """returns true if field is a checkbox"""
    return _is_checkbox(field)


@register.tag
def navigation_bootstrap(parser, token):
    """returns the bootstrap-friendly navigation"""
    kwargs = dict(li_node="coop_bootstrap/li_node.html")
    args = token.contents.split()
    kwargs.update(extract_kwargs(args))
    return NavigationAsNestedUlNode(**kwargs)
