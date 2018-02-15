# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.x_509_certificate

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class X509Certificate(object):

    """Implementation of the 'X509Certificate' model.

    TODO: type model description here.

    Attributes:
        raw_data (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "raw_data":'rawData'
    }

    def __init__(self,
                 raw_data=None,
                 additional_properties = {}):
        """Constructor for the X509Certificate class"""

        # Initialize members of the class
        self.raw_data = raw_data

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
        raw_data = dictionary.get('rawData')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(raw_data,
                   dictionary)


