# coding: utf-8

"""
    Eclipse Kapua REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ServiceConfigurationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def service_configuration_component_get(self, scope_id, service_id, **kwargs):  # noqa: E501
        """Gets the configuration of a service on an account  # noqa: E501

        Returns the configuration of a single service in an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_component_get(scope_id, service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str service_id: The full class name of the service. (required)
        :return: ServiceComponentConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_configuration_component_get_with_http_info(scope_id, service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.service_configuration_component_get_with_http_info(scope_id, service_id, **kwargs)  # noqa: E501
            return data

    def service_configuration_component_get_with_http_info(self, scope_id, service_id, **kwargs):  # noqa: E501
        """Gets the configuration of a service on an account  # noqa: E501

        Returns the configuration of a single service in an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_component_get_with_http_info(scope_id, service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str service_id: The full class name of the service. (required)
        :return: ServiceComponentConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'service_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_configuration_component_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `service_configuration_component_get`")  # noqa: E501
        # verify the required parameter 'service_id' is set
        if ('service_id' not in params or
                params['service_id'] is None):
            raise ValueError("Missing the required parameter `service_id` when calling `service_configuration_component_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501
        if 'service_id' in params:
            path_params['serviceId'] = params['service_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/serviceConfigurations/{serviceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceComponentConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_configuration_component_update(self, scope_id, service_id, body, **kwargs):  # noqa: E501
        """Updates the configuration of a service on an account  # noqa: E501

        Updates a service component configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_component_update(scope_id, service_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str service_id: The full class name of the service. (required)
        :param ServiceComponentConfiguration body: The values for the configurations (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_configuration_component_update_with_http_info(scope_id, service_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.service_configuration_component_update_with_http_info(scope_id, service_id, body, **kwargs)  # noqa: E501
            return data

    def service_configuration_component_update_with_http_info(self, scope_id, service_id, body, **kwargs):  # noqa: E501
        """Updates the configuration of a service on an account  # noqa: E501

        Updates a service component configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_component_update_with_http_info(scope_id, service_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str service_id: The full class name of the service. (required)
        :param ServiceComponentConfiguration body: The values for the configurations (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'service_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_configuration_component_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `service_configuration_component_update`")  # noqa: E501
        # verify the required parameter 'service_id' is set
        if ('service_id' not in params or
                params['service_id'] is None):
            raise ValueError("Missing the required parameter `service_id` when calling `service_configuration_component_update`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `service_configuration_component_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501
        if 'service_id' in params:
            path_params['serviceId'] = params['service_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/serviceConfigurations/{serviceId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_configuration_get(self, scope_id, **kwargs):  # noqa: E501
        """Gets multiple services configurations  # noqa: E501

        Returns the current configuration of multiple services from an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_get(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :return: ServiceConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_configuration_get_with_http_info(scope_id, **kwargs)  # noqa: E501
        else:
            (data) = self.service_configuration_get_with_http_info(scope_id, **kwargs)  # noqa: E501
            return data

    def service_configuration_get_with_http_info(self, scope_id, **kwargs):  # noqa: E501
        """Gets multiple services configurations  # noqa: E501

        Returns the current configuration of multiple services from an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_get_with_http_info(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :return: ServiceConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_configuration_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `service_configuration_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/serviceConfigurations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_configuration_update(self, scope_id, body, **kwargs):  # noqa: E501
        """Updates multiple services configuration  # noqa: E501

        Updates the configuration of multiple services in an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_update(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param ServiceConfiguration body: The values for the configurations (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_configuration_update_with_http_info(scope_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.service_configuration_update_with_http_info(scope_id, body, **kwargs)  # noqa: E501
            return data

    def service_configuration_update_with_http_info(self, scope_id, body, **kwargs):  # noqa: E501
        """Updates multiple services configuration  # noqa: E501

        Updates the configuration of multiple services in an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_configuration_update_with_http_info(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param ServiceConfiguration body: The values for the configurations (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_configuration_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `service_configuration_update`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `service_configuration_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/serviceConfigurations', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
