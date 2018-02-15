# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.event_dto

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class EventDto(object):

    """Implementation of the 'EventDto' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        mtype (string): TODO: type description here.
        payload (object): TODO: type description here.
        timestamp (datetime): TODO: type description here.
        account_id (uuid|string): TODO: type description here.
        tags (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "mtype":'type',
        "payload":'payload',
        "timestamp":'timestamp',
        "account_id":'accountId',
        "tags":'tags'
    }

    def __init__(self,
                 id=None,
                 mtype=None,
                 payload=None,
                 timestamp=None,
                 account_id=None,
                 tags=None,
                 additional_properties = {}):
        """Constructor for the EventDto class"""

        # Initialize members of the class
        self.id = id
        self.mtype = mtype
        self.payload = payload
        self.timestamp = APIHelper.RFC3339DateTime(timestamp) if timestamp else None
        self.account_id = account_id
        self.tags = tags

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        mtype = dictionary.get('type')
        payload = dictionary.get('payload')
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None
        account_id = dictionary.get('accountId')
        tags = dictionary.get('tags')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   mtype,
                   payload,
                   timestamp,
                   account_id,
                   tags,
                   dictionary)


