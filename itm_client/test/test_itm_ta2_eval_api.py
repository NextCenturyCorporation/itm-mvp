# coding: utf-8

"""
    ITM MVP TA3 API

    This is the specification of a proposed TA3 API for the In The Moment (ITM) Minimum Viable Product (MVP).  Currently, there is an Evaluation API for TA2 and a preliminary scenario/probe submission API for TA1 that won't be used in the MVP, and currently lacks an API regarding sending probe responses and receiving alignment scores from TA1.  The API is based on the OpenAPI 3.0 specification.  Some aspects of this API are not necessarily planned to be implemented for MVP, but show the direction we are heading.  # noqa: E501

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.itm_ta2_eval_api import ItmTa2EvalApi  # noqa: E501
from swagger_client.rest import ApiException


class TestItmTa2EvalApi(unittest.TestCase):
    """ItmTa2EvalApi unit test stubs"""

    def setUp(self):
        self.api = ItmTa2EvalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_vitals(self):
        """Test case for check_vitals

        Assess and retrieve all casualty vital signs  # noqa: E501
        """
        pass

    def test_get_alignment_target(self):
        """Test case for get_alignment_target

        Retrieve alignment target for the scenario  # noqa: E501
        """
        pass

    def test_get_heart_rate(self):
        """Test case for get_heart_rate

        Check casualty heart rate  # noqa: E501
        """
        pass

    def test_get_probe(self):
        """Test case for get_probe

        Request a probe  # noqa: E501
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

        Get the next scenario  # noqa: E501
        """
        pass

    def test_start_session(self):
        """Test case for start_session

        Start a new session  # noqa: E501
        """
        pass

    def test_tag_casualty(self):
        """Test case for tag_casualty

        Tag a casualty with a triage category  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
