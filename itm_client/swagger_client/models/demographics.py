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

class Demographics(object):
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
        'age': 'int',
        'sex': 'str',
        'rank': 'str'
    }

    attribute_map = {
        'age': 'age',
        'sex': 'sex',
        'rank': 'rank'
    }

    def __init__(self, age=None, sex=None, rank=None):  # noqa: E501
        """Demographics - a model defined in Swagger"""  # noqa: E501
        self._age = None
        self._sex = None
        self._rank = None
        self.discriminator = None
        if age is not None:
            self.age = age
        if sex is not None:
            self.sex = sex
        if rank is not None:
            self.rank = rank

    @property
    def age(self):
        """Gets the age of this Demographics.  # noqa: E501

        the age of the casualty, omit if unknown  # noqa: E501

        :return: The age of this Demographics.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this Demographics.

        the age of the casualty, omit if unknown  # noqa: E501

        :param age: The age of this Demographics.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def sex(self):
        """Gets the sex of this Demographics.  # noqa: E501

        the sex of the casualty, omit if unknown/indeterminate  # noqa: E501

        :return: The sex of this Demographics.  # noqa: E501
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this Demographics.

        the sex of the casualty, omit if unknown/indeterminate  # noqa: E501

        :param sex: The sex of this Demographics.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female"]  # noqa: E501
        if sex not in allowed_values:
            raise ValueError(
                "Invalid value for `sex` ({0}), must be one of {1}"  # noqa: E501
                .format(sex, allowed_values)
            )

        self._sex = sex

    @property
    def rank(self):
        """Gets the rank of this Demographics.  # noqa: E501

        The military status of the casualty, omit if unknown  # noqa: E501

        :return: The rank of this Demographics.  # noqa: E501
        :rtype: str
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this Demographics.

        The military status of the casualty, omit if unknown  # noqa: E501

        :param rank: The rank of this Demographics.  # noqa: E501
        :type: str
        """
        allowed_values = ["Military", "Enemy", "Civilian", "VIP"]  # noqa: E501
        if rank not in allowed_values:
            raise ValueError(
                "Invalid value for `rank` ({0}), must be one of {1}"  # noqa: E501
                .format(rank, allowed_values)
            )

        self._rank = rank

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
        if issubclass(Demographics, dict):
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
        if not isinstance(other, Demographics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
