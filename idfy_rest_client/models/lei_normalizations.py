# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_normalizations

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.lei_normalization

class LeiNormalizations(object):

    """Implementation of the 'LeiNormalizations' model.

    TODO: type model description here.

    Attributes:
        legal_name (LeiNormalization): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "legal_name":'LegalName'
    }

    def __init__(self,
                 legal_name=None,
                 additional_properties = {}):
        """Constructor for the LeiNormalizations class"""

        # Initialize members of the class
        self.legal_name = legal_name

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
        legal_name = idfy_rest_client.models.lei_normalization.LeiNormalization.from_dictionary(dictionary.get('LegalName')) if dictionary.get('LegalName') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(legal_name,
                   dictionary)


