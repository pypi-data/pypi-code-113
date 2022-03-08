# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tab(Component):
    """A Tab component.
Utility component to pass to Tabs. For more information, see: https://mantine.dev/core/tabs/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Tab content.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- disabled (boolean; optional):
    A tab can show it is currently unable to be interacted with.

- icon (boolean | number | string | dict | list; optional):
    Icon.

- label (boolean | number | string | dict | list; optional):
    Tab control label."""
    @_explicitize_args
    def __init__(self, children=None, class_name=Component.UNDEFINED, disabled=Component.UNDEFINED, icon=Component.UNDEFINED, id=Component.UNDEFINED, label=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'class_name', 'disabled', 'icon', 'label']
        self._type = 'Tab'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'class_name', 'disabled', 'icon', 'label']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Tab, self).__init__(children=children, **args)
