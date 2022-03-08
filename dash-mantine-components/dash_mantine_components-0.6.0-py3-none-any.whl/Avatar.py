# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Avatar(Component):
    """An Avatar component.
Display user profile image, initials or fallback icon. For more information, see: https://mantine.dev/core/avatar/

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- alt (string; optional):
    Image alt text or title for placeholder variant.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- color (a value equal to: "dark", "gray", "red", "pink", "grape", "violet", "indigo", "blue", "cyan", "teal", "green", "lime", "yellow", "orange"; default "gray"):
    Color from theme.colors used for letter and icon placeholders.

- radius (a value equal to: "xs", "sm", "md", "lg", "xl" | number; default "sm"):
    Value from theme.radius or number to set border-radius in px.

- size (a value equal to: "xs", "sm", "md", "lg", "xl" | number; default "md"):
    Avatar width and height.

- src (string; optional):
    Image url.

- style (dict; optional):
    Inline style override."""
    @_explicitize_args
    def __init__(self, alt=Component.UNDEFINED, class_name=Component.UNDEFINED, color=Component.UNDEFINED, id=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, src=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'class_name', 'color', 'radius', 'size', 'src', 'style']
        self._type = 'Avatar'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'class_name', 'color', 'radius', 'size', 'src', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Avatar, self).__init__(**args)
