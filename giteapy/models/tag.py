# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.19.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class Tag(object):
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
        'commit': 'CommitMeta',
        'id': 'str',
        'message': 'str',
        'name': 'str',
        'tarball_url': 'str',
        'zipball_url': 'str'
    }

    attribute_map = {
        'commit': 'commit',
        'id': 'id',
        'message': 'message',
        'name': 'name',
        'tarball_url': 'tarball_url',
        'zipball_url': 'zipball_url'
    }

    def __init__(self, commit=None, id=None, message=None, name=None, tarball_url=None, zipball_url=None, _configuration=None):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._commit = None
        self._id = None
        self._message = None
        self._name = None
        self._tarball_url = None
        self._zipball_url = None
        self.discriminator = None

        if commit is not None:
            self.commit = commit
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if tarball_url is not None:
            self.tarball_url = tarball_url
        if zipball_url is not None:
            self.zipball_url = zipball_url

    @property
    def commit(self):
        """Gets the commit of this Tag.  # noqa: E501


        :return: The commit of this Tag.  # noqa: E501
        :rtype: CommitMeta
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this Tag.


        :param commit: The commit of this Tag.  # noqa: E501
        :type: CommitMeta
        """

        self._commit = commit

    @property
    def id(self):
        """Gets the id of this Tag.  # noqa: E501


        :return: The id of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.


        :param id: The id of this Tag.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this Tag.  # noqa: E501


        :return: The message of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Tag.


        :param message: The message of this Tag.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501


        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.


        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tarball_url(self):
        """Gets the tarball_url of this Tag.  # noqa: E501


        :return: The tarball_url of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._tarball_url

    @tarball_url.setter
    def tarball_url(self, tarball_url):
        """Sets the tarball_url of this Tag.


        :param tarball_url: The tarball_url of this Tag.  # noqa: E501
        :type: str
        """

        self._tarball_url = tarball_url

    @property
    def zipball_url(self):
        """Gets the zipball_url of this Tag.  # noqa: E501


        :return: The zipball_url of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._zipball_url

    @zipball_url.setter
    def zipball_url(self, zipball_url):
        """Sets the zipball_url of this Tag.


        :param zipball_url: The zipball_url of this Tag.  # noqa: E501
        :type: str
        """

        self._zipball_url = zipball_url

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
        if issubclass(Tag, dict):
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
        if not isinstance(other, Tag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tag):
            return True

        return self.to_dict() != other.to_dict()
