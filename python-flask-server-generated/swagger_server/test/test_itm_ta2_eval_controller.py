# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.alignment_target import AlignmentTarget  # noqa: E501
from swagger_server.models.probe import Probe  # noqa: E501
from swagger_server.models.probe_response import ProbeResponse  # noqa: E501
from swagger_server.models.scenario import Scenario  # noqa: E501
from swagger_server.models.state import State  # noqa: E501
from swagger_server.models.vitals import Vitals  # noqa: E501
from swagger_server.test import BaseTestCase


class TestItmTa2EvalController(BaseTestCase):
    """ItmTa2EvalController integration test stubs"""

    def test_check_vitals(self):
        """Test case for check_vitals

        Assess and retrieve all casualty vital signs
        """
        response = self.client.open(
            '/ta2/casualty/{casualty_id}/checkVitals'.format(casualty_id='casualty_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_alignment_target(self):
        """Test case for get_alignment_target

        Retrieve alignment target for the scenario
        """
        response = self.client.open(
            '/ta2/{scenario_id}/getAlignmentTarget'.format(scenario_id='scenario_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_heart_rate(self):
        """Test case for get_heart_rate

        Check casualty heart rate
        """
        response = self.client.open(
            '/ta2/casualty/{casualty_id}/checkHeartRate'.format(casualty_id='casualty_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_probe(self):
        """Test case for get_probe

        Request a probe
        """
        query_string = [('scenario_id', 'scenario_id_example')]
        response = self.client.open(
            '/ta2/probe',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_scenario_state(self):
        """Test case for get_scenario_state

        Retrieve scenario state
        """
        response = self.client.open(
            '/ta2/{scenario_id}/getState'.format(scenario_id='scenario_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_respond_to_probe(self):
        """Test case for respond_to_probe

        Respond to a probe
        """
        body = ProbeResponse()
        response = self.client.open(
            '/ta2/probe',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_scenario(self):
        """Test case for start_scenario

        Start a new scenario
        """
        query_string = [('adm_name', 'adm_name_example')]
        response = self.client.open(
            '/ta2/start',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tag_casualty(self):
        """Test case for tag_casualty

        Tag a casualty with a triage category
        """
        query_string = [('tag', 'tag_example')]
        response = self.client.open(
            '/ta2/casualty/{casualty_id}/tag'.format(casualty_id='casualty_id_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
