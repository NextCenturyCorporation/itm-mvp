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
from swagger_client.api.itm_ta1_ta3_api import ItmTa1Ta3Api  # noqa: E501
from swagger_client.rest import ApiException


class TestItmTa1Ta3Api(unittest.TestCase):
    """ItmTa1Ta3Api unit test stubs"""

    def setUp(self):
        self.api = ItmTa1Ta3Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_probe(self):
        """Test case for add_probe

        Create a new evaluation probe  # noqa: E501
        """
        pass

    def test_add_scenario(self):
        """Test case for add_scenario

        Create a new evaluation scenario  # noqa: E501
        """
        pass

    def test_delete_probe(self):
        """Test case for delete_probe

        Delete an evaluation probe  # noqa: E501
        """
        pass

    def test_delete_scenario(self):
        """Test case for delete_scenario

        Delete an evaluation scenario  # noqa: E501
        """
        pass

    def test_ta1login(self):
        """Test case for ta1login

        Log in with TA3  # noqa: E501
        """
        pass

    def test_update_probe(self):
        """Test case for update_probe

        Update an existing evaluation probe  # noqa: E501
        """
        pass

    def test_update_scenario(self):
        """Test case for update_scenario

        Update an existing evaluation scenario  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
