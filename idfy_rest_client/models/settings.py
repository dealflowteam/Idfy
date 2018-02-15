# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.settings

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Settings(object):

    """Implementation of the 'Settings' model.

    Other account settings

    Attributes:
        sms_sender (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sms_sender":'SMSSender'
    }

    def __init__(self,
                 sms_sender=None,
                 additional_properties = {}):
        """Constructor for the Settings class"""

        # Initialize members of the class
        self.sms_sender = sms_sender

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
        sms_sender = dictionary.get('SMSSender')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(sms_sender,
                   dictionary)


