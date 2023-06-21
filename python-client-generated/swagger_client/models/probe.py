# coding: utf-8

"""
    ITM MVP TA3 API

    This is the specification of a proposed TA3 API for the In The Moment (ITM) Minimum Viable Product (MVP).  Currently, there is an Evaluation API for TA2 and a preliminary scenario/probe submission API for TA1 that won't be used in the MVP, and currently lacks an API regarding sending probe responses and receiving alignment scores from TA1.  The API is based on the OpenAPI 3.0 specification.  Some aspects of this API are not necessarily planned to be implemented for MVP, but show the direction we are heading.  # noqa: E501

    OpenAPI spec version: 0.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Probe(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'scenario_id': 'str',
        'type': 'str',
        'prompt': 'str',
        'state': 'State',
        'options': 'list[ProbeOption]'
    }

    attribute_map = {
        'id': 'id',
        'scenario_id': 'scenario_id',
        'type': 'type',
        'prompt': 'prompt',
        'state': 'state',
        'options': 'options'
    }

    def __init__(self, id=None, scenario_id=None, type=None, prompt=None, state=None, options=None):  # noqa: E501
        """Probe - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._scenario_id = None
        self._type = None
        self._prompt = None
        self._state = None
        self._options = None
        self.discriminator = None
        self.id = id
        self.scenario_id = scenario_id
        self.type = type
        self.prompt = prompt
        if state is not None:
            self.state = state
        if options is not None:
            self.options = options

    @property
    def id(self):
        """Gets the id of this Probe.  # noqa: E501

        globally unique probe ID  # noqa: E501

        :return: The id of this Probe.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Probe.

        globally unique probe ID  # noqa: E501

        :param id: The id of this Probe.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def scenario_id(self):
        """Gets the scenario_id of this Probe.  # noqa: E501

        scenario ID this probe is for  # noqa: E501

        :return: The scenario_id of this Probe.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this Probe.

        scenario ID this probe is for  # noqa: E501

        :param scenario_id: The scenario_id of this Probe.  # noqa: E501
        :type: str
        """
        if scenario_id is None:
            raise ValueError("Invalid value for `scenario_id`, must not be `None`")  # noqa: E501

        self._scenario_id = scenario_id

    @property
    def type(self):
        """Gets the type of this Probe.  # noqa: E501

        TAs will need to agree on the types of questions being asked; only MultipleChoice is supported for MVP  # noqa: E501

        :return: The type of this Probe.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Probe.

        TAs will need to agree on the types of questions being asked; only MultipleChoice is supported for MVP  # noqa: E501

        :param type: The type of this Probe.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["MultipleChoice", "FreeResponse", "PatientOrdering"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def prompt(self):
        """Gets the prompt of this Probe.  # noqa: E501

        a plain text natural language question for the DM  # noqa: E501

        :return: The prompt of this Probe.  # noqa: E501
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """Sets the prompt of this Probe.

        a plain text natural language question for the DM  # noqa: E501

        :param prompt: The prompt of this Probe.  # noqa: E501
        :type: str
        """
        if prompt is None:
            raise ValueError("Invalid value for `prompt`, must not be `None`")  # noqa: E501

        self._prompt = prompt

    @property
    def state(self):
        """Gets the state of this Probe.  # noqa: E501


        :return: The state of this Probe.  # noqa: E501
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Probe.


        :param state: The state of this Probe.  # noqa: E501
        :type: State
        """

        self._state = state

    @property
    def options(self):
        """Gets the options of this Probe.  # noqa: E501

        the list of valid choices for the DM to choose among  # noqa: E501

        :return: The options of this Probe.  # noqa: E501
        :rtype: list[ProbeOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Probe.

        the list of valid choices for the DM to choose among  # noqa: E501

        :param options: The options of this Probe.  # noqa: E501
        :type: list[ProbeOption]
        """

        self._options = options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Probe, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Probe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
