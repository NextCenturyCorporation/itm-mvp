# coding: utf-8

"""
    ITM TA3 MVP API

    This is the specification of a proposed TA3 API for the In The Moment (ITM) Minimum Viable Product (MVP).  It is based on the OpenAPI 3.0 specification.  Some objects and operations are not necessarily planned for the MVP, but are currently present for fostering discussion.  The API is currently in an early/draft state, even for an MVP.  # noqa: E501

    OpenAPI spec version: 0.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TriageCategory(object):
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
        'color_tag': 'str',
        'description': 'str',
        'criteria': 'str'
    }

    attribute_map = {
        'color_tag': 'color_tag',
        'description': 'description',
        'criteria': 'criteria'
    }

    def __init__(self, color_tag=None, description=None, criteria=None):  # noqa: E501
        """TriageCategory - a model defined in Swagger"""  # noqa: E501
        self._color_tag = None
        self._description = None
        self._criteria = None
        self.discriminator = None
        if color_tag is not None:
            self.color_tag = color_tag
        if description is not None:
            self.description = description
        if criteria is not None:
            self.criteria = criteria

    @property
    def color_tag(self):
        """Gets the color_tag of this TriageCategory.  # noqa: E501


        :return: The color_tag of this TriageCategory.  # noqa: E501
        :rtype: str
        """
        return self._color_tag

    @color_tag.setter
    def color_tag(self, color_tag):
        """Sets the color_tag of this TriageCategory.


        :param color_tag: The color_tag of this TriageCategory.  # noqa: E501
        :type: str
        """
        allowed_values = ["minimal", "delayed", "immediate", "expectant", "deceased"]  # noqa: E501
        if color_tag not in allowed_values:
            raise ValueError(
                "Invalid value for `color_tag` ({0}), must be one of {1}"  # noqa: E501
                .format(color_tag, allowed_values)
            )

        self._color_tag = color_tag

    @property
    def description(self):
        """Gets the description of this TriageCategory.  # noqa: E501

        a one-line description of the color_tag category  # noqa: E501

        :return: The description of this TriageCategory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TriageCategory.

        a one-line description of the color_tag category  # noqa: E501

        :param description: The description of this TriageCategory.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def criteria(self):
        """Gets the criteria of this TriageCategory.  # noqa: E501

        detailed criteria for the color_tag category  # noqa: E501

        :return: The criteria of this TriageCategory.  # noqa: E501
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this TriageCategory.

        detailed criteria for the color_tag category  # noqa: E501

        :param criteria: The criteria of this TriageCategory.  # noqa: E501
        :type: str
        """

        self._criteria = criteria

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
        if issubclass(TriageCategory, dict):
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
        if not isinstance(other, TriageCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
