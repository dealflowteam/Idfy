# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.dealer_logo

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class DealerLogo(object):

    """Implementation of the 'DealerLogo' model.

    TODO: type model description here.

    Attributes:
        dealer_id (uuid|string): TODO: type description here.
        base_64_encoded_logo (string): TODO: type description here.
        file_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dealer_id":'DealerId',
        "base_64_encoded_logo":'Base64EncodedLogo',
        "file_name":'FileName'
    }

    def __init__(self,
                 dealer_id=None,
                 base_64_encoded_logo=None,
                 file_name=None,
                 additional_properties = {}):
        """Constructor for the DealerLogo class"""

        # Initialize members of the class
        self.dealer_id = dealer_id
        self.base_64_encoded_logo = base_64_encoded_logo
        self.file_name = file_name

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
        dealer_id = dictionary.get('DealerId')
        base_64_encoded_logo = dictionary.get('Base64EncodedLogo')
        file_name = dictionary.get('FileName')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(dealer_id,
                   base_64_encoded_logo,
                   file_name,
                   dictionary)


