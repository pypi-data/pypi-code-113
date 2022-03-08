# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCustomProtectionRuleDetails(object):
    """
    The required data to create a custom protection rule.
    For more information about custom protection rules, see `Custom Protection Rules`__.
    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/customprotectionrules.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCustomProtectionRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCustomProtectionRuleDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateCustomProtectionRuleDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateCustomProtectionRuleDetails.
        :type description: str

        :param template:
            The value to assign to the template property of this CreateCustomProtectionRuleDetails.
        :type template: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCustomProtectionRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCustomProtectionRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'template': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'template': 'template',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._template = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCustomProtectionRuleDetails.
        The `OCID`__ of the compartment in which to create the custom protection rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCustomProtectionRuleDetails.
        The `OCID`__ of the compartment in which to create the custom protection rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateCustomProtectionRuleDetails.
        A user-friendly name for the custom protection rule.


        :return: The display_name of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCustomProtectionRuleDetails.
        A user-friendly name for the custom protection rule.


        :param display_name: The display_name of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateCustomProtectionRuleDetails.
        A description for the Custom Protection rule.


        :return: The description of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCustomProtectionRuleDetails.
        A description for the Custom Protection rule.


        :param description: The description of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def template(self):
        """
        **[Required]** Gets the template of this CreateCustomProtectionRuleDetails.
        The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language.

        Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule.

        `id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example.

        `ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is updated.

        *Example:*
          ```
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 1/2.',        \\
                  id: {{id_1}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 2/2.',        \\
                  id: {{id_2}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          ```


        The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis phase.

        For more information about custom protection rules, see `Custom Protection Rules`__.

        For more information about ModSecurity syntax, see `Making Rules: The Basic Syntax`__.

        For more information about ModSecurity's open source WAF rules, see `Mod Security's OWASP Core Rule Set documentation`__.

        __ https://docs.cloud.oracle.com/Content/WAF/tasks/customprotectionrules.htm
        __ https://www.modsecurity.org/CRS/Documentation/making.html
        __ https://www.modsecurity.org/CRS/Documentation/index.html


        :return: The template of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CreateCustomProtectionRuleDetails.
        The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language.

        Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule.

        `id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example.

        `ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is updated.

        *Example:*
          ```
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 1/2.',        \\
                  id: {{id_1}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 2/2.',        \\
                  id: {{id_2}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          ```


        The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis phase.

        For more information about custom protection rules, see `Custom Protection Rules`__.

        For more information about ModSecurity syntax, see `Making Rules: The Basic Syntax`__.

        For more information about ModSecurity's open source WAF rules, see `Mod Security's OWASP Core Rule Set documentation`__.

        __ https://docs.cloud.oracle.com/Content/WAF/tasks/customprotectionrules.htm
        __ https://www.modsecurity.org/CRS/Documentation/making.html
        __ https://www.modsecurity.org/CRS/Documentation/index.html


        :param template: The template of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._template = template

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCustomProtectionRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCustomProtectionRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCustomProtectionRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCustomProtectionRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCustomProtectionRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCustomProtectionRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCustomProtectionRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCustomProtectionRuleDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
