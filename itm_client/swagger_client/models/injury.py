# coding: utf-8

"""
    ITM MVP TA3 API

    This is the specification of a proposed TA3 API for the In The Moment (ITM) Minimum Viable Product (MVP).  Currently, there is an Evaluation API for TA2 and a preliminary scenario/probe submission API for TA1 that won't be used in the MVP, and currently lacks an API regarding sending probe responses and receiving alignment scores from TA1.  The API is based on the OpenAPI 3.0 specification.  Some objects and operations are not necessarily planned to be implemented for MVP, but show the direction we are heading.  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Injury(object):
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
        'name': 'str',
        'location': 'str',
        'severity': 'float'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location',
        'severity': 'severity'
    }

    def __init__(self, name=None, location=None, severity=None):  # noqa: E501
        """Injury - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._location = None
        self._severity = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if location is not None:
            self.location = location
        if severity is not None:
            self.severity = severity

    @property
    def name(self):
        """Gets the name of this Injury.  # noqa: E501

        a brief label for the injury  # noqa: E501

        :return: The name of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Injury.

        a brief label for the injury  # noqa: E501

        :param name: The name of this Injury.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def location(self):
        """Gets the location of this Injury.  # noqa: E501

        the injury location on the casualty's body  # noqa: E501

        :return: The location of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Injury.

        the injury location on the casualty's body  # noqa: E501

        :param location: The location of this Injury.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def severity(self):
        """Gets the severity of this Injury.  # noqa: E501

        the apparent severity of the injury from 0 (low) to 1.0 (high)  # noqa: E501

        :return: The severity of this Injury.  # noqa: E501
        :rtype: float
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Injury.

        the apparent severity of the injury from 0 (low) to 1.0 (high)  # noqa: E501

        :param severity: The severity of this Injury.  # noqa: E501
        :type: float
        """

        self._severity = severity

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
        if issubclass(Injury, dict):
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
        if not isinstance(other, Injury):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
