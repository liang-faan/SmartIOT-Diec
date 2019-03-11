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
from swagger_client.api.endpoint_infos_api import EndpointInfosApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEndpointInfosApi(unittest.TestCase):
    """EndpointInfosApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.endpoint_infos_api.EndpointInfosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_endpoint_info(self):
        """Test case for create_endpoint_info

        Create a EndpointInfo  # noqa: E501
        """
        pass

    def test_endpoint_info_count(self):
        """Test case for endpoint_info_count

        Counts the EndpointInfos  # noqa: E501
        """
        pass

    def test_endpoint_info_delete(self):
        """Test case for endpoint_info_delete

        Delete an EndpointInfo  # noqa: E501
        """
        pass

    def test_endpoint_info_find(self):
        """Test case for endpoint_info_find

        Get a EndpointInfo  # noqa: E501
        """
        pass

    def test_endpoint_info_query(self):
        """Test case for endpoint_info_query

        Queries the EndpointInfos  # noqa: E501
        """
        pass

    def test_endpoint_info_simple_query(self):
        """Test case for endpoint_info_simple_query

        Gets the EndpointInfo list in the scope  # noqa: E501
        """
        pass

    def test_endpoint_info_update(self):
        """Test case for endpoint_info_update

        Update a EndpointInfo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
