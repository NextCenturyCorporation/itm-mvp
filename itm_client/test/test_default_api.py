# coding: utf-8

"""
    ITM TA3 MVP API

    This is the specification of a proposed TA3 API for the In The Moment (ITM) Minimum Viable Product (MVP).  It is based on the OpenAPI 3.0 specification.  Some objects and operations are not necessarily planned for the MVP, but are currently present for fostering discussion.  The API is currently in an early/draft state, even for an MVP.  # noqa: E501

    OpenAPI spec version: 0.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_patient_heart_rate(self):
        """Test case for get_patient_heart_rate

        Retrieve patient heart rate  # noqa: E501
        """
        pass

    def test_get_patient_vitals(self):
        """Test case for get_patient_vitals

        Retrieve all patient vital signs  # noqa: E501
        """
        pass

    def test_get_probe(self):
        """Test case for get_probe

        Request the next probe  # noqa: E501
        """
        pass

    def test_get_scenario_state(self):
        """Test case for get_scenario_state

        Retrieve scenario state  # noqa: E501
        """
        pass

    def test_respond_to_probe(self):
        """Test case for respond_to_probe

        Respond to a probe  # noqa: E501
        """
        pass

    def test_start_scenario(self):
        """Test case for start_scenario

        Start a new scenario  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
