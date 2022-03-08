# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AvatarGroup(Component):
    """An AvatarGroup component.
Display user profile image, initials or fallback icon. For more information, see: https://mantine.dev/core/avatar/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    <Avatar /> components only.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- limit (number; default 2):
    Maximum amount of <Avatar /> components rendered, everything after
    limit is truncated.

- radius (a value equal to: "xs", "sm", "md", "lg", "xl" | number; default "xl"):
    Child <Avatar /> radius.

- size (a value equal to: "xs", "sm", "md", "lg", "xl" | number; default "md"):
    Child <Avatar /> components width and height.

- spacing (a value equal to: "xs", "sm", "md", "lg", "xl" | number; default "lg"):
    Spacing between avatars.

- style (dict; optional):
    Inline style override.

- total (number; optional):
    Total number of child <Avatar />, overrides the truncated amount."""
    @_explicitize_args
    def __init__(self, children=None, class_name=Component.UNDEFINED, id=Component.UNDEFINED, limit=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, spacing=Component.UNDEFINED, style=Component.UNDEFINED, total=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'class_name', 'limit', 'radius', 'size', 'spacing', 'style', 'total']
        self._type = 'AvatarGroup'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'class_name', 'limit', 'radius', 'size', 'spacing', 'style', 'total']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AvatarGroup, self).__init__(children=children, **args)
