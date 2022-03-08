# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4072
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class VendorModelRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'supplier': 'str',
        'model_name': 'str',
        'instrument_type': 'str',
        'parameters': 'str',
        'model_options': 'ModelOptions',
        'instrument_id': 'str'
    }

    attribute_map = {
        'supplier': 'supplier',
        'model_name': 'modelName',
        'instrument_type': 'instrumentType',
        'parameters': 'parameters',
        'model_options': 'modelOptions',
        'instrument_id': 'instrumentId'
    }

    required_map = {
        'supplier': 'required',
        'model_name': 'required',
        'instrument_type': 'required',
        'parameters': 'optional',
        'model_options': 'optional',
        'instrument_id': 'optional'
    }

    def __init__(self, supplier=None, model_name=None, instrument_type=None, parameters=None, model_options=None, instrument_id=None, local_vars_configuration=None):  # noqa: E501
        """VendorModelRule - a model defined in OpenAPI"
        
        :param supplier:  The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds (required)
        :type supplier: str
        :param model_name:  The vendor library model name (required)
        :type model_name: str
        :param instrument_type:  The vendor library instrument type (required)
        :type instrument_type: str
        :param parameters:  THIS FIELD IS DEPRECATED - use ModelOptions  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood.
        :type parameters: str
        :param model_options: 
        :type model_options: lusid.ModelOptions
        :param instrument_id:  This field should generally not be required. It indicates a specific case where there is a particular need to make a rule apply to only a single instrument  specified by an identifier on that instrument such as its LUID. One particular example would be to control the behaviour of a look-through portfolio scaling  methodology, such as where there is a mixture of indices and credit-debit portfolios where scaling on the sum of valuation would be deemed incorrectly for one  set but desired in general.
        :type instrument_id: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._supplier = None
        self._model_name = None
        self._instrument_type = None
        self._parameters = None
        self._model_options = None
        self._instrument_id = None
        self.discriminator = None

        self.supplier = supplier
        self.model_name = model_name
        self.instrument_type = instrument_type
        self.parameters = parameters
        if model_options is not None:
            self.model_options = model_options
        self.instrument_id = instrument_id

    @property
    def supplier(self):
        """Gets the supplier of this VendorModelRule.  # noqa: E501

        The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds  # noqa: E501

        :return: The supplier of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this VendorModelRule.

        The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds  # noqa: E501

        :param supplier: The supplier of this VendorModelRule.  # noqa: E501
        :type supplier: str
        """
        if self.local_vars_configuration.client_side_validation and supplier is None:  # noqa: E501
            raise ValueError("Invalid value for `supplier`, must not be `None`")  # noqa: E501
        allowed_values = ["Lusid", "RefinitivQps", "RefinitivTracsWeb", "VolMaster", "IsdaCds"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and supplier not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `supplier` ({0}), must be one of {1}"  # noqa: E501
                .format(supplier, allowed_values)
            )

        self._supplier = supplier

    @property
    def model_name(self):
        """Gets the model_name of this VendorModelRule.  # noqa: E501

        The vendor library model name  # noqa: E501

        :return: The model_name of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this VendorModelRule.

        The vendor library model name  # noqa: E501

        :param model_name: The model_name of this VendorModelRule.  # noqa: E501
        :type model_name: str
        """
        if self.local_vars_configuration.client_side_validation and model_name is None:  # noqa: E501
            raise ValueError("Invalid value for `model_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model_name is not None and len(model_name) > 128):
            raise ValueError("Invalid value for `model_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model_name is not None and len(model_name) < 0):
            raise ValueError("Invalid value for `model_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._model_name = model_name

    @property
    def instrument_type(self):
        """Gets the instrument_type of this VendorModelRule.  # noqa: E501

        The vendor library instrument type  # noqa: E501

        :return: The instrument_type of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this VendorModelRule.

        The vendor library instrument type  # noqa: E501

        :param instrument_type: The instrument_type of this VendorModelRule.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_type is not None and len(instrument_type) > 32):
            raise ValueError("Invalid value for `instrument_type`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_type is not None and len(instrument_type) < 0):
            raise ValueError("Invalid value for `instrument_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._instrument_type = instrument_type

    @property
    def parameters(self):
        """Gets the parameters of this VendorModelRule.  # noqa: E501

        THIS FIELD IS DEPRECATED - use ModelOptions  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood.  # noqa: E501

        :return: The parameters of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this VendorModelRule.

        THIS FIELD IS DEPRECATED - use ModelOptions  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood.  # noqa: E501

        :param parameters: The parameters of this VendorModelRule.  # noqa: E501
        :type parameters: str
        """
        if (self.local_vars_configuration.client_side_validation and
                parameters is not None and len(parameters) > 64):
            raise ValueError("Invalid value for `parameters`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                parameters is not None and len(parameters) < 0):
            raise ValueError("Invalid value for `parameters`, length must be greater than or equal to `0`")  # noqa: E501

        self._parameters = parameters

    @property
    def model_options(self):
        """Gets the model_options of this VendorModelRule.  # noqa: E501


        :return: The model_options of this VendorModelRule.  # noqa: E501
        :rtype: lusid.ModelOptions
        """
        return self._model_options

    @model_options.setter
    def model_options(self, model_options):
        """Sets the model_options of this VendorModelRule.


        :param model_options: The model_options of this VendorModelRule.  # noqa: E501
        :type model_options: lusid.ModelOptions
        """

        self._model_options = model_options

    @property
    def instrument_id(self):
        """Gets the instrument_id of this VendorModelRule.  # noqa: E501

        This field should generally not be required. It indicates a specific case where there is a particular need to make a rule apply to only a single instrument  specified by an identifier on that instrument such as its LUID. One particular example would be to control the behaviour of a look-through portfolio scaling  methodology, such as where there is a mixture of indices and credit-debit portfolios where scaling on the sum of valuation would be deemed incorrectly for one  set but desired in general.  # noqa: E501

        :return: The instrument_id of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this VendorModelRule.

        This field should generally not be required. It indicates a specific case where there is a particular need to make a rule apply to only a single instrument  specified by an identifier on that instrument such as its LUID. One particular example would be to control the behaviour of a look-through portfolio scaling  methodology, such as where there is a mixture of indices and credit-debit portfolios where scaling on the sum of valuation would be deemed incorrectly for one  set but desired in general.  # noqa: E501

        :param instrument_id: The instrument_id of this VendorModelRule.  # noqa: E501
        :type instrument_id: str
        """

        self._instrument_id = instrument_id

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VendorModelRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VendorModelRule):
            return True

        return self.to_dict() != other.to_dict()
