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


class DeviceConnectionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def device_connection_count(self, scope_id, body, **kwargs):  # noqa: E501
        """Counts the DeviceConnections  # noqa: E501

        Counts the DeviceConnections with the given DeviceConnectionQuery parameter returning the number of matching DeviceConnections  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_count(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to count results (required)
        :param DeviceConnectionQuery body: The DeviceConnectionQuery to use to filter count results (required)
        :return: CountResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_connection_count_with_http_info(scope_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.device_connection_count_with_http_info(scope_id, body, **kwargs)  # noqa: E501
            return data

    def device_connection_count_with_http_info(self, scope_id, body, **kwargs):  # noqa: E501
        """Counts the DeviceConnections  # noqa: E501

        Counts the DeviceConnections with the given DeviceConnectionQuery parameter returning the number of matching DeviceConnections  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_count_with_http_info(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to count results (required)
        :param DeviceConnectionQuery body: The DeviceConnectionQuery to use to filter count results (required)
        :return: CountResult
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
                    " to method device_connection_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `device_connection_count`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `device_connection_count`")  # noqa: E501

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
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/deviceconnections/_count', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_connection_find(self, scope_id, device_connection_id, **kwargs):  # noqa: E501
        """Get an DeviceConnection  # noqa: E501

        Returns the DeviceConnection specified by the \"deviceConnectionId\" path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_find(scope_id, device_connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId of the requested DeviceConnection. (required)
        :param str device_connection_id: The id of the requested DeviceConnection (required)
        :return: DeviceConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_connection_find_with_http_info(scope_id, device_connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.device_connection_find_with_http_info(scope_id, device_connection_id, **kwargs)  # noqa: E501
            return data

    def device_connection_find_with_http_info(self, scope_id, device_connection_id, **kwargs):  # noqa: E501
        """Get an DeviceConnection  # noqa: E501

        Returns the DeviceConnection specified by the \"deviceConnectionId\" path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_find_with_http_info(scope_id, device_connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId of the requested DeviceConnection. (required)
        :param str device_connection_id: The id of the requested DeviceConnection (required)
        :return: DeviceConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'device_connection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_connection_find" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `device_connection_find`")  # noqa: E501
        # verify the required parameter 'device_connection_id' is set
        if ('device_connection_id' not in params or
                params['device_connection_id'] is None):
            raise ValueError("Missing the required parameter `device_connection_id` when calling `device_connection_find`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501
        if 'device_connection_id' in params:
            path_params['deviceConnectionId'] = params['device_connection_id']  # noqa: E501

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
            '/{scopeId}/deviceconnections/{deviceConnectionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceConnection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_connection_query(self, scope_id, body, **kwargs):  # noqa: E501
        """Queries the DeviceConnections  # noqa: E501

        Queries the DeviceConnections with the given DeviceConnections parameter returning all matching DeviceConnections  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_query(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param DeviceConnectionQuery body: The DeviceConnectionQuery to use to filter results. (required)
        :return: DeviceConnectionListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_connection_query_with_http_info(scope_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.device_connection_query_with_http_info(scope_id, body, **kwargs)  # noqa: E501
            return data

    def device_connection_query_with_http_info(self, scope_id, body, **kwargs):  # noqa: E501
        """Queries the DeviceConnections  # noqa: E501

        Queries the DeviceConnections with the given DeviceConnections parameter returning all matching DeviceConnections  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_query_with_http_info(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param DeviceConnectionQuery body: The DeviceConnectionQuery to use to filter results. (required)
        :return: DeviceConnectionListResult
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
                    " to method device_connection_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `device_connection_query`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `device_connection_query`")  # noqa: E501

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
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/deviceconnections/_query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceConnectionListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_connection_simple_query(self, scope_id, **kwargs):  # noqa: E501
        """Gets the DeviceConnection list in the scope  # noqa: E501

        Returns the list of all the deviceConnections associated to the current selected scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_simple_query(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str body: The client id to filter results.
        :param str status: The connection status to filter results.
        :param int offset: The result set offset.
        :param int limit: The result set limit.
        :return: DeviceConnectionListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_connection_simple_query_with_http_info(scope_id, **kwargs)  # noqa: E501
        else:
            (data) = self.device_connection_simple_query_with_http_info(scope_id, **kwargs)  # noqa: E501
            return data

    def device_connection_simple_query_with_http_info(self, scope_id, **kwargs):  # noqa: E501
        """Gets the DeviceConnection list in the scope  # noqa: E501

        Returns the list of all the deviceConnections associated to the current selected scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_connection_simple_query_with_http_info(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str body: The client id to filter results.
        :param str status: The connection status to filter results.
        :param int offset: The result set offset.
        :param int limit: The result set limit.
        :return: DeviceConnectionListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'body', 'status', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_connection_simple_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `device_connection_simple_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/deviceconnections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceConnectionListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find(self, scope_id, connection_id, **kwargs):  # noqa: E501
        """Gets the DeviceConnection list in the scope  # noqa: E501

        Returns the list of all the deviceConnections associated to the current selected scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find(scope_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str connection_id: The connection id of the requested options. (required)
        :return: DeviceConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_with_http_info(scope_id, connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_with_http_info(scope_id, connection_id, **kwargs)  # noqa: E501
            return data

    def find_with_http_info(self, scope_id, connection_id, **kwargs):  # noqa: E501
        """Gets the DeviceConnection list in the scope  # noqa: E501

        Returns the list of all the deviceConnections associated to the current selected scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_with_http_info(scope_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str connection_id: The connection id of the requested options. (required)
        :return: DeviceConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'connection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `find`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `find`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/deviceconnections/{connectionId}/options', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceConnection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, scope_id, connection_id, body, **kwargs):  # noqa: E501
        """Get an DeviceConnectionOption  # noqa: E501

        Returns the DeviceConnectionOption specified by the given parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(scope_id, connection_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId of the requested DeviceConnectionOptions. (required)
        :param str connection_id: The id of the requested DeviceConnectionOptions (required)
        :param DeviceConnectionOption body: The modified Device connection options whose attributed need to be updated (required)
        :return: DeviceConnectionOption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_with_http_info(scope_id, connection_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(scope_id, connection_id, body, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, scope_id, connection_id, body, **kwargs):  # noqa: E501
        """Get an DeviceConnectionOption  # noqa: E501

        Returns the DeviceConnectionOption specified by the given parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(scope_id, connection_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId of the requested DeviceConnectionOptions. (required)
        :param str connection_id: The id of the requested DeviceConnectionOptions (required)
        :param DeviceConnectionOption body: The modified Device connection options whose attributed need to be updated (required)
        :return: DeviceConnectionOption
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'connection_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `update`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `update`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/deviceconnections/{connectionId}/options', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceConnectionOption',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
