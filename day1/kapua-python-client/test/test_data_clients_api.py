# coding: utf-8

"""
    Eclipse Kapua REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.data_clients_api import DataClientsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDataClientsApi(unittest.TestCase):
    """DataClientsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.data_clients_api.DataClientsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_data_client_count(self):
        """Test case for data_client_count

        Counts the ClientInfos  # noqa: E501
        """
        pass

    def test_data_client_find(self):
        """Test case for data_client_find

        Gets an ClientInfo  # noqa: E501
        """
        pass

    def test_data_client_query(self):
        """Test case for data_client_query

        Queries the ClientInfos  # noqa: E501
        """
        pass

    def test_data_client_simple_query(self):
        """Test case for data_client_simple_query

        Gets the ClientInfo list in the scope  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
