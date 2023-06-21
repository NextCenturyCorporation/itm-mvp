# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Mission(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, unstructured: str=None, mission_type: str=None):  # noqa: E501
        """Mission - a model defined in Swagger

        :param unstructured: The unstructured of this Mission.  # noqa: E501
        :type unstructured: str
        :param mission_type: The mission_type of this Mission.  # noqa: E501
        :type mission_type: str
        """
        self.swagger_types = {
            'unstructured': str,
            'mission_type': str
        }

        self.attribute_map = {
            'unstructured': 'unstructured',
            'mission_type': 'mission_type'
        }
        self._unstructured = unstructured
        self._mission_type = mission_type

    @classmethod
    def from_dict(cls, dikt) -> 'Mission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Mission of this Mission.  # noqa: E501
        :rtype: Mission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unstructured(self) -> str:
        """Gets the unstructured of this Mission.

        natural language description of current mission  # noqa: E501

        :return: The unstructured of this Mission.
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured: str):
        """Sets the unstructured of this Mission.

        natural language description of current mission  # noqa: E501

        :param unstructured: The unstructured of this Mission.
        :type unstructured: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def mission_type(self) -> str:
        """Gets the mission_type of this Mission.

        enum of possible mission types; only ProtectVIP is supported for MVP  # noqa: E501

        :return: The mission_type of this Mission.
        :rtype: str
        """
        return self._mission_type

    @mission_type.setter
    def mission_type(self, mission_type: str):
        """Sets the mission_type of this Mission.

        enum of possible mission types; only ProtectVIP is supported for MVP  # noqa: E501

        :param mission_type: The mission_type of this Mission.
        :type mission_type: str
        """
        allowed_values = ["ProtectVIP", "DeliverCargo", "DefendBase"]  # noqa: E501
        if mission_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mission_type` ({0}), must be one of {1}"
                .format(mission_type, allowed_values)
            )

        self._mission_type = mission_type
