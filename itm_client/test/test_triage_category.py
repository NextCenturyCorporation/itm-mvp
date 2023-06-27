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
from swagger_client.models.triage_category import TriageCategory  # noqa: E501
from swagger_client.rest import ApiException


class TestTriageCategory(unittest.TestCase):
    """TriageCategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTriageCategory(self):
        """Test TriageCategory"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.triage_category.TriageCategory()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
