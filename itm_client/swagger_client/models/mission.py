# coding: utf-8

"""
    ITM MVP TA3 API

    This is the specification of a proposed TA3 API for the In The Moment (ITM) Minimum Viable Product (MVP).  Currently, there is an Evaluation API for TA2 and a preliminary scenario/probe submission API for TA1 that won't be used in the MVP, and currently lacks an API regarding sending probe responses and receiving alignment scores from TA1.  The API is based on the OpenAPI 3.0 specification.  Some aspects of this API are not necessarily planned to be implemented for MVP, but show the direction we are heading.  # noqa: E501

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Mission(object):
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
        'unstructured': 'str',
        'mission_type': 'str'
    }

    attribute_map = {
        'unstructured': 'unstructured',
        'mission_type': 'mission_type'
    }

    def __init__(self, unstructured=None, mission_type=None):  # noqa: E501
        """Mission - a model defined in Swagger"""  # noqa: E501
        self._unstructured = None
        self._mission_type = None
        self.discriminator = None
        self.unstructured = unstructured
        self.mission_type = mission_type

    @property
    def unstructured(self):
        """Gets the unstructured of this Mission.  # noqa: E501

        natural language description of current mission  # noqa: E501

        :return: The unstructured of this Mission.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this Mission.

        natural language description of current mission  # noqa: E501

        :param unstructured: The unstructured of this Mission.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def mission_type(self):
        """Gets the mission_type of this Mission.  # noqa: E501

        enum of possible mission types; only ProtectVIP is supported for MVP  # noqa: E501

        :return: The mission_type of this Mission.  # noqa: E501
        :rtype: str
        """
        return self._mission_type

    @mission_type.setter
    def mission_type(self, mission_type):
        """Sets the mission_type of this Mission.

        enum of possible mission types; only ProtectVIP is supported for MVP  # noqa: E501

        :param mission_type: The mission_type of this Mission.  # noqa: E501
        :type: str
        """
        if mission_type is None:
            raise ValueError("Invalid value for `mission_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ProtectVIP", "ProtectCivilians", "DeliverCargo", "DefendBase"]  # noqa: E501
        if mission_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mission_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mission_type, allowed_values)
            )

        self._mission_type = mission_type

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
        if issubclass(Mission, dict):
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
        if not isinstance(other, Mission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
