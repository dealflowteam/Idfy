# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.time_to_live

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class TimeToLive(object):

    """Implementation of the 'TimeToLive' model.

    TODO: type model description here.

    Attributes:
        deadline (datetime): Define when the document should expire (ISO
            8601), document is not signable after this (Default/maximum 45
            days)
        delete_after_hours (int): How many hours should we keep the document
            after it is signed? Default/ maximum  7 days (168 hours)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deadline":'deadline',
        "delete_after_hours":'deleteAfterHours'
    }

    def __init__(self,
                 deadline=None,
                 delete_after_hours=None,
                 additional_properties = {}):
        """Constructor for the TimeToLive class"""

        # Initialize members of the class
        self.deadline = APIHelper.RFC3339DateTime(deadline) if deadline else None
        self.delete_after_hours = delete_after_hours

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
        deadline = APIHelper.RFC3339DateTime.from_value(dictionary.get("deadline")).datetime if dictionary.get("deadline") else None
        delete_after_hours = dictionary.get('deleteAfterHours')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(deadline,
                   delete_after_hours,
                   dictionary)


