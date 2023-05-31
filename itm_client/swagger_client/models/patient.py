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

class Patient(object):
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
        'name': 'str',
        'age': 'int',
        'sex': 'str',
        'injuries': 'list[Injury]',
        'vitals': 'Vitals',
        'mental_status': 'str',
        'assessed': 'bool',
        'tag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'age': 'age',
        'sex': 'sex',
        'injuries': 'injuries',
        'vitals': 'vitals',
        'mental_status': 'mental_status',
        'assessed': 'assessed',
        'tag': 'tag'
    }

    def __init__(self, id=None, name=None, age=None, sex=None, injuries=None, vitals=None, mental_status=None, assessed=None, tag=None):  # noqa: E501
        """Patient - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._age = None
        self._sex = None
        self._injuries = None
        self._vitals = None
        self._mental_status = None
        self._assessed = None
        self._tag = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if sex is not None:
            self.sex = sex
        if injuries is not None:
            self.injuries = injuries
        if vitals is not None:
            self.vitals = vitals
        if mental_status is not None:
            self.mental_status = mental_status
        if assessed is not None:
            self.assessed = assessed
        if tag is not None:
            self.tag = tag

    @property
    def id(self):
        """Gets the id of this Patient.  # noqa: E501

        the patient id, having scenario scope  # noqa: E501

        :return: The id of this Patient.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Patient.

        the patient id, having scenario scope  # noqa: E501

        :param id: The id of this Patient.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Patient.  # noqa: E501

        the name of the patient  # noqa: E501

        :return: The name of this Patient.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Patient.

        the name of the patient  # noqa: E501

        :param name: The name of this Patient.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def age(self):
        """Gets the age of this Patient.  # noqa: E501

        the age of the patient  # noqa: E501

        :return: The age of this Patient.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this Patient.

        the age of the patient  # noqa: E501

        :param age: The age of this Patient.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def sex(self):
        """Gets the sex of this Patient.  # noqa: E501

        the sex of the patient, or unknown  # noqa: E501

        :return: The sex of this Patient.  # noqa: E501
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this Patient.

        the sex of the patient, or unknown  # noqa: E501

        :param sex: The sex of this Patient.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female", "unknown"]  # noqa: E501
        if sex not in allowed_values:
            raise ValueError(
                "Invalid value for `sex` ({0}), must be one of {1}"  # noqa: E501
                .format(sex, allowed_values)
            )

        self._sex = sex

    @property
    def injuries(self):
        """Gets the injuries of this Patient.  # noqa: E501

        an array of patient injuries  # noqa: E501

        :return: The injuries of this Patient.  # noqa: E501
        :rtype: list[Injury]
        """
        return self._injuries

    @injuries.setter
    def injuries(self, injuries):
        """Sets the injuries of this Patient.

        an array of patient injuries  # noqa: E501

        :param injuries: The injuries of this Patient.  # noqa: E501
        :type: list[Injury]
        """

        self._injuries = injuries

    @property
    def vitals(self):
        """Gets the vitals of this Patient.  # noqa: E501


        :return: The vitals of this Patient.  # noqa: E501
        :rtype: Vitals
        """
        return self._vitals

    @vitals.setter
    def vitals(self, vitals):
        """Sets the vitals of this Patient.


        :param vitals: The vitals of this Patient.  # noqa: E501
        :type: Vitals
        """

        self._vitals = vitals

    @property
    def mental_status(self):
        """Gets the mental_status of this Patient.  # noqa: E501

        mood and apparent mental state  # noqa: E501

        :return: The mental_status of this Patient.  # noqa: E501
        :rtype: str
        """
        return self._mental_status

    @mental_status.setter
    def mental_status(self, mental_status):
        """Sets the mental_status of this Patient.

        mood and apparent mental state  # noqa: E501

        :param mental_status: The mental_status of this Patient.  # noqa: E501
        :type: str
        """
        allowed_values = ["calm", "confused", "upset", "agony", "unresponsive"]  # noqa: E501
        if mental_status not in allowed_values:
            raise ValueError(
                "Invalid value for `mental_status` ({0}), must be one of {1}"  # noqa: E501
                .format(mental_status, allowed_values)
            )

        self._mental_status = mental_status

    @property
    def assessed(self):
        """Gets the assessed of this Patient.  # noqa: E501

        whether or not this patient has been assessed in the current scenario  # noqa: E501

        :return: The assessed of this Patient.  # noqa: E501
        :rtype: bool
        """
        return self._assessed

    @assessed.setter
    def assessed(self, assessed):
        """Sets the assessed of this Patient.

        whether or not this patient has been assessed in the current scenario  # noqa: E501

        :param assessed: The assessed of this Patient.  # noqa: E501
        :type: bool
        """

        self._assessed = assessed

    @property
    def tag(self):
        """Gets the tag of this Patient.  # noqa: E501

        the tag assigned to this patient, or none if untagged  # noqa: E501

        :return: The tag of this Patient.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Patient.

        the tag assigned to this patient, or none if untagged  # noqa: E501

        :param tag: The tag of this Patient.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "minimal", "delayed", "immediate", "expectant", "deceased"]  # noqa: E501
        if tag not in allowed_values:
            raise ValueError(
                "Invalid value for `tag` ({0}), must be one of {1}"  # noqa: E501
                .format(tag, allowed_values)
            )

        self._tag = tag

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
        if issubclass(Patient, dict):
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
        if not isinstance(other, Patient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
