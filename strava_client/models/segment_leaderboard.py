# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SegmentLeaderboard(object):
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
        'entry_count': 'int',
        'effort_count': 'int',
        'kom_type': 'str',
        'entries': 'list[SegmentLeaderboardEntry]'
    }

    attribute_map = {
        'entry_count': 'entry_count',
        'effort_count': 'effort_count',
        'kom_type': 'kom_type',
        'entries': 'entries'
    }

    def __init__(self, entry_count=None, effort_count=None, kom_type=None, entries=None):  # noqa: E501
        """SegmentLeaderboard - a model defined in Swagger"""  # noqa: E501
        self._entry_count = None
        self._effort_count = None
        self._kom_type = None
        self._entries = None
        self.discriminator = None
        if entry_count is not None:
            self.entry_count = entry_count
        if effort_count is not None:
            self.effort_count = effort_count
        if kom_type is not None:
            self.kom_type = kom_type
        if entries is not None:
            self.entries = entries

    @property
    def entry_count(self):
        """Gets the entry_count of this SegmentLeaderboard.  # noqa: E501

        The total number of entries for this leaderboard  # noqa: E501

        :return: The entry_count of this SegmentLeaderboard.  # noqa: E501
        :rtype: int
        """
        return self._entry_count

    @entry_count.setter
    def entry_count(self, entry_count):
        """Sets the entry_count of this SegmentLeaderboard.

        The total number of entries for this leaderboard  # noqa: E501

        :param entry_count: The entry_count of this SegmentLeaderboard.  # noqa: E501
        :type: int
        """

        self._entry_count = entry_count

    @property
    def effort_count(self):
        """Gets the effort_count of this SegmentLeaderboard.  # noqa: E501

        Deprecated, use entry_count  # noqa: E501

        :return: The effort_count of this SegmentLeaderboard.  # noqa: E501
        :rtype: int
        """
        return self._effort_count

    @effort_count.setter
    def effort_count(self, effort_count):
        """Sets the effort_count of this SegmentLeaderboard.

        Deprecated, use entry_count  # noqa: E501

        :param effort_count: The effort_count of this SegmentLeaderboard.  # noqa: E501
        :type: int
        """

        self._effort_count = effort_count

    @property
    def kom_type(self):
        """Gets the kom_type of this SegmentLeaderboard.  # noqa: E501


        :return: The kom_type of this SegmentLeaderboard.  # noqa: E501
        :rtype: str
        """
        return self._kom_type

    @kom_type.setter
    def kom_type(self, kom_type):
        """Sets the kom_type of this SegmentLeaderboard.


        :param kom_type: The kom_type of this SegmentLeaderboard.  # noqa: E501
        :type: str
        """
        allowed_values = ["kom", "cr"]  # noqa: E501
        if kom_type not in allowed_values:
            raise ValueError(
                "Invalid value for `kom_type` ({0}), must be one of {1}"  # noqa: E501
                .format(kom_type, allowed_values)
            )

        self._kom_type = kom_type

    @property
    def entries(self):
        """Gets the entries of this SegmentLeaderboard.  # noqa: E501


        :return: The entries of this SegmentLeaderboard.  # noqa: E501
        :rtype: list[SegmentLeaderboardEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this SegmentLeaderboard.


        :param entries: The entries of this SegmentLeaderboard.  # noqa: E501
        :type: list[SegmentLeaderboardEntry]
        """

        self._entries = entries

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
        if issubclass(SegmentLeaderboard, dict):
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
        if not isinstance(other, SegmentLeaderboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
