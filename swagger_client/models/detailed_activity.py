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


class DetailedActivity(object):
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
        'description': 'str',
        'photos': 'PhotosSummary',
        'gear': 'SummaryGear',
        'calories': 'float',
        'segment_efforts': 'list[DetailedSegmentEffort]',
        'device_name': 'str',
        'embed_token': 'str',
        'splits_metric': 'list[Split]',
        'splits_standard': 'list[Split]',
        'laps': 'list[Lap]',
        'best_efforts': 'list[DetailedSegmentEffort]'
    }
    if hasattr(SummaryActivity, "swagger_types"):
        swagger_types.update(SummaryActivity.swagger_types)

    attribute_map = {
        'description': 'description',
        'photos': 'photos',
        'gear': 'gear',
        'calories': 'calories',
        'segment_efforts': 'segment_efforts',
        'device_name': 'device_name',
        'embed_token': 'embed_token',
        'splits_metric': 'splits_metric',
        'splits_standard': 'splits_standard',
        'laps': 'laps',
        'best_efforts': 'best_efforts'
    }
    if hasattr(SummaryActivity, "attribute_map"):
        attribute_map.update(SummaryActivity.attribute_map)

    def __init__(self, description=None, photos=None, gear=None, calories=None, segment_efforts=None, device_name=None, embed_token=None, splits_metric=None, splits_standard=None, laps=None, best_efforts=None, *args, **kwargs):  # noqa: E501
        """DetailedActivity - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._photos = None
        self._gear = None
        self._calories = None
        self._segment_efforts = None
        self._device_name = None
        self._embed_token = None
        self._splits_metric = None
        self._splits_standard = None
        self._laps = None
        self._best_efforts = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if photos is not None:
            self.photos = photos
        if gear is not None:
            self.gear = gear
        if calories is not None:
            self.calories = calories
        if segment_efforts is not None:
            self.segment_efforts = segment_efforts
        if device_name is not None:
            self.device_name = device_name
        if embed_token is not None:
            self.embed_token = embed_token
        if splits_metric is not None:
            self.splits_metric = splits_metric
        if splits_standard is not None:
            self.splits_standard = splits_standard
        if laps is not None:
            self.laps = laps
        if best_efforts is not None:
            self.best_efforts = best_efforts
        SummaryActivity.__init__(self, *args, **kwargs)

    @property
    def description(self):
        """Gets the description of this DetailedActivity.  # noqa: E501

        The description of the activity  # noqa: E501

        :return: The description of this DetailedActivity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DetailedActivity.

        The description of the activity  # noqa: E501

        :param description: The description of this DetailedActivity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def photos(self):
        """Gets the photos of this DetailedActivity.  # noqa: E501


        :return: The photos of this DetailedActivity.  # noqa: E501
        :rtype: PhotosSummary
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this DetailedActivity.


        :param photos: The photos of this DetailedActivity.  # noqa: E501
        :type: PhotosSummary
        """

        self._photos = photos

    @property
    def gear(self):
        """Gets the gear of this DetailedActivity.  # noqa: E501


        :return: The gear of this DetailedActivity.  # noqa: E501
        :rtype: SummaryGear
        """
        return self._gear

    @gear.setter
    def gear(self, gear):
        """Sets the gear of this DetailedActivity.


        :param gear: The gear of this DetailedActivity.  # noqa: E501
        :type: SummaryGear
        """

        self._gear = gear

    @property
    def calories(self):
        """Gets the calories of this DetailedActivity.  # noqa: E501

        The number of kilocalories consumed during this activity  # noqa: E501

        :return: The calories of this DetailedActivity.  # noqa: E501
        :rtype: float
        """
        return self._calories

    @calories.setter
    def calories(self, calories):
        """Sets the calories of this DetailedActivity.

        The number of kilocalories consumed during this activity  # noqa: E501

        :param calories: The calories of this DetailedActivity.  # noqa: E501
        :type: float
        """

        self._calories = calories

    @property
    def segment_efforts(self):
        """Gets the segment_efforts of this DetailedActivity.  # noqa: E501


        :return: The segment_efforts of this DetailedActivity.  # noqa: E501
        :rtype: list[DetailedSegmentEffort]
        """
        return self._segment_efforts

    @segment_efforts.setter
    def segment_efforts(self, segment_efforts):
        """Sets the segment_efforts of this DetailedActivity.


        :param segment_efforts: The segment_efforts of this DetailedActivity.  # noqa: E501
        :type: list[DetailedSegmentEffort]
        """

        self._segment_efforts = segment_efforts

    @property
    def device_name(self):
        """Gets the device_name of this DetailedActivity.  # noqa: E501

        The name of the device used to record the activity  # noqa: E501

        :return: The device_name of this DetailedActivity.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this DetailedActivity.

        The name of the device used to record the activity  # noqa: E501

        :param device_name: The device_name of this DetailedActivity.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def embed_token(self):
        """Gets the embed_token of this DetailedActivity.  # noqa: E501

        The token used to embed a Strava activity  # noqa: E501

        :return: The embed_token of this DetailedActivity.  # noqa: E501
        :rtype: str
        """
        return self._embed_token

    @embed_token.setter
    def embed_token(self, embed_token):
        """Sets the embed_token of this DetailedActivity.

        The token used to embed a Strava activity  # noqa: E501

        :param embed_token: The embed_token of this DetailedActivity.  # noqa: E501
        :type: str
        """

        self._embed_token = embed_token

    @property
    def splits_metric(self):
        """Gets the splits_metric of this DetailedActivity.  # noqa: E501

        The splits of this activity in metric units (for runs)  # noqa: E501

        :return: The splits_metric of this DetailedActivity.  # noqa: E501
        :rtype: list[Split]
        """
        return self._splits_metric

    @splits_metric.setter
    def splits_metric(self, splits_metric):
        """Sets the splits_metric of this DetailedActivity.

        The splits of this activity in metric units (for runs)  # noqa: E501

        :param splits_metric: The splits_metric of this DetailedActivity.  # noqa: E501
        :type: list[Split]
        """

        self._splits_metric = splits_metric

    @property
    def splits_standard(self):
        """Gets the splits_standard of this DetailedActivity.  # noqa: E501

        The splits of this activity in imperial units (for runs)  # noqa: E501

        :return: The splits_standard of this DetailedActivity.  # noqa: E501
        :rtype: list[Split]
        """
        return self._splits_standard

    @splits_standard.setter
    def splits_standard(self, splits_standard):
        """Sets the splits_standard of this DetailedActivity.

        The splits of this activity in imperial units (for runs)  # noqa: E501

        :param splits_standard: The splits_standard of this DetailedActivity.  # noqa: E501
        :type: list[Split]
        """

        self._splits_standard = splits_standard

    @property
    def laps(self):
        """Gets the laps of this DetailedActivity.  # noqa: E501


        :return: The laps of this DetailedActivity.  # noqa: E501
        :rtype: list[Lap]
        """
        return self._laps

    @laps.setter
    def laps(self, laps):
        """Sets the laps of this DetailedActivity.


        :param laps: The laps of this DetailedActivity.  # noqa: E501
        :type: list[Lap]
        """

        self._laps = laps

    @property
    def best_efforts(self):
        """Gets the best_efforts of this DetailedActivity.  # noqa: E501


        :return: The best_efforts of this DetailedActivity.  # noqa: E501
        :rtype: list[DetailedSegmentEffort]
        """
        return self._best_efforts

    @best_efforts.setter
    def best_efforts(self, best_efforts):
        """Sets the best_efforts of this DetailedActivity.


        :param best_efforts: The best_efforts of this DetailedActivity.  # noqa: E501
        :type: list[DetailedSegmentEffort]
        """

        self._best_efforts = best_efforts

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
        if issubclass(DetailedActivity, dict):
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
        if not isinstance(other, DetailedActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
