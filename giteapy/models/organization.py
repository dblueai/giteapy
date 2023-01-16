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


class Organization(object):
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
        'avatar_url': 'str',
        'description': 'str',
        'full_name': 'str',
        'id': 'int',
        'location': 'str',
        'name': 'str',
        'repo_admin_change_team_access': 'bool',
        'username': 'str',
        'visibility': 'str',
        'website': 'str'
    }

    attribute_map = {
        'avatar_url': 'avatar_url',
        'description': 'description',
        'full_name': 'full_name',
        'id': 'id',
        'location': 'location',
        'name': 'name',
        'repo_admin_change_team_access': 'repo_admin_change_team_access',
        'username': 'username',
        'visibility': 'visibility',
        'website': 'website'
    }

    def __init__(self, avatar_url=None, description=None, full_name=None, id=None, location=None, name=None, repo_admin_change_team_access=None, username=None, visibility=None, website=None, _configuration=None):  # noqa: E501
        """Organization - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avatar_url = None
        self._description = None
        self._full_name = None
        self._id = None
        self._location = None
        self._name = None
        self._repo_admin_change_team_access = None
        self._username = None
        self._visibility = None
        self._website = None
        self.discriminator = None

        if avatar_url is not None:
            self.avatar_url = avatar_url
        if description is not None:
            self.description = description
        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if repo_admin_change_team_access is not None:
            self.repo_admin_change_team_access = repo_admin_change_team_access
        if username is not None:
            self.username = username
        if visibility is not None:
            self.visibility = visibility
        if website is not None:
            self.website = website

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Organization.  # noqa: E501


        :return: The avatar_url of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Organization.


        :param avatar_url: The avatar_url of this Organization.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def description(self):
        """Gets the description of this Organization.  # noqa: E501


        :return: The description of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Organization.


        :param description: The description of this Organization.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def full_name(self):
        """Gets the full_name of this Organization.  # noqa: E501


        :return: The full_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Organization.


        :param full_name: The full_name of this Organization.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501


        :return: The id of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this Organization.  # noqa: E501


        :return: The location of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Organization.


        :param location: The location of this Organization.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501


        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def repo_admin_change_team_access(self):
        """Gets the repo_admin_change_team_access of this Organization.  # noqa: E501


        :return: The repo_admin_change_team_access of this Organization.  # noqa: E501
        :rtype: bool
        """
        return self._repo_admin_change_team_access

    @repo_admin_change_team_access.setter
    def repo_admin_change_team_access(self, repo_admin_change_team_access):
        """Sets the repo_admin_change_team_access of this Organization.


        :param repo_admin_change_team_access: The repo_admin_change_team_access of this Organization.  # noqa: E501
        :type: bool
        """

        self._repo_admin_change_team_access = repo_admin_change_team_access

    @property
    def username(self):
        """Gets the username of this Organization.  # noqa: E501

        deprecated  # noqa: E501

        :return: The username of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Organization.

        deprecated  # noqa: E501

        :param username: The username of this Organization.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def visibility(self):
        """Gets the visibility of this Organization.  # noqa: E501


        :return: The visibility of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Organization.


        :param visibility: The visibility of this Organization.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def website(self):
        """Gets the website of this Organization.  # noqa: E501


        :return: The website of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Organization.


        :param website: The website of this Organization.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(Organization, dict):
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
        if not isinstance(other, Organization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Organization):
            return True

        return self.to_dict() != other.to_dict()
