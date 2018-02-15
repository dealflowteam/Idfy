# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.invalidate_identification_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class InvalidateIdentificationRequest(object):

    """Implementation of the 'InvalidateIdentificationRequest' model.

    Invalidates a identifyrequest so that it cannot be used twice.

    Attributes:
        request_id (string): The requestid of the identification process

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id":'RequestId'
    }

    def __init__(self,
                 request_id=None,
                 additional_properties = {}):
        """Constructor for the InvalidateIdentificationRequest class"""

        # Initialize members of the class
        self.request_id = request_id

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
        request_id = dictionary.get('RequestId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(request_id,
                   dictionary)


