# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MultiSelect(Component):
    """A MultiSelect component.
Custom searchable MultiSelect. For more information, see: https://mantine.dev/core/multi-select/

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- clearSearchOnBlur (boolean; optional):
    Clear search field value on blur.

- clearSearchOnChange (boolean; optional):
    Clear search value when item is selected.

- clearable (boolean; optional):
    Allow to clear value.

- data (list of dicts; optional):
    Select options used to renderer items in dropdown.

    `data` is a list of dicts with keys:

    - disabled (boolean; optional):
        If True, this option is disabled and cannot be selected.

    - group (string; optional):
        Item Groups.

    - label (string; optional):
        The option's label.

    - value (string; required):
        Option's value. | list of strings

- description (boolean | number | string | dict | list; optional):
    Input description, displayed after label.

- disabled (boolean; optional):
    The component can show it is currently unable to be interacted
    with.

- error (boolean | number | string | dict | list; optional):
    Displays error message after input.

- icon (boolean | number | string | dict | list; optional):
    Adds icon on the left side of input.

- iconWidth (number; optional):
    Width of icon section in px.

- initiallyOpened (boolean; optional):
    Initial dropdown opened state.

- invalid (boolean; optional):
    Sets border color to red and aria-invalid=True on input element.

- label (boolean | number | string | dict | list; optional):
    Input label, displayed before input.

- limit (number; optional):
    Limit amount of items displayed at a time for searchable select.

- maxDropdownHeight (number; optional):
    Maximum dropdown height in px.

- maxSelectedValues (number; optional):
    Limit amount of items selected.

- multiline (boolean; optional):
    Will input have multiple lines?.

- nothingFound (string; optional):
    Nothing found label.

- persisted_props (list of a value equal to: "value"s; default ["value"]):
    Properties whose user interactions will persist after refreshing
    the component or the page.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: "local", "session", "memory"; default "local"):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- placeholder (string; optional):
    Placeholder, displayed when date is not selected.

- radius (a value equal to: "xs", "sm", "md", "lg", "xl" | number; optional):
    Input border-radius from theme or number to set border-radius in
    px.

- required (boolean; optional):
    Adds red asterisk on the right side of label.

- rightSection (boolean | number | string | dict | list; optional):
    Right section of input, similar to icon but on the right.

- rightSectionWidth (number; optional):
    Width of right section, is used to calculate input padding-right.

- searchable (boolean; optional):
    Set to True to enable search.

- selectOnBlur (boolean; optional):
    Select highlighted item on blur.

- shadow (a value equal to: "xs", "sm", "md", "lg", "xl" | number; optional):
    Dropdown shadow from theme or any value to set box-shadow.

- size (a value equal to: "xs", "sm", "md", "lg", "xl"; optional):
    Input size.

- style (dict; optional):
    Inline style override.

- switchDirectionOnFlip (boolean; optional):
    Whether to switch item order and keyboard navigation on dropdown
    position flip.

- transition (a value equal to: "fade", "skew-up", "skew-down", "rotate-right", "rotate-left", "slide-down", "slide-up", "slide-right", "slide-left", "scale-y", "scale-x", "scale", "pop", "pop-top-left", "pop-top-right", "pop-bottom-left", "pop-bottom-right"; optional):
    Dropdown appear/disappear transition.

- transitionDuration (number; optional):
    Dropdown appear/disappear transition duration.

- transitionTimingFunction (string; optional):
    Dropdown body transition timing function, defaults to
    theme.transitionTimingFunction.

- value (list of strings; optional):
    Selected value.

- variant (a value equal to: "default", "filled", "unstyled", "headless"; optional):
    Defines input appearance, defaults to default in light color
    scheme and filled in dark.

- withinPortal (boolean; optional):
    Whether to render the dropdown in a Portal.

- zIndex (number; optional):
    Dropdown z-index."""
    @_explicitize_args
    def __init__(self, class_name=Component.UNDEFINED, clearSearchOnBlur=Component.UNDEFINED, clearSearchOnChange=Component.UNDEFINED, clearable=Component.UNDEFINED, data=Component.UNDEFINED, description=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, icon=Component.UNDEFINED, iconWidth=Component.UNDEFINED, id=Component.UNDEFINED, initiallyOpened=Component.UNDEFINED, invalid=Component.UNDEFINED, label=Component.UNDEFINED, limit=Component.UNDEFINED, maxDropdownHeight=Component.UNDEFINED, maxSelectedValues=Component.UNDEFINED, multiline=Component.UNDEFINED, nothingFound=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, placeholder=Component.UNDEFINED, radius=Component.UNDEFINED, required=Component.UNDEFINED, rightSection=Component.UNDEFINED, rightSectionWidth=Component.UNDEFINED, searchable=Component.UNDEFINED, selectOnBlur=Component.UNDEFINED, shadow=Component.UNDEFINED, size=Component.UNDEFINED, style=Component.UNDEFINED, switchDirectionOnFlip=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, transitionTimingFunction=Component.UNDEFINED, value=Component.UNDEFINED, variant=Component.UNDEFINED, withinPortal=Component.UNDEFINED, zIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'class_name', 'clearSearchOnBlur', 'clearSearchOnChange', 'clearable', 'data', 'description', 'disabled', 'error', 'icon', 'iconWidth', 'initiallyOpened', 'invalid', 'label', 'limit', 'maxDropdownHeight', 'maxSelectedValues', 'multiline', 'nothingFound', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'radius', 'required', 'rightSection', 'rightSectionWidth', 'searchable', 'selectOnBlur', 'shadow', 'size', 'style', 'switchDirectionOnFlip', 'transition', 'transitionDuration', 'transitionTimingFunction', 'value', 'variant', 'withinPortal', 'zIndex']
        self._type = 'MultiSelect'
        self._namespace = 'dash_mantine_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'class_name', 'clearSearchOnBlur', 'clearSearchOnChange', 'clearable', 'data', 'description', 'disabled', 'error', 'icon', 'iconWidth', 'initiallyOpened', 'invalid', 'label', 'limit', 'maxDropdownHeight', 'maxSelectedValues', 'multiline', 'nothingFound', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'radius', 'required', 'rightSection', 'rightSectionWidth', 'searchable', 'selectOnBlur', 'shadow', 'size', 'style', 'switchDirectionOnFlip', 'transition', 'transitionDuration', 'transitionTimingFunction', 'value', 'variant', 'withinPortal', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MultiSelect, self).__init__(**args)
