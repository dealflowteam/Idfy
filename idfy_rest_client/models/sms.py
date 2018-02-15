# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.sms

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class SMS(object):

    """Implementation of the 'SMS' model.

    TODO: type model description here.

    Attributes:
        language (Language185): Sms language
        text (string): Sms text
        sender (string): Sender name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language":'language',
        "text":'text',
        "sender":'sender'
    }

    def __init__(self,
                 language=None,
                 text=None,
                 sender=None,
                 additional_properties = {}):
        """Constructor for the SMS class"""

        # Initialize members of the class
        self.language = language
        self.text = text
        self.sender = sender

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
        language = dictionary.get('language')
        text = dictionary.get('text')
        sender = dictionary.get('sender')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(language,
                   text,
                   sender,
                   dictionary)


