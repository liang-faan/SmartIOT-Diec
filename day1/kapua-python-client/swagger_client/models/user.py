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


class User(object):
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
        'display_name': 'str',
        'email': 'str',
        'phone_number': 'str',
        'status': 'str',
        'expiration_date': 'datetime',
        'user_type': 'str',
        'external_id': 'str',
        'type': 'str',
        'name': 'str',
        'modified_on': 'datetime',
        'modified_by': 'str',
        'optlock': 'int',
        'entity_attributes': 'dict(str, str)',
        'entity_properties': 'dict(str, str)',
        'scope_id': 'str',
        'id': 'str',
        'created_on': 'datetime',
        'created_by': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'email': 'email',
        'phone_number': 'phoneNumber',
        'status': 'status',
        'expiration_date': 'expirationDate',
        'user_type': 'userType',
        'external_id': 'externalId',
        'type': 'type',
        'name': 'name',
        'modified_on': 'modifiedOn',
        'modified_by': 'modifiedBy',
        'optlock': 'optlock',
        'entity_attributes': 'entityAttributes',
        'entity_properties': 'entityProperties',
        'scope_id': 'scopeId',
        'id': 'id',
        'created_on': 'createdOn',
        'created_by': 'createdBy'
    }

    def __init__(self, display_name=None, email=None, phone_number=None, status=None, expiration_date=None, user_type=None, external_id=None, type=None, name=None, modified_on=None, modified_by=None, optlock=None, entity_attributes=None, entity_properties=None, scope_id=None, id=None, created_on=None, created_by=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._email = None
        self._phone_number = None
        self._status = None
        self._expiration_date = None
        self._user_type = None
        self._external_id = None
        self._type = None
        self._name = None
        self._modified_on = None
        self._modified_by = None
        self._optlock = None
        self._entity_attributes = None
        self._entity_properties = None
        self._scope_id = None
        self._id = None
        self._created_on = None
        self._created_by = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if status is not None:
            self.status = status
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if user_type is not None:
            self.user_type = user_type
        if external_id is not None:
            self.external_id = external_id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if modified_on is not None:
            self.modified_on = modified_on
        if modified_by is not None:
            self.modified_by = modified_by
        if optlock is not None:
            self.optlock = optlock
        if entity_attributes is not None:
            self.entity_attributes = entity_attributes
        if entity_properties is not None:
            self.entity_properties = entity_properties
        if scope_id is not None:
            self.scope_id = scope_id
        if id is not None:
            self.id = id
        if created_on is not None:
            self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by

    @property
    def display_name(self):
        """Gets the display_name of this User.  # noqa: E501


        :return: The display_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this User.


        :param display_name: The display_name of this User.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """Gets the phone_number of this User.  # noqa: E501


        :return: The phone_number of this User.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this User.


        :param phone_number: The phone_number of this User.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def status(self):
        """Gets the status of this User.  # noqa: E501


        :return: The status of this User.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this User.


        :param status: The status of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def expiration_date(self):
        """Gets the expiration_date of this User.  # noqa: E501


        :return: The expiration_date of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this User.


        :param expiration_date: The expiration_date of this User.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def user_type(self):
        """Gets the user_type of this User.  # noqa: E501


        :return: The user_type of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this User.


        :param user_type: The user_type of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEVICE", "INTERNAL", "EXTERNAL"]  # noqa: E501
        if user_type not in allowed_values:
            raise ValueError(
                "Invalid value for `user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(user_type, allowed_values)
            )

        self._user_type = user_type

    @property
    def external_id(self):
        """Gets the external_id of this User.  # noqa: E501


        :return: The external_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this User.


        :param external_id: The external_id of this User.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def type(self):
        """Gets the type of this User.  # noqa: E501


        :return: The type of this User.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this User.


        :param type: The type of this User.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def modified_on(self):
        """Gets the modified_on of this User.  # noqa: E501


        :return: The modified_on of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this User.


        :param modified_on: The modified_on of this User.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def modified_by(self):
        """Gets the modified_by of this User.  # noqa: E501


        :return: The modified_by of this User.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this User.


        :param modified_by: The modified_by of this User.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def optlock(self):
        """Gets the optlock of this User.  # noqa: E501


        :return: The optlock of this User.  # noqa: E501
        :rtype: int
        """
        return self._optlock

    @optlock.setter
    def optlock(self, optlock):
        """Sets the optlock of this User.


        :param optlock: The optlock of this User.  # noqa: E501
        :type: int
        """

        self._optlock = optlock

    @property
    def entity_attributes(self):
        """Gets the entity_attributes of this User.  # noqa: E501


        :return: The entity_attributes of this User.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._entity_attributes

    @entity_attributes.setter
    def entity_attributes(self, entity_attributes):
        """Sets the entity_attributes of this User.


        :param entity_attributes: The entity_attributes of this User.  # noqa: E501
        :type: dict(str, str)
        """

        self._entity_attributes = entity_attributes

    @property
    def entity_properties(self):
        """Gets the entity_properties of this User.  # noqa: E501


        :return: The entity_properties of this User.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._entity_properties

    @entity_properties.setter
    def entity_properties(self, entity_properties):
        """Sets the entity_properties of this User.


        :param entity_properties: The entity_properties of this User.  # noqa: E501
        :type: dict(str, str)
        """

        self._entity_properties = entity_properties

    @property
    def scope_id(self):
        """Gets the scope_id of this User.  # noqa: E501


        :return: The scope_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this User.


        :param scope_id: The scope_id of this User.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this User.  # noqa: E501


        :return: The created_on of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this User.


        :param created_on: The created_on of this User.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this User.  # noqa: E501


        :return: The created_by of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this User.


        :param created_by: The created_by of this User.  # noqa: E501
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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
