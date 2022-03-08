# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ThemeIcon(Component):
    """A ThemeIcon component.
Render icon inside element with theme colors. For more information, see: https://mantine.dev/core/theme-icon/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Component children.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- color (a value equal to: "dark", "gray", "red", "pink", "grape", "violet", "indigo", "blue", "cyan", "teal", "green", "lime", "yellow", "orange"; optional):
    Icon color from theme.

- gradient (dict; optional):
    Controls gradient settings in gradient variant only.

    `gradient` is a dict with keys:

    - deg (number; optional)

    - from (string; optional)

    - to (string; optional)

- radius (a value equal to: "xs", "sm", "md", "lg", "xl" | number; optional):
    Predefined border-radius from theme.radius or number for
    border-radius in px.

- size (a value equal to: "xs", "sm", "md", "lg", "xl" | number; optional):
    Predefined width and height or number for width and height in px.

- style (dict; optional):
    Inline style override.

- variant (a value equal to: "filled", "light", "gradient"; optional):
    Controls appearance."""
    @_explicitize_args
    def __init__(self, children=None, class_name=Component.UNDEFINED, color=Component.UNDEFINED, gradient=Component.UNDEFINED, id=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, style=Component.UNDEFINED, variant=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'class_name', 'color', 'gradient', 'radius', 'size', 'style', 'variant']
        self._type = 'ThemeIcon'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'class_name', 'color', 'gradient', 'radius', 'size', 'style', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ThemeIcon, self).__init__(children=children, **args)
