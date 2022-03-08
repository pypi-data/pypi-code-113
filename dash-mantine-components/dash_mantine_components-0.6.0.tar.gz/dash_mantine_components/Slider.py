# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Slider(Component):
    """A Slider component.
Capture user feedback from a range of values. For more information, see: https://mantine.dev/core/slider/

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- color (a value equal to: "dark", "gray", "red", "pink", "grape", "violet", "indigo", "blue", "cyan", "teal", "green", "lime", "yellow", "orange"; optional):
    Slider color.

- labelAlwaysOn (boolean; optional):
    If True label will be not be hidden when user stops dragging.

- labelTransition (a value equal to: "fade", "skew-up", "skew-down", "rotate-right", "rotate-left", "slide-down", "slide-up", "slide-right", "slide-left", "scale-y", "scale-x", "scale", "pop", "pop-top-left", "pop-top-right", "pop-bottom-left", "pop-bottom-right"; optional):
    Label appear/disappear transition.

- labelTransitionDuration (number; optional):
    Label appear/disappear transition duration in ms.

- labelTransitionTimingFunction (string; optional):
    Label appear/disappear transition timing function, defaults to
    theme.transitionRimingFunction.

- marks (list of dicts; optional):
    Marks which will be placed on the track.

    `marks` is a list of dicts with keys:

    - label (string; optional):
        The option's label.

    - value (number; required):
        option's value.

- max (number; optional):
    Maximum possible value.

- min (number; optional):
    Minimal possible value.

- name (string; optional):
    Hidden input name, use with uncontrolled variant.

- radius (a value equal to: "xs", "sm", "md", "lg", "xl" | number; optional):
    Track border-radius from theme or number to set border-radius in
    px.

- showLabelOnHover (boolean; optional):
    If True slider label will appear on hover.

- size (a value equal to: "xs", "sm", "md", "lg", "xl"; optional):
    Predefined track and thumb size, number to set sizes in px.

- step (number; optional):
    Number by which value will be incremented/decremented with thumb
    drag and arrows.

- style (dict; optional):
    Inline style override.

- thumbChildren (boolean | number | string | dict | list; optional):
    Thumb children, can be used to add icon.

- value (number; optional):
    Current value for controlled slider."""
    @_explicitize_args
    def __init__(self, class_name=Component.UNDEFINED, color=Component.UNDEFINED, id=Component.UNDEFINED, labelAlwaysOn=Component.UNDEFINED, labelTransition=Component.UNDEFINED, labelTransitionDuration=Component.UNDEFINED, labelTransitionTimingFunction=Component.UNDEFINED, marks=Component.UNDEFINED, max=Component.UNDEFINED, min=Component.UNDEFINED, name=Component.UNDEFINED, radius=Component.UNDEFINED, showLabelOnHover=Component.UNDEFINED, size=Component.UNDEFINED, step=Component.UNDEFINED, style=Component.UNDEFINED, thumbChildren=Component.UNDEFINED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'class_name', 'color', 'labelAlwaysOn', 'labelTransition', 'labelTransitionDuration', 'labelTransitionTimingFunction', 'marks', 'max', 'min', 'name', 'radius', 'showLabelOnHover', 'size', 'step', 'style', 'thumbChildren', 'value']
        self._type = 'Slider'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'class_name', 'color', 'labelAlwaysOn', 'labelTransition', 'labelTransitionDuration', 'labelTransitionTimingFunction', 'marks', 'max', 'min', 'name', 'radius', 'showLabelOnHover', 'size', 'step', 'style', 'thumbChildren', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Slider, self).__init__(**args)
