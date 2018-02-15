# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.identifikasjon

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Identifikasjon(object):

    """Implementation of the 'Identifikasjon' model.

    TODO: type model description here.

    Attributes:
        orgnr_field (int): TODO: type description here.
        dunsnr_field (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "orgnr_field":'orgnrField',
        "dunsnr_field":'dunsnrField'
    }

    def __init__(self,
                 orgnr_field=None,
                 dunsnr_field=None,
                 additional_properties = {}):
        """Constructor for the Identifikasjon class"""

        # Initialize members of the class
        self.orgnr_field = orgnr_field
        self.dunsnr_field = dunsnr_field

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
        orgnr_field = dictionary.get('orgnrField')
        dunsnr_field = dictionary.get('dunsnrField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(orgnr_field,
                   dunsnr_field,
                   dictionary)


