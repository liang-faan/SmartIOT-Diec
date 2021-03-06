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


class DeviceConnection(object):
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
        'protocol': 'str',
        'status': 'str',
        'user_id': 'str',
        'client_id': 'str',
        'server_ip': 'str',
        'allow_user_change': 'bool',
        'user_coupling_mode': 'str',
        'reserved_user_id': 'str',
        'client_ip': 'str',
        'type': 'str',
        'optlock': 'int',
        'entity_attributes': 'dict(str, str)',
        'entity_properties': 'dict(str, str)',
        'modified_on': 'datetime',
        'modified_by': 'str',
        'scope_id': 'str',
        'id': 'str',
        'created_on': 'datetime',
        'created_by': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'status': 'status',
        'user_id': 'userId',
        'client_id': 'clientId',
        'server_ip': 'serverIp',
        'allow_user_change': 'allowUserChange',
        'user_coupling_mode': 'userCouplingMode',
        'reserved_user_id': 'reservedUserId',
        'client_ip': 'clientIp',
        'type': 'type',
        'optlock': 'optlock',
        'entity_attributes': 'entityAttributes',
        'entity_properties': 'entityProperties',
        'modified_on': 'modifiedOn',
        'modified_by': 'modifiedBy',
        'scope_id': 'scopeId',
        'id': 'id',
        'created_on': 'createdOn',
        'created_by': 'createdBy'
    }

    def __init__(self, protocol=None, status=None, user_id=None, client_id=None, server_ip=None, allow_user_change=None, user_coupling_mode=None, reserved_user_id=None, client_ip=None, type=None, optlock=None, entity_attributes=None, entity_properties=None, modified_on=None, modified_by=None, scope_id=None, id=None, created_on=None, created_by=None):  # noqa: E501
        """DeviceConnection - a model defined in Swagger"""  # noqa: E501

        self._protocol = None
        self._status = None
        self._user_id = None
        self._client_id = None
        self._server_ip = None
        self._allow_user_change = None
        self._user_coupling_mode = None
        self._reserved_user_id = None
        self._client_ip = None
        self._type = None
        self._optlock = None
        self._entity_attributes = None
        self._entity_properties = None
        self._modified_on = None
        self._modified_by = None
        self._scope_id = None
        self._id = None
        self._created_on = None
        self._created_by = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status
        if user_id is not None:
            self.user_id = user_id
        if client_id is not None:
            self.client_id = client_id
        if server_ip is not None:
            self.server_ip = server_ip
        if allow_user_change is not None:
            self.allow_user_change = allow_user_change
        if user_coupling_mode is not None:
            self.user_coupling_mode = user_coupling_mode
        if reserved_user_id is not None:
            self.reserved_user_id = reserved_user_id
        if client_ip is not None:
            self.client_ip = client_ip
        if type is not None:
            self.type = type
        if optlock is not None:
            self.optlock = optlock
        if entity_attributes is not None:
            self.entity_attributes = entity_attributes
        if entity_properties is not None:
            self.entity_properties = entity_properties
        if modified_on is not None:
            self.modified_on = modified_on
        if modified_by is not None:
            self.modified_by = modified_by
        if scope_id is not None:
            self.scope_id = scope_id
        if id is not None:
            self.id = id
        if created_on is not None:
            self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by

    @property
    def protocol(self):
        """Gets the protocol of this DeviceConnection.  # noqa: E501


        :return: The protocol of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DeviceConnection.


        :param protocol: The protocol of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def status(self):
        """Gets the status of this DeviceConnection.  # noqa: E501


        :return: The status of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeviceConnection.


        :param status: The status of this DeviceConnection.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONNECTED", "DISCONNECTED", "MISSING", "NULL"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this DeviceConnection.  # noqa: E501


        :return: The user_id of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DeviceConnection.


        :param user_id: The user_id of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def client_id(self):
        """Gets the client_id of this DeviceConnection.  # noqa: E501


        :return: The client_id of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this DeviceConnection.


        :param client_id: The client_id of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def server_ip(self):
        """Gets the server_ip of this DeviceConnection.  # noqa: E501


        :return: The server_ip of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        """Sets the server_ip of this DeviceConnection.


        :param server_ip: The server_ip of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._server_ip = server_ip

    @property
    def allow_user_change(self):
        """Gets the allow_user_change of this DeviceConnection.  # noqa: E501


        :return: The allow_user_change of this DeviceConnection.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_change

    @allow_user_change.setter
    def allow_user_change(self, allow_user_change):
        """Sets the allow_user_change of this DeviceConnection.


        :param allow_user_change: The allow_user_change of this DeviceConnection.  # noqa: E501
        :type: bool
        """

        self._allow_user_change = allow_user_change

    @property
    def user_coupling_mode(self):
        """Gets the user_coupling_mode of this DeviceConnection.  # noqa: E501


        :return: The user_coupling_mode of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._user_coupling_mode

    @user_coupling_mode.setter
    def user_coupling_mode(self, user_coupling_mode):
        """Sets the user_coupling_mode of this DeviceConnection.


        :param user_coupling_mode: The user_coupling_mode of this DeviceConnection.  # noqa: E501
        :type: str
        """
        allowed_values = ["INHERITED", "LOOSE", "STRICT"]  # noqa: E501
        if user_coupling_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `user_coupling_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(user_coupling_mode, allowed_values)
            )

        self._user_coupling_mode = user_coupling_mode

    @property
    def reserved_user_id(self):
        """Gets the reserved_user_id of this DeviceConnection.  # noqa: E501


        :return: The reserved_user_id of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._reserved_user_id

    @reserved_user_id.setter
    def reserved_user_id(self, reserved_user_id):
        """Sets the reserved_user_id of this DeviceConnection.


        :param reserved_user_id: The reserved_user_id of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._reserved_user_id = reserved_user_id

    @property
    def client_ip(self):
        """Gets the client_ip of this DeviceConnection.  # noqa: E501


        :return: The client_ip of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this DeviceConnection.


        :param client_ip: The client_ip of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._client_ip = client_ip

    @property
    def type(self):
        """Gets the type of this DeviceConnection.  # noqa: E501


        :return: The type of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceConnection.


        :param type: The type of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def optlock(self):
        """Gets the optlock of this DeviceConnection.  # noqa: E501


        :return: The optlock of this DeviceConnection.  # noqa: E501
        :rtype: int
        """
        return self._optlock

    @optlock.setter
    def optlock(self, optlock):
        """Sets the optlock of this DeviceConnection.


        :param optlock: The optlock of this DeviceConnection.  # noqa: E501
        :type: int
        """

        self._optlock = optlock

    @property
    def entity_attributes(self):
        """Gets the entity_attributes of this DeviceConnection.  # noqa: E501


        :return: The entity_attributes of this DeviceConnection.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._entity_attributes

    @entity_attributes.setter
    def entity_attributes(self, entity_attributes):
        """Sets the entity_attributes of this DeviceConnection.


        :param entity_attributes: The entity_attributes of this DeviceConnection.  # noqa: E501
        :type: dict(str, str)
        """

        self._entity_attributes = entity_attributes

    @property
    def entity_properties(self):
        """Gets the entity_properties of this DeviceConnection.  # noqa: E501


        :return: The entity_properties of this DeviceConnection.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._entity_properties

    @entity_properties.setter
    def entity_properties(self, entity_properties):
        """Sets the entity_properties of this DeviceConnection.


        :param entity_properties: The entity_properties of this DeviceConnection.  # noqa: E501
        :type: dict(str, str)
        """

        self._entity_properties = entity_properties

    @property
    def modified_on(self):
        """Gets the modified_on of this DeviceConnection.  # noqa: E501


        :return: The modified_on of this DeviceConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this DeviceConnection.


        :param modified_on: The modified_on of this DeviceConnection.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def modified_by(self):
        """Gets the modified_by of this DeviceConnection.  # noqa: E501


        :return: The modified_by of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this DeviceConnection.


        :param modified_by: The modified_by of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def scope_id(self):
        """Gets the scope_id of this DeviceConnection.  # noqa: E501


        :return: The scope_id of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this DeviceConnection.


        :param scope_id: The scope_id of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def id(self):
        """Gets the id of this DeviceConnection.  # noqa: E501


        :return: The id of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceConnection.


        :param id: The id of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this DeviceConnection.  # noqa: E501


        :return: The created_on of this DeviceConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceConnection.


        :param created_on: The created_on of this DeviceConnection.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this DeviceConnection.  # noqa: E501


        :return: The created_by of this DeviceConnection.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DeviceConnection.


        :param created_by: The created_by of this DeviceConnection.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
        if issubclass(DeviceConnection, dict):
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
        if not isinstance(other, DeviceConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
