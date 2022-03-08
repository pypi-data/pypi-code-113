"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.bank_transfer_direction import BankTransferDirection
    from plaid.model.bank_transfer_event_type import BankTransferEventType
    from plaid.model.bank_transfer_failure import BankTransferFailure
    from plaid.model.bank_transfer_type import BankTransferType
    globals()['BankTransferDirection'] = BankTransferDirection
    globals()['BankTransferEventType'] = BankTransferEventType
    globals()['BankTransferFailure'] = BankTransferFailure
    globals()['BankTransferType'] = BankTransferType


class BankTransferEvent(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('event_id',): {
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'event_id': (int,),  # noqa: E501
            'timestamp': (datetime,),  # noqa: E501
            'event_type': (BankTransferEventType,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'bank_transfer_id': (str,),  # noqa: E501
            'origination_account_id': (str, none_type,),  # noqa: E501
            'bank_transfer_type': (BankTransferType,),  # noqa: E501
            'bank_transfer_amount': (str,),  # noqa: E501
            'bank_transfer_iso_currency_code': (str,),  # noqa: E501
            'failure_reason': (BankTransferFailure,),  # noqa: E501
            'direction': (BankTransferDirection,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'event_id': 'event_id',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'event_type': 'event_type',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'bank_transfer_id': 'bank_transfer_id',  # noqa: E501
        'origination_account_id': 'origination_account_id',  # noqa: E501
        'bank_transfer_type': 'bank_transfer_type',  # noqa: E501
        'bank_transfer_amount': 'bank_transfer_amount',  # noqa: E501
        'bank_transfer_iso_currency_code': 'bank_transfer_iso_currency_code',  # noqa: E501
        'failure_reason': 'failure_reason',  # noqa: E501
        'direction': 'direction',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, event_id, timestamp, event_type, account_id, bank_transfer_id, origination_account_id, bank_transfer_type, bank_transfer_amount, bank_transfer_iso_currency_code, failure_reason, direction, *args, **kwargs):  # noqa: E501
        """BankTransferEvent - a model defined in OpenAPI

        Args:
            event_id (int): Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.
            timestamp (datetime): The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`.
            event_type (BankTransferEventType):
            account_id (str): The account ID associated with the bank transfer.
            bank_transfer_id (str): Plaid’s unique identifier for a bank transfer.
            origination_account_id (str, none_type): The ID of the origination account that this balance belongs to.
            bank_transfer_type (BankTransferType):
            bank_transfer_amount (str): The bank transfer amount.
            bank_transfer_iso_currency_code (str): The currency of the bank transfer amount.
            failure_reason (BankTransferFailure):
            direction (BankTransferDirection):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.event_id = event_id
        self.timestamp = timestamp
        self.event_type = event_type
        self.account_id = account_id
        self.bank_transfer_id = bank_transfer_id
        self.origination_account_id = origination_account_id
        self.bank_transfer_type = bank_transfer_type
        self.bank_transfer_amount = bank_transfer_amount
        self.bank_transfer_iso_currency_code = bank_transfer_iso_currency_code
        self.failure_reason = failure_reason
        self.direction = direction
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
