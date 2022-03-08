# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MenuItem(Component):
    """A MenuItem component.
Combine a list of secondary actions into single interactive area. For more information, see: https://mantine.dev/core/menu/

Keyword arguments:

- children (string; optional):
    Item children.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- color (a value equal to: "dark", "gray", "red", "pink", "grape", "violet", "indigo", "blue", "cyan", "teal", "green", "lime", "yellow", "orange"; optional):
    Any color from theme.colors.

- disabled (boolean; optional):
    Is item disabled.

- icon (boolean | number | string | dict | list; optional):
    Icon rendered on the left side of label.

- rightSection (boolean | number | string | dict | list; optional):
    Any react node to render on the right side of item, for example,
    keyboard shortcut or badge.

- style (dict; optional):
    Inline style override."""
    @_explicitize_args
    def __init__(self, children=None, class_name=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, icon=Component.UNDEFINED, id=Component.UNDEFINED, rightSection=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'class_name', 'color', 'disabled', 'icon', 'rightSection', 'style']
        self._type = 'MenuItem'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'class_name', 'color', 'disabled', 'icon', 'rightSection', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MenuItem, self).__init__(children=children, **args)
