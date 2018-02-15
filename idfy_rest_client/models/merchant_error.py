# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.merchant_error

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class MerchantError(object):

    """Implementation of the 'merchantError' model.

    TODO: type model description here.

    Attributes:
        error_code (int): TODO: type description here.
        error_description (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_code":'errorCode',
        "error_description":'errorDescription'
    }

    def __init__(self,
                 error_code=None,
                 error_description=None,
                 additional_properties = {}):
        """Constructor for the MerchantError class"""

        # Initialize members of the class
        self.error_code = error_code
        self.error_description = error_description

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
        error_code = dictionary.get('errorCode')
        error_description = dictionary.get('errorDescription')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(error_code,
                   error_description,
                   dictionary)


