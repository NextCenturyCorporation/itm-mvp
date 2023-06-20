# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.demographics import Demographics  # noqa: F401,E501
from swagger_server.models.injury import Injury  # noqa: F401,E501
from swagger_server.models.vitals import Vitals  # noqa: F401,E501
from swagger_server import util


class Casualty(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, unstructured: str=None, name: str=None, demographics: Demographics=None, injuries: List[Injury]=None, vitals: Vitals=None, mental_status: str=None, assessed: bool=False, tag: str=None):  # noqa: E501
        """Casualty - a model defined in Swagger

        :param id: The id of this Casualty.  # noqa: E501
        :type id: str
        :param unstructured: The unstructured of this Casualty.  # noqa: E501
        :type unstructured: str
        :param name: The name of this Casualty.  # noqa: E501
        :type name: str
        :param demographics: The demographics of this Casualty.  # noqa: E501
        :type demographics: Demographics
        :param injuries: The injuries of this Casualty.  # noqa: E501
        :type injuries: List[Injury]
        :param vitals: The vitals of this Casualty.  # noqa: E501
        :type vitals: Vitals
        :param mental_status: The mental_status of this Casualty.  # noqa: E501
        :type mental_status: str
        :param assessed: The assessed of this Casualty.  # noqa: E501
        :type assessed: bool
        :param tag: The tag of this Casualty.  # noqa: E501
        :type tag: str
        """
        self.swagger_types = {
            'id': str,
            'unstructured': str,
            'name': str,
            'demographics': Demographics,
            'injuries': List[Injury],
            'vitals': Vitals,
            'mental_status': str,
            'assessed': bool,
            'tag': str
        }

        self.attribute_map = {
            'id': 'id',
            'unstructured': 'unstructured',
            'name': 'name',
            'demographics': 'demographics',
            'injuries': 'injuries',
            'vitals': 'vitals',
            'mental_status': 'mental_status',
            'assessed': 'assessed',
            'tag': 'tag'
        }
        self._id = id
        self._unstructured = unstructured
        self._name = name
        self._demographics = demographics
        self._injuries = injuries
        self._vitals = vitals
        self._mental_status = mental_status
        self._assessed = assessed
        self._tag = tag

    @classmethod
    def from_dict(cls, dikt) -> 'Casualty':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Casualty of this Casualty.  # noqa: E501
        :rtype: Casualty
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Casualty.

        string, globally unique casualty identifier  # noqa: E501

        :return: The id of this Casualty.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Casualty.

        string, globally unique casualty identifier  # noqa: E501

        :param id: The id of this Casualty.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def unstructured(self) -> str:
        """Gets the unstructured of this Casualty.

        natural language text description of the casualty  # noqa: E501

        :return: The unstructured of this Casualty.
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured: str):
        """Sets the unstructured of this Casualty.

        natural language text description of the casualty  # noqa: E501

        :param unstructured: The unstructured of this Casualty.
        :type unstructured: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def name(self) -> str:
        """Gets the name of this Casualty.

        the name of the casualty, omit if unknown  # noqa: E501

        :return: The name of this Casualty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Casualty.

        the name of the casualty, omit if unknown  # noqa: E501

        :param name: The name of this Casualty.
        :type name: str
        """

        self._name = name

    @property
    def demographics(self) -> Demographics:
        """Gets the demographics of this Casualty.


        :return: The demographics of this Casualty.
        :rtype: Demographics
        """
        return self._demographics

    @demographics.setter
    def demographics(self, demographics: Demographics):
        """Sets the demographics of this Casualty.


        :param demographics: The demographics of this Casualty.
        :type demographics: Demographics
        """

        self._demographics = demographics

    @property
    def injuries(self) -> List[Injury]:
        """Gets the injuries of this Casualty.

        an array of casualty injuries  # noqa: E501

        :return: The injuries of this Casualty.
        :rtype: List[Injury]
        """
        return self._injuries

    @injuries.setter
    def injuries(self, injuries: List[Injury]):
        """Sets the injuries of this Casualty.

        an array of casualty injuries  # noqa: E501

        :param injuries: The injuries of this Casualty.
        :type injuries: List[Injury]
        """

        self._injuries = injuries

    @property
    def vitals(self) -> Vitals:
        """Gets the vitals of this Casualty.


        :return: The vitals of this Casualty.
        :rtype: Vitals
        """
        return self._vitals

    @vitals.setter
    def vitals(self, vitals: Vitals):
        """Sets the vitals of this Casualty.


        :param vitals: The vitals of this Casualty.
        :type vitals: Vitals
        """

        self._vitals = vitals

    @property
    def mental_status(self) -> str:
        """Gets the mental_status of this Casualty.

        mood and apparent mental state, omit if unknown  # noqa: E501

        :return: The mental_status of this Casualty.
        :rtype: str
        """
        return self._mental_status

    @mental_status.setter
    def mental_status(self, mental_status: str):
        """Sets the mental_status of this Casualty.

        mood and apparent mental state, omit if unknown  # noqa: E501

        :param mental_status: The mental_status of this Casualty.
        :type mental_status: str
        """
        allowed_values = ["calm", "confused", "upset", "agony", "unresponsive"]  # noqa: E501
        if mental_status not in allowed_values:
            raise ValueError(
                "Invalid value for `mental_status` ({0}), must be one of {1}"
                .format(mental_status, allowed_values)
            )

        self._mental_status = mental_status

    @property
    def assessed(self) -> bool:
        """Gets the assessed of this Casualty.

        whether or not this casualty has been assessed in the current scenario  # noqa: E501

        :return: The assessed of this Casualty.
        :rtype: bool
        """
        return self._assessed

    @assessed.setter
    def assessed(self, assessed: bool):
        """Sets the assessed of this Casualty.

        whether or not this casualty has been assessed in the current scenario  # noqa: E501

        :param assessed: The assessed of this Casualty.
        :type assessed: bool
        """

        self._assessed = assessed

    @property
    def tag(self) -> str:
        """Gets the tag of this Casualty.

        the tag assigned to this casualty, omit if untagged  # noqa: E501

        :return: The tag of this Casualty.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag: str):
        """Sets the tag of this Casualty.

        the tag assigned to this casualty, omit if untagged  # noqa: E501

        :param tag: The tag of this Casualty.
        :type tag: str
        """
        allowed_values = ["minimal", "delayed", "immediate", "expectant", "deceased"]  # noqa: E501
        if tag not in allowed_values:
            raise ValueError(
                "Invalid value for `tag` ({0}), must be one of {1}"
                .format(tag, allowed_values)
            )

        self._tag = tag
