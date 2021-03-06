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
from swagger_client.api.devices_api import DevicesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_asset_filtered_get(self):
        """Test case for device_asset_filtered_get

        Gets a list of assets  # noqa: E501
        """
        pass

    def test_device_asset_get(self):
        """Test case for device_asset_get

        Gets a list of assets  # noqa: E501
        """
        pass

    def test_device_asset_read(self):
        """Test case for device_asset_read

        Reads asset channel values  # noqa: E501
        """
        pass

    def test_device_asset_write(self):
        """Test case for device_asset_write

        Gets a list of assets  # noqa: E501
        """
        pass

    def test_device_bundle_get(self):
        """Test case for device_bundle_get

        Gets a list of bundles  # noqa: E501
        """
        pass

    def test_device_bundle_start(self):
        """Test case for device_bundle_start

        Start a bundle  # noqa: E501
        """
        pass

    def test_device_bundle_stop(self):
        """Test case for device_bundle_stop

        Stop a bundle  # noqa: E501
        """
        pass

    def test_device_command_execute(self):
        """Test case for device_command_execute

        Executes a command  # noqa: E501
        """
        pass

    def test_device_configuration_component_get(self):
        """Test case for device_configuration_component_get

        Gets the configuration of a component on a device  # noqa: E501
        """
        pass

    def test_device_configuration_component_update(self):
        """Test case for device_configuration_component_update

        Updates the configuration of a component on a device  # noqa: E501
        """
        pass

    def test_device_configuration_get(self):
        """Test case for device_configuration_get

        Gets the device configurations  # noqa: E501
        """
        pass

    def test_device_configuration_update(self):
        """Test case for device_configuration_update

        Updates a device configuration  # noqa: E501
        """
        pass

    def test_device_count(self):
        """Test case for device_count

        Counts the Devices  # noqa: E501
        """
        pass

    def test_device_create(self):
        """Test case for device_create

        Create an Device  # noqa: E501
        """
        pass

    def test_device_delete(self):
        """Test case for device_delete

        Delete a Device  # noqa: E501
        """
        pass

    def test_device_event_count(self):
        """Test case for device_event_count

        Counts the DeviceEvents  # noqa: E501
        """
        pass

    def test_device_event_delete(self):
        """Test case for device_event_delete

        Delete a DeviceEvent  # noqa: E501
        """
        pass

    def test_device_event_find(self):
        """Test case for device_event_find

        Get an DeviceEvent  # noqa: E501
        """
        pass

    def test_device_event_query(self):
        """Test case for device_event_query

        Queries the DeviceEvents  # noqa: E501
        """
        pass

    def test_device_event_simple_query(self):
        """Test case for device_event_simple_query

        Gets the DeviceEvent list in the scope  # noqa: E501
        """
        pass

    def test_device_find(self):
        """Test case for device_find

        Get a Device  # noqa: E501
        """
        pass

    def test_device_package_download(self):
        """Test case for device_package_download

        Installs a package  # noqa: E501
        """
        pass

    def test_device_package_get(self):
        """Test case for device_package_get

        Gets a list of packages  # noqa: E501
        """
        pass

    def test_device_package_uninstall(self):
        """Test case for device_package_uninstall

        Uninstalls a package  # noqa: E501
        """
        pass

    def test_device_query(self):
        """Test case for device_query

        Queries the Devices  # noqa: E501
        """
        pass

    def test_device_request_send(self):
        """Test case for device_request_send

        Sends a request  # noqa: E501
        """
        pass

    def test_device_simple_query(self):
        """Test case for device_simple_query

        Gets the Device list in the scope  # noqa: E501
        """
        pass

    def test_device_snapshot_get(self):
        """Test case for device_snapshot_get

        Gets a list of snapshots  # noqa: E501
        """
        pass

    def test_device_snapshot_rollback(self):
        """Test case for device_snapshot_rollback

        Gets a list of snapshots  # noqa: E501
        """
        pass

    def test_device_update(self):
        """Test case for device_update

        Update a Device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
