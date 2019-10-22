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


class SummaryClub(object):
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
        'profile_medium': 'str',
        'cover_photo': 'str',
        'cover_photo_small': 'str',
        'sport_type': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'private': 'bool',
        'member_count': 'int',
        'featured': 'bool',
        'verified': 'bool',
        'url': 'str'
    }
    if hasattr(MetaClub, "swagger_types"):
        swagger_types.update(MetaClub.swagger_types)

    attribute_map = {
        'profile_medium': 'profile_medium',
        'cover_photo': 'cover_photo',
        'cover_photo_small': 'cover_photo_small',
        'sport_type': 'sport_type',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'private': 'private',
        'member_count': 'member_count',
        'featured': 'featured',
        'verified': 'verified',
        'url': 'url'
    }
    if hasattr(MetaClub, "attribute_map"):
        attribute_map.update(MetaClub.attribute_map)

    def __init__(self, profile_medium=None, cover_photo=None, cover_photo_small=None, sport_type=None, city=None, state=None, country=None, private=None, member_count=None, featured=None, verified=None, url=None, *args, **kwargs):  # noqa: E501
        """SummaryClub - a model defined in Swagger"""  # noqa: E501
        self._profile_medium = None
        self._cover_photo = None
        self._cover_photo_small = None
        self._sport_type = None
        self._city = None
        self._state = None
        self._country = None
        self._private = None
        self._member_count = None
        self._featured = None
        self._verified = None
        self._url = None
        self.discriminator = None
        if profile_medium is not None:
            self.profile_medium = profile_medium
        if cover_photo is not None:
            self.cover_photo = cover_photo
        if cover_photo_small is not None:
            self.cover_photo_small = cover_photo_small
        if sport_type is not None:
            self.sport_type = sport_type
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if private is not None:
            self.private = private
        if member_count is not None:
            self.member_count = member_count
        if featured is not None:
            self.featured = featured
        if verified is not None:
            self.verified = verified
        if url is not None:
            self.url = url
        MetaClub.__init__(self, *args, **kwargs)

    @property
    def profile_medium(self):
        """Gets the profile_medium of this SummaryClub.  # noqa: E501

        URL to a 60x60 pixel profile picture.  # noqa: E501

        :return: The profile_medium of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._profile_medium

    @profile_medium.setter
    def profile_medium(self, profile_medium):
        """Sets the profile_medium of this SummaryClub.

        URL to a 60x60 pixel profile picture.  # noqa: E501

        :param profile_medium: The profile_medium of this SummaryClub.  # noqa: E501
        :type: str
        """

        self._profile_medium = profile_medium

    @property
    def cover_photo(self):
        """Gets the cover_photo of this SummaryClub.  # noqa: E501

        URL to a ~1185x580 pixel cover photo.  # noqa: E501

        :return: The cover_photo of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._cover_photo

    @cover_photo.setter
    def cover_photo(self, cover_photo):
        """Sets the cover_photo of this SummaryClub.

        URL to a ~1185x580 pixel cover photo.  # noqa: E501

        :param cover_photo: The cover_photo of this SummaryClub.  # noqa: E501
        :type: str
        """

        self._cover_photo = cover_photo

    @property
    def cover_photo_small(self):
        """Gets the cover_photo_small of this SummaryClub.  # noqa: E501

        URL to a ~360x176  pixel cover photo.  # noqa: E501

        :return: The cover_photo_small of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._cover_photo_small

    @cover_photo_small.setter
    def cover_photo_small(self, cover_photo_small):
        """Sets the cover_photo_small of this SummaryClub.

        URL to a ~360x176  pixel cover photo.  # noqa: E501

        :param cover_photo_small: The cover_photo_small of this SummaryClub.  # noqa: E501
        :type: str
        """

        self._cover_photo_small = cover_photo_small

    @property
    def sport_type(self):
        """Gets the sport_type of this SummaryClub.  # noqa: E501


        :return: The sport_type of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._sport_type

    @sport_type.setter
    def sport_type(self, sport_type):
        """Sets the sport_type of this SummaryClub.


        :param sport_type: The sport_type of this SummaryClub.  # noqa: E501
        :type: str
        """
        allowed_values = ["cycling", "running", "triathlon", "other"]  # noqa: E501
        if sport_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sport_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sport_type, allowed_values)
            )

        self._sport_type = sport_type

    @property
    def city(self):
        """Gets the city of this SummaryClub.  # noqa: E501

        The club's city.  # noqa: E501

        :return: The city of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SummaryClub.

        The club's city.  # noqa: E501

        :param city: The city of this SummaryClub.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this SummaryClub.  # noqa: E501

        The club's state or geographical region.  # noqa: E501

        :return: The state of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SummaryClub.

        The club's state or geographical region.  # noqa: E501

        :param state: The state of this SummaryClub.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this SummaryClub.  # noqa: E501

        The club's country.  # noqa: E501

        :return: The country of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SummaryClub.

        The club's country.  # noqa: E501

        :param country: The country of this SummaryClub.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def private(self):
        """Gets the private of this SummaryClub.  # noqa: E501

        Whether the club is private.  # noqa: E501

        :return: The private of this SummaryClub.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this SummaryClub.

        Whether the club is private.  # noqa: E501

        :param private: The private of this SummaryClub.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def member_count(self):
        """Gets the member_count of this SummaryClub.  # noqa: E501

        The club's member count.  # noqa: E501

        :return: The member_count of this SummaryClub.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this SummaryClub.

        The club's member count.  # noqa: E501

        :param member_count: The member_count of this SummaryClub.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def featured(self):
        """Gets the featured of this SummaryClub.  # noqa: E501

        Whether the club is featured or not.  # noqa: E501

        :return: The featured of this SummaryClub.  # noqa: E501
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """Sets the featured of this SummaryClub.

        Whether the club is featured or not.  # noqa: E501

        :param featured: The featured of this SummaryClub.  # noqa: E501
        :type: bool
        """

        self._featured = featured

    @property
    def verified(self):
        """Gets the verified of this SummaryClub.  # noqa: E501

        Whether the club is verified or not.  # noqa: E501

        :return: The verified of this SummaryClub.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this SummaryClub.

        Whether the club is verified or not.  # noqa: E501

        :param verified: The verified of this SummaryClub.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def url(self):
        """Gets the url of this SummaryClub.  # noqa: E501

        The club's vanity URL.  # noqa: E501

        :return: The url of this SummaryClub.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SummaryClub.

        The club's vanity URL.  # noqa: E501

        :param url: The url of this SummaryClub.  # noqa: E501
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
        if issubclass(SummaryClub, dict):
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
        if not isinstance(other, SummaryClub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
