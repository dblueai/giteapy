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


class Comment(object):
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
        'body': 'str',
        'created_at': 'datetime',
        'html_url': 'str',
        'id': 'int',
        'issue_url': 'str',
        'original_author': 'str',
        'original_author_id': 'int',
        'pull_request_url': 'str',
        'updated_at': 'datetime',
        'user': 'User'
    }

    attribute_map = {
        'body': 'body',
        'created_at': 'created_at',
        'html_url': 'html_url',
        'id': 'id',
        'issue_url': 'issue_url',
        'original_author': 'original_author',
        'original_author_id': 'original_author_id',
        'pull_request_url': 'pull_request_url',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, body=None, created_at=None, html_url=None, id=None, issue_url=None, original_author=None, original_author_id=None, pull_request_url=None, updated_at=None, user=None, _configuration=None):  # noqa: E501
        """Comment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._created_at = None
        self._html_url = None
        self._id = None
        self._issue_url = None
        self._original_author = None
        self._original_author_id = None
        self._pull_request_url = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if created_at is not None:
            self.created_at = created_at
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if issue_url is not None:
            self.issue_url = issue_url
        if original_author is not None:
            self.original_author = original_author
        if original_author_id is not None:
            self.original_author_id = original_author_id
        if pull_request_url is not None:
            self.pull_request_url = pull_request_url
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def body(self):
        """Gets the body of this Comment.  # noqa: E501


        :return: The body of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Comment.


        :param body: The body of this Comment.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def created_at(self):
        """Gets the created_at of this Comment.  # noqa: E501


        :return: The created_at of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Comment.


        :param created_at: The created_at of this Comment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def html_url(self):
        """Gets the html_url of this Comment.  # noqa: E501


        :return: The html_url of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this Comment.


        :param html_url: The html_url of this Comment.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501


        :return: The id of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.


        :param id: The id of this Comment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def issue_url(self):
        """Gets the issue_url of this Comment.  # noqa: E501


        :return: The issue_url of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._issue_url

    @issue_url.setter
    def issue_url(self, issue_url):
        """Sets the issue_url of this Comment.


        :param issue_url: The issue_url of this Comment.  # noqa: E501
        :type: str
        """

        self._issue_url = issue_url

    @property
    def original_author(self):
        """Gets the original_author of this Comment.  # noqa: E501


        :return: The original_author of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._original_author

    @original_author.setter
    def original_author(self, original_author):
        """Sets the original_author of this Comment.


        :param original_author: The original_author of this Comment.  # noqa: E501
        :type: str
        """

        self._original_author = original_author

    @property
    def original_author_id(self):
        """Gets the original_author_id of this Comment.  # noqa: E501


        :return: The original_author_id of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._original_author_id

    @original_author_id.setter
    def original_author_id(self, original_author_id):
        """Sets the original_author_id of this Comment.


        :param original_author_id: The original_author_id of this Comment.  # noqa: E501
        :type: int
        """

        self._original_author_id = original_author_id

    @property
    def pull_request_url(self):
        """Gets the pull_request_url of this Comment.  # noqa: E501


        :return: The pull_request_url of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._pull_request_url

    @pull_request_url.setter
    def pull_request_url(self, pull_request_url):
        """Sets the pull_request_url of this Comment.


        :param pull_request_url: The pull_request_url of this Comment.  # noqa: E501
        :type: str
        """

        self._pull_request_url = pull_request_url

    @property
    def updated_at(self):
        """Gets the updated_at of this Comment.  # noqa: E501


        :return: The updated_at of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Comment.


        :param updated_at: The updated_at of this Comment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this Comment.  # noqa: E501


        :return: The user of this Comment.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Comment.


        :param user: The user of this Comment.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(Comment, dict):
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
        if not isinstance(other, Comment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Comment):
            return True

        return self.to_dict() != other.to_dict()
