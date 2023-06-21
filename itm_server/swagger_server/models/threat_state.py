# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.threat import Threat  # noqa: F401,E501
from swagger_server import util


class ThreatState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, unstructured: str=None, threats: List[Threat]=None):  # noqa: E501
        """ThreatState - a model defined in Swagger

        :param unstructured: The unstructured of this ThreatState.  # noqa: E501
        :type unstructured: str
        :param threats: The threats of this ThreatState.  # noqa: E501
        :type threats: List[Threat]
        """
        self.swagger_types = {
            'unstructured': str,
            'threats': List[Threat]
        }

        self.attribute_map = {
            'unstructured': 'unstructured',
            'threats': 'threats'
        }
        self._unstructured = unstructured
        self._threats = threats

    @classmethod
    def from_dict(cls, dikt) -> 'ThreatState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ThreatState of this ThreatState.  # noqa: E501
        :rtype: ThreatState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unstructured(self) -> str:
        """Gets the unstructured of this ThreatState.

        text description of current threat state  # noqa: E501

        :return: The unstructured of this ThreatState.
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured: str):
        """Sets the unstructured of this ThreatState.

        text description of current threat state  # noqa: E501

        :param unstructured: The unstructured of this ThreatState.
        :type unstructured: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def threats(self) -> List[Threat]:
        """Gets the threats of this ThreatState.

        An array of threats  # noqa: E501

        :return: The threats of this ThreatState.
        :rtype: List[Threat]
        """
        return self._threats

    @threats.setter
    def threats(self, threats: List[Threat]):
        """Sets the threats of this ThreatState.

        An array of threats  # noqa: E501

        :param threats: The threats of this ThreatState.
        :type threats: List[Threat]
        """

        self._threats = threats
