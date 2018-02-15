# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.email

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Email(object):

    """Implementation of the 'Email' model.

    TODO: type model description here.

    Attributes:
        language (Language185): Email language
        subject (string): Email subject
        text (string): Insert your email text, we support plain text and
            markdown
        sender_name (string): Name of sender

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language":'language',
        "subject":'subject',
        "text":'text',
        "sender_name":'senderName'
    }

    def __init__(self,
                 language=None,
                 subject=None,
                 text=None,
                 sender_name=None,
                 additional_properties = {}):
        """Constructor for the Email class"""

        # Initialize members of the class
        self.language = language
        self.subject = subject
        self.text = text
        self.sender_name = sender_name

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
        subject = dictionary.get('subject')
        text = dictionary.get('text')
        sender_name = dictionary.get('senderName')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(language,
                   subject,
                   text,
                   sender_name,
                   dictionary)


