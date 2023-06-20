# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.probe import Probe  # noqa: E501
from swagger_server.models.scenario import Scenario  # noqa: E501
from swagger_server.test import BaseTestCase


class TestItmTa1Ta3Controller(BaseTestCase):
    """ItmTa1Ta3Controller integration test stubs"""

    def test_add_probe(self):
        """Test case for add_probe

        Create a new evaluation probe
        """
        body = Probe()
        query_string = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/ta1/probe/{scenarioId}'.format(scenario_id='scenario_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_scenario(self):
        """Test case for add_scenario

        Create a new evaluation scenario
        """
        body = Scenario()
        query_string = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/ta1/scenario',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_probe(self):
        """Test case for delete_probe

        Delete an evaluation probe
        """
        query_string = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/ta1/probe/{probeId}'.format(probe_id='probe_id_example'),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_scenario(self):
        """Test case for delete_scenario

        Delete an evaluation scenario
        """
        query_string = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/ta1/scenario/{scenarioId}'.format(scenario_id='scenario_id_example'),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ta1login(self):
        """Test case for ta1login

        Log in with TA3
        """
        query_string = [('username', 'username_example')]
        response = self.client.open(
            '/ta1/login',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_probe(self):
        """Test case for update_probe

        Update an existing evaluation probe
        """
        body = Probe()
        query_string = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/ta1/probe',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_scenario(self):
        """Test case for update_scenario

        Update an existing evaluation scenario
        """
        body = Scenario()
        query_string = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/ta1/scenario',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
