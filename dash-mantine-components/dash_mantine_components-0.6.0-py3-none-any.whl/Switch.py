# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Switch(Component):
    """A Switch component.
Capture user feedback limited to small set of options. For more information, see: https://mantine.dev/core/switch/

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- checked (boolean; default False):
    State of check box.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- color (a value equal to: "dark", "gray", "red", "pink", "grape", "violet", "indigo", "blue", "cyan", "teal", "green", "lime", "yellow", "orange"; optional):
    Checkbox color.

- disabled (boolean; optional):
    A checkbox can show it is currently unable to be interacted with.

- label (boolean | number | string | dict | list; optional):
    Checkbox label.

- offLabel (string; optional):
    The inner label to be set when Switch is in an unchecked state.

- onLabel (string; optional):
    The inner label to be set when Switch is in the checked state.

- radius (a value equal to: "xs", "sm", "md", "lg", "xl" | number; optional):
    Predefined border-radius value from theme.radius or number for
    border-radius in px.

- size (a value equal to: "xs", "sm", "md", "lg", "xl"; optional):
    Predefined label font-size and checkbox width and height in px.

- style (dict; optional):
    Inline style override."""
    @_explicitize_args
    def __init__(self, class_name=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, id=Component.UNDEFINED, label=Component.UNDEFINED, onLabel=Component.UNDEFINED, offLabel=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, style=Component.UNDEFINED, checked=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'checked', 'class_name', 'color', 'disabled', 'label', 'offLabel', 'onLabel', 'radius', 'size', 'style']
        self._type = 'Switch'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'checked', 'class_name', 'color', 'disabled', 'label', 'offLabel', 'onLabel', 'radius', 'size', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Switch, self).__init__(**args)
