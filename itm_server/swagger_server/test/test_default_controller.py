# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.probe import Probe  # noqa: E501
from swagger_server.models.scenario import Scenario  # noqa: E501
from swagger_server.models.scenario_state import ScenarioState  # noqa: E501
from swagger_server.models.vitals import Vitals  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_patient_heart_rate(self):
        """Test case for get_patient_heart_rate

        Retrieve patient heart rate
        """
        query_string = [('scenario_id', 'scenario_id_example'),
                        ('patient_id', 'patient_id_example')]
        response = self.client.open(
            '/patient/getHeartRate',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_patient_vitals(self):
        """Test case for get_patient_vitals

        Retrieve all patient vital signs
        """
        query_string = [('scenario_id', 'scenario_id_example'),
                        ('patient_id', 'patient_id_example')]
        response = self.client.open(
            '/patient/getVitals',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_probe(self):
        """Test case for get_probe

        Request the next probe
        """
        query_string = [('scenario_id', 'scenario_id_example')]
        response = self.client.open(
            '/scenario/probe',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_scenario_state(self):
        """Test case for get_scenario_state

        Retrieve scenario state
        """
        query_string = [('scenario_id', 'scenario_id_example')]
        response = self.client.open(
            '/scenario/getState',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_respond_to_probe(self):
        """Test case for respond_to_probe

        Respond to a probe
        """
        query_string = [('probe_id', 'probe_id_example'),
                        ('patient_id', 'patient_id_example'),
                        ('explanation', 'explanation_example')]
        response = self.client.open(
            '/scenario/probe',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_scenario(self):
        """Test case for start_scenario

        Start a new scenario
        """
        query_string = [('username', 'username_example')]
        response = self.client.open(
            '/scenario/start',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
