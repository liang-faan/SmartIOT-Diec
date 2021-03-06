# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: kapuaAccessToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.AccessInfoQuery() # AccessInfoQuery | The AccessInfoQuery to use to filter count results

try:
    # Counts the AccessInfos
    api_response = api_instance.access_info_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_info_count: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessInfoApi* | [**access_info_count**](docs/AccessInfoApi.md#access_info_count) | **POST** /{scopeId}/accessinfos/_count | Counts the AccessInfos
*AccessInfoApi* | [**access_info_create**](docs/AccessInfoApi.md#access_info_create) | **POST** /{scopeId}/accessinfos | Creates a new AccessInfo
*AccessInfoApi* | [**access_info_delete**](docs/AccessInfoApi.md#access_info_delete) | **DELETE** /{scopeId}/accessinfos/{accessInfoId} | Deletes an AccessInfo
*AccessInfoApi* | [**access_info_find**](docs/AccessInfoApi.md#access_info_find) | **GET** /{scopeId}/accessinfos/{accessInfoId} | Gets an AccessInfo
*AccessInfoApi* | [**access_info_query**](docs/AccessInfoApi.md#access_info_query) | **POST** /{scopeId}/accessinfos/_query | Queries the AccessInfos
*AccessInfoApi* | [**access_info_simple_query**](docs/AccessInfoApi.md#access_info_simple_query) | **GET** /{scopeId}/accessinfos | Gets the AccessInfo list in the scope.
*AccessInfoApi* | [**access_permission_count**](docs/AccessInfoApi.md#access_permission_count) | **POST** /{scopeId}/accessinfos/{accessInfoId}/permissions/_count | Counts the AccessPermissions
*AccessInfoApi* | [**access_permission_create**](docs/AccessInfoApi.md#access_permission_create) | **POST** /{scopeId}/accessinfos/{accessInfoId}/permissions | Create an AccessPermission
*AccessInfoApi* | [**access_permission_delete**](docs/AccessInfoApi.md#access_permission_delete) | **DELETE** /{scopeId}/accessinfos/{accessInfoId}/permissions/{accessPermissionId} | Delete an AccessPermission
*AccessInfoApi* | [**access_permission_find**](docs/AccessInfoApi.md#access_permission_find) | **GET** /{scopeId}/accessinfos/{accessInfoId}/permissions/{accessPermissionId} | Get an AccessPermission
*AccessInfoApi* | [**access_permission_query**](docs/AccessInfoApi.md#access_permission_query) | **POST** /{scopeId}/accessinfos/{accessInfoId}/permissions/_query | Queries the AccessPermissions
*AccessInfoApi* | [**access_permission_simple_query**](docs/AccessInfoApi.md#access_permission_simple_query) | **GET** /{scopeId}/accessinfos/{accessInfoId}/permissions | Gets the AccessPermission list in the scope
*AccessInfoApi* | [**access_role_count**](docs/AccessInfoApi.md#access_role_count) | **POST** /{scopeId}/accessinfos/{accessInfoId}/roles/_count | Counts the AccessRoles
*AccessInfoApi* | [**access_role_create**](docs/AccessInfoApi.md#access_role_create) | **POST** /{scopeId}/accessinfos/{accessInfoId}/roles | Create an AccessRole
*AccessInfoApi* | [**access_role_delete**](docs/AccessInfoApi.md#access_role_delete) | **DELETE** /{scopeId}/accessinfos/{accessInfoId}/roles/{accessRoleId} | Delete an AccessRole
*AccessInfoApi* | [**access_role_find**](docs/AccessInfoApi.md#access_role_find) | **GET** /{scopeId}/accessinfos/{accessInfoId}/roles/{accessRoleId} | Get an AccessRole
*AccessInfoApi* | [**access_role_query**](docs/AccessInfoApi.md#access_role_query) | **POST** /{scopeId}/accessinfos/{accessInfoId}/roles/_query | Queries the AccessRoles
*AccessInfoApi* | [**access_role_simple_query**](docs/AccessInfoApi.md#access_role_simple_query) | **GET** /{scopeId}/accessinfos/{accessInfoId}/roles | Gets the AccessRole list in the scope
*AccountsApi* | [**account_count**](docs/AccountsApi.md#account_count) | **POST** /{scopeId}/accounts/_count | Counts the Accounts
*AccountsApi* | [**account_create**](docs/AccountsApi.md#account_create) | **POST** /{scopeId}/accounts | Create an Account
*AccountsApi* | [**account_delete**](docs/AccountsApi.md#account_delete) | **DELETE** /{scopeId}/accounts/{accountId} | Delete an Account
*AccountsApi* | [**account_find**](docs/AccountsApi.md#account_find) | **GET** /{scopeId}/accounts/{accountId} | Get an Account
*AccountsApi* | [**account_query**](docs/AccountsApi.md#account_query) | **POST** /{scopeId}/accounts/_query | Queries the Accounts
*AccountsApi* | [**account_simple_query**](docs/AccountsApi.md#account_simple_query) | **GET** /{scopeId}/accounts | Gets the Account list in the scope
*AccountsApi* | [**account_update**](docs/AccountsApi.md#account_update) | **PUT** /{scopeId}/accounts/{accountId} | Update an Account
*AuthenticationApi* | [**authentication_api_key**](docs/AuthenticationApi.md#authentication_api_key) | **POST** /authentication/apikey | Authenticate an user
*AuthenticationApi* | [**authentication_jwt**](docs/AuthenticationApi.md#authentication_jwt) | **POST** /authentication/jwt | Authenticate an user
*AuthenticationApi* | [**authentication_logout**](docs/AuthenticationApi.md#authentication_logout) | **POST** /authentication/logout | Logs out an user
*AuthenticationApi* | [**authentication_refresh**](docs/AuthenticationApi.md#authentication_refresh) | **POST** /authentication/refresh | Refreshes an AccessToken
*AuthenticationApi* | [**authentication_user**](docs/AuthenticationApi.md#authentication_user) | **POST** /authentication/user | Authenticate an user
*CredentialsApi* | [**credential_count**](docs/CredentialsApi.md#credential_count) | **POST** /{scopeId}/credentials/_count | Counts the Credentials
*CredentialsApi* | [**credential_create**](docs/CredentialsApi.md#credential_create) | **POST** /{scopeId}/credentials | Create a Credential
*CredentialsApi* | [**credential_delete**](docs/CredentialsApi.md#credential_delete) | **DELETE** /{scopeId}/credentials/{credentialId} | Delete a Credential
*CredentialsApi* | [**credential_find**](docs/CredentialsApi.md#credential_find) | **GET** /{scopeId}/credentials/{credentialId} | Get a Credential
*CredentialsApi* | [**credential_query**](docs/CredentialsApi.md#credential_query) | **POST** /{scopeId}/credentials/_query | Queries the Credentials
*CredentialsApi* | [**credential_simple_query**](docs/CredentialsApi.md#credential_simple_query) | **GET** /{scopeId}/credentials | Gets the Credential list in the scope
*CredentialsApi* | [**credential_unlock**](docs/CredentialsApi.md#credential_unlock) | **POST** /{scopeId}/credentials/{credentialId}/unlock | Unlock a Credential
*CredentialsApi* | [**credential_update**](docs/CredentialsApi.md#credential_update) | **PUT** /{scopeId}/credentials/{credentialId} | Update an Credential
*DataChannelsApi* | [**data_channel_count**](docs/DataChannelsApi.md#data_channel_count) | **POST** /{scopeId}/data/channels/_count | Counts the ChannelInfos
*DataChannelsApi* | [**data_channel_find**](docs/DataChannelsApi.md#data_channel_find) | **GET** /{scopeId}/data/channels/{channelInfoId} | Gets an ChannelInfo
*DataChannelsApi* | [**data_channel_query**](docs/DataChannelsApi.md#data_channel_query) | **POST** /{scopeId}/data/channels/_query | Queries the ChannelInfos
*DataChannelsApi* | [**data_channel_simple_query**](docs/DataChannelsApi.md#data_channel_simple_query) | **GET** /{scopeId}/data/channels | Gets the ChannelInfo list in the scope
*DataClientsApi* | [**data_client_count**](docs/DataClientsApi.md#data_client_count) | **POST** /{scopeId}/data/clients/_count | Counts the ClientInfos
*DataClientsApi* | [**data_client_find**](docs/DataClientsApi.md#data_client_find) | **GET** /{scopeId}/data/clients/{clientInfoId} | Gets an ClientInfo
*DataClientsApi* | [**data_client_query**](docs/DataClientsApi.md#data_client_query) | **POST** /{scopeId}/data/clients/_query | Queries the ClientInfos
*DataClientsApi* | [**data_client_simple_query**](docs/DataClientsApi.md#data_client_simple_query) | **GET** /{scopeId}/data/clients | Gets the ClientInfo list in the scope
*DataMessagesApi* | [**data_message_count**](docs/DataMessagesApi.md#data_message_count) | **POST** /{scopeId}/data/messages/_count | Counts the DatastoreMessages
*DataMessagesApi* | [**data_message_find**](docs/DataMessagesApi.md#data_message_find) | **GET** /{scopeId}/data/messages/{datastoreMessageId} | Gets an DatastoreMessage
*DataMessagesApi* | [**data_message_query**](docs/DataMessagesApi.md#data_message_query) | **POST** /{scopeId}/data/messages/_query | Queries the DatastoreMessages
*DataMessagesApi* | [**data_message_simple_query**](docs/DataMessagesApi.md#data_message_simple_query) | **GET** /{scopeId}/data/messages | Gets the DatastoreMessage list in the scope
*DataMessagesApi* | [**data_message_store**](docs/DataMessagesApi.md#data_message_store) | **POST** /{scopeId}/data/messages | Stores a new KapuaDataMessage
*DataMetricsApi* | [**data_metric_count**](docs/DataMetricsApi.md#data_metric_count) | **POST** /{scopeId}/data/metrics/_count | Counts the MetricInfos
*DataMetricsApi* | [**data_metric_find**](docs/DataMetricsApi.md#data_metric_find) | **GET** /{scopeId}/data/metrics/{metricInfoId} | Gets an MetricInfo
*DataMetricsApi* | [**data_metric_query**](docs/DataMetricsApi.md#data_metric_query) | **POST** /{scopeId}/data/metrics/_query | Queries the MetricInfos
*DataMetricsApi* | [**data_metric_simple_query**](docs/DataMetricsApi.md#data_metric_simple_query) | **GET** /{scopeId}/data/metrics | Gets the MetricInfo list in the scope
*DeviceConnectionsApi* | [**device_connection_count**](docs/DeviceConnectionsApi.md#device_connection_count) | **POST** /{scopeId}/deviceconnections/_count | Counts the DeviceConnections
*DeviceConnectionsApi* | [**device_connection_find**](docs/DeviceConnectionsApi.md#device_connection_find) | **GET** /{scopeId}/deviceconnections/{deviceConnectionId} | Get an DeviceConnection
*DeviceConnectionsApi* | [**device_connection_query**](docs/DeviceConnectionsApi.md#device_connection_query) | **POST** /{scopeId}/deviceconnections/_query | Queries the DeviceConnections
*DeviceConnectionsApi* | [**device_connection_simple_query**](docs/DeviceConnectionsApi.md#device_connection_simple_query) | **GET** /{scopeId}/deviceconnections | Gets the DeviceConnection list in the scope
*DeviceConnectionsApi* | [**find**](docs/DeviceConnectionsApi.md#find) | **GET** /{scopeId}/deviceconnections/{connectionId}/options | Gets the DeviceConnection list in the scope
*DeviceConnectionsApi* | [**update**](docs/DeviceConnectionsApi.md#update) | **PUT** /{scopeId}/deviceconnections/{connectionId}/options | Get an DeviceConnectionOption
*DevicesApi* | [**device_asset_filtered_get**](docs/DevicesApi.md#device_asset_filtered_get) | **POST** /{scopeId}/devices/{deviceId}/assets | Gets a list of assets
*DevicesApi* | [**device_asset_get**](docs/DevicesApi.md#device_asset_get) | **GET** /{scopeId}/devices/{deviceId}/assets | Gets a list of assets
*DevicesApi* | [**device_asset_read**](docs/DevicesApi.md#device_asset_read) | **POST** /{scopeId}/devices/{deviceId}/assets/_read | Reads asset channel values
*DevicesApi* | [**device_asset_write**](docs/DevicesApi.md#device_asset_write) | **POST** /{scopeId}/devices/{deviceId}/assets/_write | Gets a list of assets
*DevicesApi* | [**device_bundle_get**](docs/DevicesApi.md#device_bundle_get) | **GET** /{scopeId}/devices/{deviceId}/bundles | Gets a list of bundles
*DevicesApi* | [**device_bundle_start**](docs/DevicesApi.md#device_bundle_start) | **POST** /{scopeId}/devices/{deviceId}/bundles/{bundleId}/_start | Start a bundle
*DevicesApi* | [**device_bundle_stop**](docs/DevicesApi.md#device_bundle_stop) | **POST** /{scopeId}/devices/{deviceId}/bundles/{bundleId}/_stop | Stop a bundle
*DevicesApi* | [**device_command_execute**](docs/DevicesApi.md#device_command_execute) | **POST** /{scopeId}/devices/{deviceId}/commands/_execute | Executes a command
*DevicesApi* | [**device_configuration_component_get**](docs/DevicesApi.md#device_configuration_component_get) | **GET** /{scopeId}/devices/{deviceId}/configurations/{componentId} | Gets the configuration of a component on a device
*DevicesApi* | [**device_configuration_component_update**](docs/DevicesApi.md#device_configuration_component_update) | **PUT** /{scopeId}/devices/{deviceId}/configurations/{componentId} | Updates the configuration of a component on a device
*DevicesApi* | [**device_configuration_get**](docs/DevicesApi.md#device_configuration_get) | **GET** /{scopeId}/devices/{deviceId}/configurations | Gets the device configurations
*DevicesApi* | [**device_configuration_update**](docs/DevicesApi.md#device_configuration_update) | **PUT** /{scopeId}/devices/{deviceId}/configurations | Updates a device configuration
*DevicesApi* | [**device_count**](docs/DevicesApi.md#device_count) | **POST** /{scopeId}/devices/_count | Counts the Devices
*DevicesApi* | [**device_create**](docs/DevicesApi.md#device_create) | **POST** /{scopeId}/devices | Create an Device
*DevicesApi* | [**device_delete**](docs/DevicesApi.md#device_delete) | **DELETE** /{scopeId}/devices/{deviceId} | Delete a Device
*DevicesApi* | [**device_event_count**](docs/DevicesApi.md#device_event_count) | **POST** /{scopeId}/devices/{deviceId}/events/_count | Counts the DeviceEvents
*DevicesApi* | [**device_event_delete**](docs/DevicesApi.md#device_event_delete) | **DELETE** /{scopeId}/devices/{deviceId}/events/{deviceEventId} | Delete a DeviceEvent
*DevicesApi* | [**device_event_find**](docs/DevicesApi.md#device_event_find) | **GET** /{scopeId}/devices/{deviceId}/events/{deviceEventId} | Get an DeviceEvent
*DevicesApi* | [**device_event_query**](docs/DevicesApi.md#device_event_query) | **POST** /{scopeId}/devices/{deviceId}/events/_query | Queries the DeviceEvents
*DevicesApi* | [**device_event_simple_query**](docs/DevicesApi.md#device_event_simple_query) | **GET** /{scopeId}/devices/{deviceId}/events | Gets the DeviceEvent list in the scope
*DevicesApi* | [**device_find**](docs/DevicesApi.md#device_find) | **GET** /{scopeId}/devices/{deviceId} | Get a Device
*DevicesApi* | [**device_package_download**](docs/DevicesApi.md#device_package_download) | **POST** /{scopeId}/devices/{deviceId}/packages/_download | Installs a package
*DevicesApi* | [**device_package_get**](docs/DevicesApi.md#device_package_get) | **GET** /{scopeId}/devices/{deviceId}/packages | Gets a list of packages
*DevicesApi* | [**device_package_uninstall**](docs/DevicesApi.md#device_package_uninstall) | **POST** /{scopeId}/devices/{deviceId}/packages/_uninstall | Uninstalls a package
*DevicesApi* | [**device_query**](docs/DevicesApi.md#device_query) | **POST** /{scopeId}/devices/_query | Queries the Devices
*DevicesApi* | [**device_request_send**](docs/DevicesApi.md#device_request_send) | **POST** /{scopeId}/devices/{deviceId}/requests | Sends a request
*DevicesApi* | [**device_simple_query**](docs/DevicesApi.md#device_simple_query) | **GET** /{scopeId}/devices | Gets the Device list in the scope
*DevicesApi* | [**device_snapshot_get**](docs/DevicesApi.md#device_snapshot_get) | **GET** /{scopeId}/devices/{deviceId}/snapshots | Gets a list of snapshots
*DevicesApi* | [**device_snapshot_rollback**](docs/DevicesApi.md#device_snapshot_rollback) | **POST** /{scopeId}/devices/{deviceId}/snapshots/{snapshotId}/_rollback | Gets a list of snapshots
*DevicesApi* | [**device_update**](docs/DevicesApi.md#device_update) | **PUT** /{scopeId}/devices/{deviceId} | Update a Device
*DomainsApi* | [**domain_count**](docs/DomainsApi.md#domain_count) | **POST** /{scopeId}/domains/_count | Counts the Domains
*DomainsApi* | [**domain_find**](docs/DomainsApi.md#domain_find) | **GET** /{scopeId}/domains/{domainId} | Get a Domain
*DomainsApi* | [**domain_query**](docs/DomainsApi.md#domain_query) | **POST** /{scopeId}/domains/_query | Queries the Domains
*DomainsApi* | [**domain_simple_query**](docs/DomainsApi.md#domain_simple_query) | **GET** /{scopeId}/domains | Gets the Domain list in the scope
*EndpointInfosApi* | [**create_endpoint_info**](docs/EndpointInfosApi.md#create_endpoint_info) | **POST** /{scopeId}/endpointInfos | Create a EndpointInfo
*EndpointInfosApi* | [**endpoint_info_count**](docs/EndpointInfosApi.md#endpoint_info_count) | **POST** /{scopeId}/endpointInfos/_count | Counts the EndpointInfos
*EndpointInfosApi* | [**endpoint_info_delete**](docs/EndpointInfosApi.md#endpoint_info_delete) | **DELETE** /{scopeId}/endpointInfos/{endpointInfoId} | Delete an EndpointInfo
*EndpointInfosApi* | [**endpoint_info_find**](docs/EndpointInfosApi.md#endpoint_info_find) | **GET** /{scopeId}/endpointInfos/{endpointInfoId} | Get a EndpointInfo
*EndpointInfosApi* | [**endpoint_info_query**](docs/EndpointInfosApi.md#endpoint_info_query) | **POST** /{scopeId}/endpointInfos/_query | Queries the EndpointInfos
*EndpointInfosApi* | [**endpoint_info_simple_query**](docs/EndpointInfosApi.md#endpoint_info_simple_query) | **GET** /{scopeId}/endpointInfos | Gets the EndpointInfo list in the scope
*EndpointInfosApi* | [**endpoint_info_update**](docs/EndpointInfosApi.md#endpoint_info_update) | **PUT** /{scopeId}/endpointInfos/{endpointInfoId} | Update a EndpointInfo
*GroupsApi* | [**group_count**](docs/GroupsApi.md#group_count) | **POST** /{scopeId}/groups/_count | Counts the Groups
*GroupsApi* | [**group_create**](docs/GroupsApi.md#group_create) | **POST** /{scopeId}/groups | Create a Group
*GroupsApi* | [**group_delete**](docs/GroupsApi.md#group_delete) | **DELETE** /{scopeId}/groups/{groupId} | Delete an Group
*GroupsApi* | [**group_find**](docs/GroupsApi.md#group_find) | **GET** /{scopeId}/groups/{groupId} | Get an Group
*GroupsApi* | [**group_query**](docs/GroupsApi.md#group_query) | **POST** /{scopeId}/groups/_query | Queries the Groups
*GroupsApi* | [**group_simple_query**](docs/GroupsApi.md#group_simple_query) | **GET** /{scopeId}/groups | Gets the Group list in the scope
*GroupsApi* | [**group_update**](docs/GroupsApi.md#group_update) | **PUT** /{scopeId}/groups/{groupId} | Update an Group
*RolesApi* | [**role_count**](docs/RolesApi.md#role_count) | **POST** /{scopeId}/roles/_count | Counts the Roles
*RolesApi* | [**role_create**](docs/RolesApi.md#role_create) | **POST** /{scopeId}/roles | Create a Role
*RolesApi* | [**role_delete**](docs/RolesApi.md#role_delete) | **DELETE** /{scopeId}/roles/{roleId} | Delete a Role
*RolesApi* | [**role_find**](docs/RolesApi.md#role_find) | **GET** /{scopeId}/roles/{roleId} | Get a Role
*RolesApi* | [**role_permission_count**](docs/RolesApi.md#role_permission_count) | **POST** /{scopeId}/roles/{roleId}/permissions/_count | Counts the RolePermissions
*RolesApi* | [**role_permission_create**](docs/RolesApi.md#role_permission_create) | **POST** /{scopeId}/roles/{roleId}/permissions | Create a RolePermission
*RolesApi* | [**role_permission_delete**](docs/RolesApi.md#role_permission_delete) | **DELETE** /{scopeId}/roles/{roleId}/permissions/{rolePermissionId} | Delete an RolePermission
*RolesApi* | [**role_permission_find**](docs/RolesApi.md#role_permission_find) | **GET** /{scopeId}/roles/{roleId}/permissions/{rolePermissionId} | Get a RolePermission
*RolesApi* | [**role_permission_query**](docs/RolesApi.md#role_permission_query) | **POST** /{scopeId}/roles/{roleId}/permissions/_query | Queries the RolePermissions
*RolesApi* | [**role_permission_simple_query**](docs/RolesApi.md#role_permission_simple_query) | **GET** /{scopeId}/roles/{roleId}/permissions | Gets the RolePermission list in the scope
*RolesApi* | [**role_query**](docs/RolesApi.md#role_query) | **POST** /{scopeId}/roles/_query | Queries the Roles
*RolesApi* | [**role_simple_query**](docs/RolesApi.md#role_simple_query) | **GET** /{scopeId}/roles | Gets the Role list in the scope
*RolesApi* | [**role_update**](docs/RolesApi.md#role_update) | **PUT** /{scopeId}/roles/{roleId} | Update an Role
*StreamsApi* | [**stream_publish**](docs/StreamsApi.md#stream_publish) | **POST** /{scopeId}/streams/messages | Publishes a fire-and-forget message
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /{scopeId}/tags | Create a Tag
*TagsApi* | [**tag_count**](docs/TagsApi.md#tag_count) | **POST** /{scopeId}/tags/_count | Counts the Tags
*TagsApi* | [**tag_delete**](docs/TagsApi.md#tag_delete) | **DELETE** /{scopeId}/tags/{tagId} | Delete an Tag
*TagsApi* | [**tag_find**](docs/TagsApi.md#tag_find) | **GET** /{scopeId}/tags/{tagId} | Get a Tag
*TagsApi* | [**tag_query**](docs/TagsApi.md#tag_query) | **POST** /{scopeId}/tags/_query | Queries the Tags
*TagsApi* | [**tag_simple_query**](docs/TagsApi.md#tag_simple_query) | **GET** /{scopeId}/tags | Gets the Tag list in the scope
*TagsApi* | [**tag_update**](docs/TagsApi.md#tag_update) | **PUT** /{scopeId}/tags/{tagId} | Update a Tag
*UsersApi* | [**user_count**](docs/UsersApi.md#user_count) | **POST** /{scopeId}/users/_count | Counts the Users
*UsersApi* | [**user_create**](docs/UsersApi.md#user_create) | **POST** /{scopeId}/users | Create an User
*UsersApi* | [**user_delete**](docs/UsersApi.md#user_delete) | **DELETE** /{scopeId}/users/{userId} | Delete an User
*UsersApi* | [**user_find**](docs/UsersApi.md#user_find) | **GET** /{scopeId}/users/{userId} | Get an User
*UsersApi* | [**user_query**](docs/UsersApi.md#user_query) | **POST** /{scopeId}/users/_query | Queries the Users
*UsersApi* | [**user_simple_query**](docs/UsersApi.md#user_simple_query) | **GET** /{scopeId}/users | Gets the User list in the scope
*UsersApi* | [**user_update**](docs/UsersApi.md#user_update) | **PUT** /{scopeId}/users/{userId} | Update an User


## Documentation For Models

 - [AccessInfo](docs/AccessInfo.md)
 - [AccessInfoCreator](docs/AccessInfoCreator.md)
 - [AccessInfoListResult](docs/AccessInfoListResult.md)
 - [AccessInfoQuery](docs/AccessInfoQuery.md)
 - [AccessPermission](docs/AccessPermission.md)
 - [AccessPermissionCreator](docs/AccessPermissionCreator.md)
 - [AccessPermissionListResult](docs/AccessPermissionListResult.md)
 - [AccessPermissionQuery](docs/AccessPermissionQuery.md)
 - [AccessRole](docs/AccessRole.md)
 - [AccessRoleCreator](docs/AccessRoleCreator.md)
 - [AccessRoleListResult](docs/AccessRoleListResult.md)
 - [AccessRoleQuery](docs/AccessRoleQuery.md)
 - [AccessToken](docs/AccessToken.md)
 - [Account](docs/Account.md)
 - [AccountCreator](docs/AccountCreator.md)
 - [AccountListResult](docs/AccountListResult.md)
 - [AccountQuery](docs/AccountQuery.md)
 - [ApiKeyCredentials](docs/ApiKeyCredentials.md)
 - [ChannelInfo](docs/ChannelInfo.md)
 - [ChannelInfoListResult](docs/ChannelInfoListResult.md)
 - [ChannelInfoQuery](docs/ChannelInfoQuery.md)
 - [ClientInfo](docs/ClientInfo.md)
 - [ClientInfoListResult](docs/ClientInfoListResult.md)
 - [ClientInfoQuery](docs/ClientInfoQuery.md)
 - [CountResult](docs/CountResult.md)
 - [Credential](docs/Credential.md)
 - [CredentialCreator](docs/CredentialCreator.md)
 - [CredentialListResult](docs/CredentialListResult.md)
 - [CredentialQuery](docs/CredentialQuery.md)
 - [DatastoreMessage](docs/DatastoreMessage.md)
 - [Device](docs/Device.md)
 - [DeviceAsset](docs/DeviceAsset.md)
 - [DeviceAssetChannel](docs/DeviceAssetChannel.md)
 - [DeviceAssets](docs/DeviceAssets.md)
 - [DeviceBundle](docs/DeviceBundle.md)
 - [DeviceBundles](docs/DeviceBundles.md)
 - [DeviceCommandInput](docs/DeviceCommandInput.md)
 - [DeviceCommandOutput](docs/DeviceCommandOutput.md)
 - [DeviceComponentConfiguration](docs/DeviceComponentConfiguration.md)
 - [DeviceConfiguration](docs/DeviceConfiguration.md)
 - [DeviceConnection](docs/DeviceConnection.md)
 - [DeviceConnectionListResult](docs/DeviceConnectionListResult.md)
 - [DeviceConnectionOption](docs/DeviceConnectionOption.md)
 - [DeviceConnectionQuery](docs/DeviceConnectionQuery.md)
 - [DeviceCreator](docs/DeviceCreator.md)
 - [DeviceEvent](docs/DeviceEvent.md)
 - [DeviceEventListResult](docs/DeviceEventListResult.md)
 - [DeviceEventQuery](docs/DeviceEventQuery.md)
 - [DeviceListResult](docs/DeviceListResult.md)
 - [DevicePackageDownloadRequest](docs/DevicePackageDownloadRequest.md)
 - [DevicePackageUninstallRequest](docs/DevicePackageUninstallRequest.md)
 - [DeviceQuery](docs/DeviceQuery.md)
 - [DeviceSnapshot](docs/DeviceSnapshot.md)
 - [DeviceSnapshots](docs/DeviceSnapshots.md)
 - [Domain](docs/Domain.md)
 - [DomainListResult](docs/DomainListResult.md)
 - [DomainQuery](docs/DomainQuery.md)
 - [EndpointInfo](docs/EndpointInfo.md)
 - [EndpointInfoCreator](docs/EndpointInfoCreator.md)
 - [EndpointInfoListResult](docs/EndpointInfoListResult.md)
 - [EndpointInfoQuery](docs/EndpointInfoQuery.md)
 - [EndpointUsage](docs/EndpointUsage.md)
 - [GenericRequestChannel](docs/GenericRequestChannel.md)
 - [GenericRequestMessage](docs/GenericRequestMessage.md)
 - [GenericRequestPayload](docs/GenericRequestPayload.md)
 - [Group](docs/Group.md)
 - [GroupCreator](docs/GroupCreator.md)
 - [GroupListResult](docs/GroupListResult.md)
 - [GroupQuery](docs/GroupQuery.md)
 - [JsonGenericRequestMessage](docs/JsonGenericRequestMessage.md)
 - [JsonKapuaDataMessage](docs/JsonKapuaDataMessage.md)
 - [JsonKapuaPayload](docs/JsonKapuaPayload.md)
 - [JsonMessageQuery](docs/JsonMessageQuery.md)
 - [JwtCredentials](docs/JwtCredentials.md)
 - [KapuaAppProperties](docs/KapuaAppProperties.md)
 - [KapuaDataChannel](docs/KapuaDataChannel.md)
 - [KapuaDataMessage](docs/KapuaDataMessage.md)
 - [KapuaDataPayload](docs/KapuaDataPayload.md)
 - [KapuaId](docs/KapuaId.md)
 - [KapuaPayload](docs/KapuaPayload.md)
 - [KapuaPosition](docs/KapuaPosition.md)
 - [KapuaSortCriteria](docs/KapuaSortCriteria.md)
 - [KapuaTad](docs/KapuaTad.md)
 - [KapuaTicon](docs/KapuaTicon.md)
 - [KapuaTocd](docs/KapuaTocd.md)
 - [KapuaToption](docs/KapuaToption.md)
 - [KapuaTscalar](docs/KapuaTscalar.md)
 - [MessageListResult](docs/MessageListResult.md)
 - [MessageQuery](docs/MessageQuery.md)
 - [MetricInfo](docs/MetricInfo.md)
 - [MetricInfoListResult](docs/MetricInfoListResult.md)
 - [MetricInfoQuery](docs/MetricInfoQuery.md)
 - [Organization](docs/Organization.md)
 - [Permission](docs/Permission.md)
 - [QueryPredicate](docs/QueryPredicate.md)
 - [RefreshTokenCredentials](docs/RefreshTokenCredentials.md)
 - [Role](docs/Role.md)
 - [RoleCreator](docs/RoleCreator.md)
 - [RoleListResult](docs/RoleListResult.md)
 - [RolePermission](docs/RolePermission.md)
 - [RolePermissionCreator](docs/RolePermissionCreator.md)
 - [RolePermissionListResult](docs/RolePermissionListResult.md)
 - [RolePermissionQuery](docs/RolePermissionQuery.md)
 - [RoleQuery](docs/RoleQuery.md)
 - [SortField](docs/SortField.md)
 - [StorableId](docs/StorableId.md)
 - [StorablePredicate](docs/StorablePredicate.md)
 - [Tag](docs/Tag.md)
 - [TagCreator](docs/TagCreator.md)
 - [TagListResult](docs/TagListResult.md)
 - [TagQuery](docs/TagQuery.md)
 - [User](docs/User.md)
 - [UserCreator](docs/UserCreator.md)
 - [UserListResult](docs/UserListResult.md)
 - [UserQuery](docs/UserQuery.md)
 - [UsernamePasswordCredentials](docs/UsernamePasswordCredentials.md)
 - [XmlAdaptedMetric](docs/XmlAdaptedMetric.md)
 - [XmlAdaptedSortField](docs/XmlAdaptedSortField.md)


## Documentation For Authorization


## kapuaAccessToken

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



