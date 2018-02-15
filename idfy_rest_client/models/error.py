# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.error

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Error(object):

    """Implementation of the 'Error' model.

    Error details information

    Attributes:
        native_error_code (string): The error code from the Identity provider
        error_code (string): The error code for the error
        error_message (string): Error message

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "native_error_code":'NativeErrorCode',
        "error_code":'ErrorCode',
        "error_message":'ErrorMessage'
    }

    def __init__(self,
                 native_error_code=None,
                 error_code=None,
                 error_message=None,
                 additional_properties = {}):
        """Constructor for the Error class"""

        # Initialize members of the class
        self.native_error_code = native_error_code
        self.error_code = error_code
        self.error_message = error_message

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
        native_error_code = dictionary.get('NativeErrorCode')
        error_code = dictionary.get('ErrorCode')
        error_message = dictionary.get('ErrorMessage')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(native_error_code,
                   error_code,
                   error_message,
                   dictionary)


