# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Model(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, model=None):  # noqa: E501
        """Model - a model defined in OpenAPI

        :param model: The model of this Model.  # noqa: E501
        :type model: str
        """
        self.openapi_types = {
            'model': str
        }

        self.attribute_map = {
            'model': 'model'
        }

        self._model = model

    @classmethod
    def from_dict(cls, dikt) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.  # noqa: E501
        :rtype: Model
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model(self):
        """Gets the model of this Model.


        :return: The model of this Model.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Model.


        :param model: The model of this Model.
        :type model: str
        """

        self._model = model
