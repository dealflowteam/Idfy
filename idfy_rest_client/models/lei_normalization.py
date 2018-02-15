# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_normalization

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class LeiNormalization(object):

    """Implementation of the 'LeiNormalization' model.

    TODO: type model description here.

    Attributes:
        cleaned (string): TODO: type description here.
        normalized (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cleaned":'Cleaned',
        "normalized":'Normalized'
    }

    def __init__(self,
                 cleaned=None,
                 normalized=None,
                 additional_properties = {}):
        """Constructor for the LeiNormalization class"""

        # Initialize members of the class
        self.cleaned = cleaned
        self.normalized = normalized

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
        cleaned = dictionary.get('Cleaned')
        normalized = dictionary.get('Normalized')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(cleaned,
                   normalized,
                   dictionary)


