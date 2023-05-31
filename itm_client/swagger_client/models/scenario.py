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

class Scenario(object):
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
        'description': 'str',
        'start_time': 'str',
        'environment': 'Environment',
        'patients': 'list[Patient]',
        'medical_supplies': 'list[MedicalSupply]',
        'triage_categories': 'list[TriageCategory]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'start_time': 'startTime',
        'environment': 'environment',
        'patients': 'patients',
        'medical_supplies': 'medical_supplies',
        'triage_categories': 'triage_categories'
    }

    def __init__(self, id=None, name=None, description=None, start_time=None, environment=None, patients=None, medical_supplies=None, triage_categories=None):  # noqa: E501
        """Scenario - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._start_time = None
        self._environment = None
        self._patients = None
        self._medical_supplies = None
        self._triage_categories = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if environment is not None:
            self.environment = environment
        if patients is not None:
            self.patients = patients
        if medical_supplies is not None:
            self.medical_supplies = medical_supplies
        if triage_categories is not None:
            self.triage_categories = triage_categories

    @property
    def id(self):
        """Gets the id of this Scenario.  # noqa: E501

        a unique id for the scenario  # noqa: E501

        :return: The id of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scenario.

        a unique id for the scenario  # noqa: E501

        :param id: The id of this Scenario.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Scenario.  # noqa: E501

        the scenario name  # noqa: E501

        :return: The name of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Scenario.

        the scenario name  # noqa: E501

        :param name: The name of this Scenario.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Scenario.  # noqa: E501

        a plain text natural language description of the scenario  # noqa: E501

        :return: The description of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Scenario.

        a plain text natural language description of the scenario  # noqa: E501

        :param description: The description of this Scenario.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this Scenario.  # noqa: E501

        the wall clock local start time of the scenario, expressed as hh:mm  # noqa: E501

        :return: The start_time of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Scenario.

        the wall clock local start time of the scenario, expressed as hh:mm  # noqa: E501

        :param start_time: The start_time of this Scenario.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def environment(self):
        """Gets the environment of this Scenario.  # noqa: E501


        :return: The environment of this Scenario.  # noqa: E501
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Scenario.


        :param environment: The environment of this Scenario.  # noqa: E501
        :type: Environment
        """

        self._environment = environment

    @property
    def patients(self):
        """Gets the patients of this Scenario.  # noqa: E501


        :return: The patients of this Scenario.  # noqa: E501
        :rtype: list[Patient]
        """
        return self._patients

    @patients.setter
    def patients(self, patients):
        """Sets the patients of this Scenario.


        :param patients: The patients of this Scenario.  # noqa: E501
        :type: list[Patient]
        """

        self._patients = patients

    @property
    def medical_supplies(self):
        """Gets the medical_supplies of this Scenario.  # noqa: E501


        :return: The medical_supplies of this Scenario.  # noqa: E501
        :rtype: list[MedicalSupply]
        """
        return self._medical_supplies

    @medical_supplies.setter
    def medical_supplies(self, medical_supplies):
        """Sets the medical_supplies of this Scenario.


        :param medical_supplies: The medical_supplies of this Scenario.  # noqa: E501
        :type: list[MedicalSupply]
        """

        self._medical_supplies = medical_supplies

    @property
    def triage_categories(self):
        """Gets the triage_categories of this Scenario.  # noqa: E501


        :return: The triage_categories of this Scenario.  # noqa: E501
        :rtype: list[TriageCategory]
        """
        return self._triage_categories

    @triage_categories.setter
    def triage_categories(self, triage_categories):
        """Sets the triage_categories of this Scenario.


        :param triage_categories: The triage_categories of this Scenario.  # noqa: E501
        :type: list[TriageCategory]
        """

        self._triage_categories = triage_categories

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
        if issubclass(Scenario, dict):
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
        if not isinstance(other, Scenario):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
