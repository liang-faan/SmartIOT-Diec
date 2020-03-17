# swagger_client.ServiceConfigurationsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_configuration_component_get**](ServiceConfigurationsApi.md#service_configuration_component_get) | **GET** /{scopeId}/serviceConfigurations/{serviceId} | Gets the configuration of a service on an account
[**service_configuration_component_update**](ServiceConfigurationsApi.md#service_configuration_component_update) | **PUT** /{scopeId}/serviceConfigurations/{serviceId} | Updates the configuration of a service on an account
[**service_configuration_get**](ServiceConfigurationsApi.md#service_configuration_get) | **GET** /{scopeId}/serviceConfigurations | Gets multiple services configurations
[**service_configuration_update**](ServiceConfigurationsApi.md#service_configuration_update) | **PUT** /{scopeId}/serviceConfigurations | Updates multiple services configuration


# **service_configuration_component_get**
> ServiceComponentConfiguration service_configuration_component_get(scope_id, service_id)

Gets the configuration of a service on an account

Returns the configuration of a single service in an account

### Example
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
api_instance = swagger_client.ServiceConfigurationsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
service_id = 'service_id_example' # str | The full class name of the service.

try:
    # Gets the configuration of a service on an account
    api_response = api_instance.service_configuration_component_get(scope_id, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceConfigurationsApi->service_configuration_component_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **service_id** | **str**| The full class name of the service. | 

### Return type

[**ServiceComponentConfiguration**](ServiceComponentConfiguration.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_configuration_component_update**
> service_configuration_component_update(scope_id, service_id, body)

Updates the configuration of a service on an account

Updates a service component configuration

### Example
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
api_instance = swagger_client.ServiceConfigurationsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
service_id = 'service_id_example' # str | The full class name of the service.
body = swagger_client.ServiceComponentConfiguration() # ServiceComponentConfiguration | The values for the configurations

try:
    # Updates the configuration of a service on an account
    api_instance.service_configuration_component_update(scope_id, service_id, body)
except ApiException as e:
    print("Exception when calling ServiceConfigurationsApi->service_configuration_component_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **service_id** | **str**| The full class name of the service. | 
 **body** | [**ServiceComponentConfiguration**](ServiceComponentConfiguration.md)| The values for the configurations | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_configuration_get**
> ServiceConfiguration service_configuration_get(scope_id)

Gets multiple services configurations

Returns the current configuration of multiple services from an account

### Example
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
api_instance = swagger_client.ServiceConfigurationsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.

try:
    # Gets multiple services configurations
    api_response = api_instance.service_configuration_get(scope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceConfigurationsApi->service_configuration_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 

### Return type

[**ServiceConfiguration**](ServiceConfiguration.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_configuration_update**
> service_configuration_update(scope_id, body)

Updates multiple services configuration

Updates the configuration of multiple services in an account

### Example
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
api_instance = swagger_client.ServiceConfigurationsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.ServiceConfiguration() # ServiceConfiguration | The values for the configurations

try:
    # Updates multiple services configuration
    api_instance.service_configuration_update(scope_id, body)
except ApiException as e:
    print("Exception when calling ServiceConfigurationsApi->service_configuration_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**ServiceConfiguration**](ServiceConfiguration.md)| The values for the configurations | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

