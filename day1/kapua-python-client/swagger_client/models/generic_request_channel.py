# coding: utf-8

"""
    Eclipse Kapua REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.kapua_app_properties import KapuaAppProperties  # noqa: F401,E501


class GenericRequestChannel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resources': 'list[str]',
        'method': 'str',
        'version': 'KapuaAppProperties',
        'app_name': 'KapuaAppProperties',
        'semantic_parts': 'list[str]'
    }

    attribute_map = {
        'resources': 'resources',
        'method': 'method',
        'version': 'version',
        'app_name': 'appName',
        'semantic_parts': 'semanticParts'
    }

    def __init__(self, resources=None, method=None, version=None, app_name=None, semantic_parts=None):  # noqa: E501
        """GenericRequestChannel - a model defined in Swagger"""  # noqa: E501

        self._resources = None
        self._method = None
        self._version = None
        self._app_name = None
        self._semantic_parts = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if method is not None:
            self.method = method
        if version is not None:
            self.version = version
        if app_name is not None:
            self.app_name = app_name
        if semantic_parts is not None:
            self.semantic_parts = semantic_parts

    @property
    def resources(self):
        """Gets the resources of this GenericRequestChannel.  # noqa: E501


        :return: The resources of this GenericRequestChannel.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this GenericRequestChannel.


        :param resources: The resources of this GenericRequestChannel.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

    @property
    def method(self):
        """Gets the method of this GenericRequestChannel.  # noqa: E501


        :return: The method of this GenericRequestChannel.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this GenericRequestChannel.


        :param method: The method of this GenericRequestChannel.  # noqa: E501
        :type: str
        """
        allowed_values = ["READ", "CREATE", "WRITE", "DELETE", "OPTIONS", "EXECUTE"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def version(self):
        """Gets the version of this GenericRequestChannel.  # noqa: E501


        :return: The version of this GenericRequestChannel.  # noqa: E501
        :rtype: KapuaAppProperties
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GenericRequestChannel.


        :param version: The version of this GenericRequestChannel.  # noqa: E501
        :type: KapuaAppProperties
        """

        self._version = version

    @property
    def app_name(self):
        """Gets the app_name of this GenericRequestChannel.  # noqa: E501


        :return: The app_name of this GenericRequestChannel.  # noqa: E501
        :rtype: KapuaAppProperties
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this GenericRequestChannel.


        :param app_name: The app_name of this GenericRequestChannel.  # noqa: E501
        :type: KapuaAppProperties
        """

        self._app_name = app_name

    @property
    def semantic_parts(self):
        """Gets the semantic_parts of this GenericRequestChannel.  # noqa: E501


        :return: The semantic_parts of this GenericRequestChannel.  # noqa: E501
        :rtype: list[str]
        """
        return self._semantic_parts

    @semantic_parts.setter
    def semantic_parts(self, semantic_parts):
        """Sets the semantic_parts of this GenericRequestChannel.


        :param semantic_parts: The semantic_parts of this GenericRequestChannel.  # noqa: E501
        :type: list[str]
        """

        self._semantic_parts = semantic_parts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GenericRequestChannel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GenericRequestChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
