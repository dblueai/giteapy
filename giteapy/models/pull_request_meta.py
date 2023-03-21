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


class PullRequestMeta(object):
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
        'merged': 'bool',
        'merged_at': 'datetime'
    }

    attribute_map = {
        'merged': 'merged',
        'merged_at': 'merged_at'
    }

    def __init__(self, merged=None, merged_at=None, _configuration=None):  # noqa: E501
        """PullRequestMeta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._merged = None
        self._merged_at = None
        self.discriminator = None

        if merged is not None:
            self.merged = merged
        if merged_at is not None:
            self.merged_at = merged_at

    @property
    def merged(self):
        """Gets the merged of this PullRequestMeta.  # noqa: E501


        :return: The merged of this PullRequestMeta.  # noqa: E501
        :rtype: bool
        """
        return self._merged

    @merged.setter
    def merged(self, merged):
        """Sets the merged of this PullRequestMeta.


        :param merged: The merged of this PullRequestMeta.  # noqa: E501
        :type: bool
        """

        self._merged = merged

    @property
    def merged_at(self):
        """Gets the merged_at of this PullRequestMeta.  # noqa: E501


        :return: The merged_at of this PullRequestMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        """Sets the merged_at of this PullRequestMeta.


        :param merged_at: The merged_at of this PullRequestMeta.  # noqa: E501
        :type: datetime
        """

        self._merged_at = merged_at

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
        if issubclass(PullRequestMeta, dict):
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
        if not isinstance(other, PullRequestMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PullRequestMeta):
            return True

        return self.to_dict() != other.to_dict()
