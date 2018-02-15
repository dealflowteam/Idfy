# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_error

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class SignatureError(object):

    """Implementation of the 'signatureError' model.

    TODO: type model description here.

    Attributes:
        error_message (string): TODO: type description here.
        error_code (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_message":'errorMessage',
        "error_code":'errorCode'
    }

    def __init__(self,
                 error_message=None,
                 error_code=None,
                 additional_properties = {}):
        """Constructor for the SignatureError class"""

        # Initialize members of the class
        self.error_message = error_message
        self.error_code = error_code

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
        error_message = dictionary.get('errorMessage')
        error_code = dictionary.get('errorCode')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(error_message,
                   error_code,
                   dictionary)


