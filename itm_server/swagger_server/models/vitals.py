# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Vitals(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, hrpmin: int=None, mm_hg: int=None, rr: int=None, sp_o2: int=None, pain: int=None):  # noqa: E501
        """Vitals - a model defined in Swagger

        :param hrpmin: The hrpmin of this Vitals.  # noqa: E501
        :type hrpmin: int
        :param mm_hg: The mm_hg of this Vitals.  # noqa: E501
        :type mm_hg: int
        :param rr: The rr of this Vitals.  # noqa: E501
        :type rr: int
        :param sp_o2: The sp_o2 of this Vitals.  # noqa: E501
        :type sp_o2: int
        :param pain: The pain of this Vitals.  # noqa: E501
        :type pain: int
        """
        self.swagger_types = {
            'hrpmin': int,
            'mm_hg': int,
            'rr': int,
            'sp_o2': int,
            'pain': int
        }

        self.attribute_map = {
            'hrpmin': 'hrpmin',
            'mm_hg': 'mmHg',
            'rr': 'RR',
            'sp_o2': 'SpO2%',
            'pain': 'pain'
        }
        self._hrpmin = hrpmin
        self._mm_hg = mm_hg
        self._rr = rr
        self._sp_o2 = sp_o2
        self._pain = pain

    @classmethod
    def from_dict(cls, dikt) -> 'Vitals':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Vitals of this Vitals.  # noqa: E501
        :rtype: Vitals
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hrpmin(self) -> int:
        """Gets the hrpmin of this Vitals.

        heart rate in beats per minute  # noqa: E501

        :return: The hrpmin of this Vitals.
        :rtype: int
        """
        return self._hrpmin

    @hrpmin.setter
    def hrpmin(self, hrpmin: int):
        """Sets the hrpmin of this Vitals.

        heart rate in beats per minute  # noqa: E501

        :param hrpmin: The hrpmin of this Vitals.
        :type hrpmin: int
        """

        self._hrpmin = hrpmin

    @property
    def mm_hg(self) -> int:
        """Gets the mm_hg of this Vitals.

        blood pressure in mmHg  # noqa: E501

        :return: The mm_hg of this Vitals.
        :rtype: int
        """
        return self._mm_hg

    @mm_hg.setter
    def mm_hg(self, mm_hg: int):
        """Sets the mm_hg of this Vitals.

        blood pressure in mmHg  # noqa: E501

        :param mm_hg: The mm_hg of this Vitals.
        :type mm_hg: int
        """

        self._mm_hg = mm_hg

    @property
    def rr(self) -> int:
        """Gets the rr of this Vitals.

        respiratory rate in breaths/minute  # noqa: E501

        :return: The rr of this Vitals.
        :rtype: int
        """
        return self._rr

    @rr.setter
    def rr(self, rr: int):
        """Sets the rr of this Vitals.

        respiratory rate in breaths/minute  # noqa: E501

        :param rr: The rr of this Vitals.
        :type rr: int
        """

        self._rr = rr

    @property
    def sp_o2(self) -> int:
        """Gets the sp_o2 of this Vitals.

        Oxygen saturation level, expressed as a percentage  # noqa: E501

        :return: The sp_o2 of this Vitals.
        :rtype: int
        """
        return self._sp_o2

    @sp_o2.setter
    def sp_o2(self, sp_o2: int):
        """Sets the sp_o2 of this Vitals.

        Oxygen saturation level, expressed as a percentage  # noqa: E501

        :param sp_o2: The sp_o2 of this Vitals.
        :type sp_o2: int
        """

        self._sp_o2 = sp_o2

    @property
    def pain(self) -> int:
        """Gets the pain of this Vitals.

        1-10 scale, omit if unknown or unconscious  # noqa: E501

        :return: The pain of this Vitals.
        :rtype: int
        """
        return self._pain

    @pain.setter
    def pain(self, pain: int):
        """Sets the pain of this Vitals.

        1-10 scale, omit if unknown or unconscious  # noqa: E501

        :param pain: The pain of this Vitals.
        :type pain: int
        """

        self._pain = pain
