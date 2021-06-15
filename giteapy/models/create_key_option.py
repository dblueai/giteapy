# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class CreateKeyOption(object):
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
        'key': 'str',
        'read_only': 'bool',
        'title': 'str'
    }

    attribute_map = {
        'key': 'key',
        'read_only': 'read_only',
        'title': 'title'
    }

    def __init__(self, key=None, read_only=None, title=None, _configuration=None):  # noqa: E501
        """CreateKeyOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._read_only = None
        self._title = None
        self.discriminator = None

        self.key = key
        if read_only is not None:
            self.read_only = read_only
        self.title = title

    @property
    def key(self):
        """Gets the key of this CreateKeyOption.  # noqa: E501

        An armored SSH key to add  # noqa: E501

        :return: The key of this CreateKeyOption.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateKeyOption.

        An armored SSH key to add  # noqa: E501

        :param key: The key of this CreateKeyOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def read_only(self):
        """Gets the read_only of this CreateKeyOption.  # noqa: E501

        Describe if the key has only read access or read/write  # noqa: E501

        :return: The read_only of this CreateKeyOption.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this CreateKeyOption.

        Describe if the key has only read access or read/write  # noqa: E501

        :param read_only: The read_only of this CreateKeyOption.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def title(self):
        """Gets the title of this CreateKeyOption.  # noqa: E501

        Title of the key to add  # noqa: E501

        :return: The title of this CreateKeyOption.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateKeyOption.

        Title of the key to add  # noqa: E501

        :param title: The title of this CreateKeyOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

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
        if issubclass(CreateKeyOption, dict):
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
        if not isinstance(other, CreateKeyOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateKeyOption):
            return True

        return self.to_dict() != other.to_dict()
