# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SubmitPullReviewOptions(object):
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
        'event': 'ReviewStateType'
    }

    attribute_map = {
        'body': 'body',
        'event': 'event'
    }

    def __init__(self, body=None, event=None):  # noqa: E501
        """SubmitPullReviewOptions - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._event = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if event is not None:
            self.event = event

    @property
    def body(self):
        """Gets the body of this SubmitPullReviewOptions.  # noqa: E501


        :return: The body of this SubmitPullReviewOptions.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SubmitPullReviewOptions.


        :param body: The body of this SubmitPullReviewOptions.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def event(self):
        """Gets the event of this SubmitPullReviewOptions.  # noqa: E501


        :return: The event of this SubmitPullReviewOptions.  # noqa: E501
        :rtype: ReviewStateType
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this SubmitPullReviewOptions.


        :param event: The event of this SubmitPullReviewOptions.  # noqa: E501
        :type: ReviewStateType
        """

        self._event = event

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
        if issubclass(SubmitPullReviewOptions, dict):
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
        if not isinstance(other, SubmitPullReviewOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
