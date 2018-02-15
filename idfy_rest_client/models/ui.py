# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.ui

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.dialogs
import idfy_rest_client.models.signature_styling

class UI(object):

    """Implementation of the 'UI' model.

    TODO: type model description here.

    Attributes:
        dialogs (Dialogs): You can create dialogs that will be showed to the
            signer in the signature process
        language (Language157): The signers preferred language, this setting
            is used when signing the document and in email/sms
            notifications.<span style="color: blue;">If you set it to browser
            language the notifications will be delievered in english unless
            you specify custom notification messages with browser as language
            in your request.</span>
        styling (SignatureStyling): Customize styling to make the the
            signature application look perfect in combination with your
            application

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dialogs":'dialogs',
        "language":'language',
        "styling":'styling'
    }

    def __init__(self,
                 dialogs=None,
                 language=None,
                 styling=None,
                 additional_properties = {}):
        """Constructor for the UI class"""

        # Initialize members of the class
        self.dialogs = dialogs
        self.language = language
        self.styling = styling

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
        dialogs = idfy_rest_client.models.dialogs.Dialogs.from_dictionary(dictionary.get('dialogs')) if dictionary.get('dialogs') else None
        language = dictionary.get('language')
        styling = idfy_rest_client.models.signature_styling.SignatureStyling.from_dictionary(dictionary.get('styling')) if dictionary.get('styling') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(dialogs,
                   language,
                   styling,
                   dictionary)


