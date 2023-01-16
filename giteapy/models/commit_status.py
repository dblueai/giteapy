# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class CommitStatus(object):
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
        'context': 'str',
        'created_at': 'datetime',
        'creator': 'User',
        'description': 'str',
        'id': 'int',
        'status': 'CommitStatusState',
        'target_url': 'str',
        'updated_at': 'datetime',
        'url': 'str'
    }

    attribute_map = {
        'context': 'context',
        'created_at': 'created_at',
        'creator': 'creator',
        'description': 'description',
        'id': 'id',
        'status': 'status',
        'target_url': 'target_url',
        'updated_at': 'updated_at',
        'url': 'url'
    }

    def __init__(self, context=None, created_at=None, creator=None, description=None, id=None, status=None, target_url=None, updated_at=None, url=None, _configuration=None):  # noqa: E501
        """CommitStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._context = None
        self._created_at = None
        self._creator = None
        self._description = None
        self._id = None
        self._status = None
        self._target_url = None
        self._updated_at = None
        self._url = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if created_at is not None:
            self.created_at = created_at
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if target_url is not None:
            self.target_url = target_url
        if updated_at is not None:
            self.updated_at = updated_at
        if url is not None:
            self.url = url

    @property
    def context(self):
        """Gets the context of this CommitStatus.  # noqa: E501


        :return: The context of this CommitStatus.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this CommitStatus.


        :param context: The context of this CommitStatus.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def created_at(self):
        """Gets the created_at of this CommitStatus.  # noqa: E501


        :return: The created_at of this CommitStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CommitStatus.


        :param created_at: The created_at of this CommitStatus.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def creator(self):
        """Gets the creator of this CommitStatus.  # noqa: E501


        :return: The creator of this CommitStatus.  # noqa: E501
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this CommitStatus.


        :param creator: The creator of this CommitStatus.  # noqa: E501
        :type: User
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this CommitStatus.  # noqa: E501


        :return: The description of this CommitStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommitStatus.


        :param description: The description of this CommitStatus.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this CommitStatus.  # noqa: E501


        :return: The id of this CommitStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommitStatus.


        :param id: The id of this CommitStatus.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this CommitStatus.  # noqa: E501


        :return: The status of this CommitStatus.  # noqa: E501
        :rtype: CommitStatusState
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CommitStatus.


        :param status: The status of this CommitStatus.  # noqa: E501
        :type: CommitStatusState
        """

        self._status = status

    @property
    def target_url(self):
        """Gets the target_url of this CommitStatus.  # noqa: E501


        :return: The target_url of this CommitStatus.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this CommitStatus.


        :param target_url: The target_url of this CommitStatus.  # noqa: E501
        :type: str
        """

        self._target_url = target_url

    @property
    def updated_at(self):
        """Gets the updated_at of this CommitStatus.  # noqa: E501


        :return: The updated_at of this CommitStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CommitStatus.


        :param updated_at: The updated_at of this CommitStatus.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this CommitStatus.  # noqa: E501


        :return: The url of this CommitStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CommitStatus.


        :param url: The url of this CommitStatus.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(CommitStatus, dict):
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
        if not isinstance(other, CommitStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommitStatus):
            return True

        return self.to_dict() != other.to_dict()
