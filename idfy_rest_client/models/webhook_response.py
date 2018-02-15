# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.webhook_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class WebhookResponse(object):

    """Implementation of the 'WebhookResponse' model.

    TODO: type model description here.

    Attributes:
        code (int): The status code returned by the webhook endpoint on last
            delivery attempt.
        message (string): The message returned by the webhook endpoint on last
            delivery attempt.
        timestamp (datetime): Time at which the last delivery attempt was
            made.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "message":'message',
        "timestamp":'timestamp'
    }

    def __init__(self,
                 code=None,
                 message=None,
                 timestamp=None,
                 additional_properties = {}):
        """Constructor for the WebhookResponse class"""

        # Initialize members of the class
        self.code = code
        self.message = message
        self.timestamp = APIHelper.RFC3339DateTime(timestamp) if timestamp else None

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
        code = dictionary.get('code')
        message = dictionary.get('message')
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(code,
                   message,
                   timestamp,
                   dictionary)


