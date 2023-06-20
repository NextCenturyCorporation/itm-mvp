# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Demographics(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, age: int=None, sex: str=None, rank: str=None):  # noqa: E501
        """Demographics - a model defined in Swagger

        :param age: The age of this Demographics.  # noqa: E501
        :type age: int
        :param sex: The sex of this Demographics.  # noqa: E501
        :type sex: str
        :param rank: The rank of this Demographics.  # noqa: E501
        :type rank: str
        """
        self.swagger_types = {
            'age': int,
            'sex': str,
            'rank': str
        }

        self.attribute_map = {
            'age': 'age',
            'sex': 'sex',
            'rank': 'rank'
        }
        self._age = age
        self._sex = sex
        self._rank = rank

    @classmethod
    def from_dict(cls, dikt) -> 'Demographics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Demographics of this Demographics.  # noqa: E501
        :rtype: Demographics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def age(self) -> int:
        """Gets the age of this Demographics.

        the age of the casualty, omit if unknown  # noqa: E501

        :return: The age of this Demographics.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this Demographics.

        the age of the casualty, omit if unknown  # noqa: E501

        :param age: The age of this Demographics.
        :type age: int
        """

        self._age = age

    @property
    def sex(self) -> str:
        """Gets the sex of this Demographics.

        the sex of the casualty, omit if unknown/indeterminate  # noqa: E501

        :return: The sex of this Demographics.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex: str):
        """Sets the sex of this Demographics.

        the sex of the casualty, omit if unknown/indeterminate  # noqa: E501

        :param sex: The sex of this Demographics.
        :type sex: str
        """
        allowed_values = ["male", "female"]  # noqa: E501
        if sex not in allowed_values:
            raise ValueError(
                "Invalid value for `sex` ({0}), must be one of {1}"
                .format(sex, allowed_values)
            )

        self._sex = sex

    @property
    def rank(self) -> str:
        """Gets the rank of this Demographics.

        The military status of the casualty, omit if unknown  # noqa: E501

        :return: The rank of this Demographics.
        :rtype: str
        """
        return self._rank

    @rank.setter
    def rank(self, rank: str):
        """Sets the rank of this Demographics.

        The military status of the casualty, omit if unknown  # noqa: E501

        :param rank: The rank of this Demographics.
        :type rank: str
        """
        allowed_values = ["Military", "Enemy", "Civilian", "VIP"]  # noqa: E501
        if rank not in allowed_values:
            raise ValueError(
                "Invalid value for `rank` ({0}), must be one of {1}"
                .format(rank, allowed_values)
            )

        self._rank = rank