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


class CreateBranchRepoOption(object):
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
        'new_branch_name': 'str',
        'old_branch_name': 'str'
    }

    attribute_map = {
        'new_branch_name': 'new_branch_name',
        'old_branch_name': 'old_branch_name'
    }

    def __init__(self, new_branch_name=None, old_branch_name=None, _configuration=None):  # noqa: E501
        """CreateBranchRepoOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_branch_name = None
        self._old_branch_name = None
        self.discriminator = None

        self.new_branch_name = new_branch_name
        if old_branch_name is not None:
            self.old_branch_name = old_branch_name

    @property
    def new_branch_name(self):
        """Gets the new_branch_name of this CreateBranchRepoOption.  # noqa: E501

        Name of the branch to create  # noqa: E501

        :return: The new_branch_name of this CreateBranchRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._new_branch_name

    @new_branch_name.setter
    def new_branch_name(self, new_branch_name):
        """Sets the new_branch_name of this CreateBranchRepoOption.

        Name of the branch to create  # noqa: E501

        :param new_branch_name: The new_branch_name of this CreateBranchRepoOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and new_branch_name is None:
            raise ValueError("Invalid value for `new_branch_name`, must not be `None`")  # noqa: E501

        self._new_branch_name = new_branch_name

    @property
    def old_branch_name(self):
        """Gets the old_branch_name of this CreateBranchRepoOption.  # noqa: E501

        Name of the old branch to create from  # noqa: E501

        :return: The old_branch_name of this CreateBranchRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._old_branch_name

    @old_branch_name.setter
    def old_branch_name(self, old_branch_name):
        """Sets the old_branch_name of this CreateBranchRepoOption.

        Name of the old branch to create from  # noqa: E501

        :param old_branch_name: The old_branch_name of this CreateBranchRepoOption.  # noqa: E501
        :type: str
        """

        self._old_branch_name = old_branch_name

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
        if issubclass(CreateBranchRepoOption, dict):
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
        if not isinstance(other, CreateBranchRepoOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateBranchRepoOption):
            return True

        return self.to_dict() != other.to_dict()
