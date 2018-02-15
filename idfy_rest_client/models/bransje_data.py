# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.bransje_data

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class BransjeData(object):

    """Implementation of the 'BransjeData' model.

    TODO: type model description here.

    Attributes:
        bransje_kode_field (int): TODO: type description here.
        bransje_tekst_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bransje_kode_field":'bransjeKodeField',
        "bransje_tekst_field":'bransjeTekstField'
    }

    def __init__(self,
                 bransje_kode_field=None,
                 bransje_tekst_field=None,
                 additional_properties = {}):
        """Constructor for the BransjeData class"""

        # Initialize members of the class
        self.bransje_kode_field = bransje_kode_field
        self.bransje_tekst_field = bransje_tekst_field

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
        bransje_kode_field = dictionary.get('bransjeKodeField')
        bransje_tekst_field = dictionary.get('bransjeTekstField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(bransje_kode_field,
                   bransje_tekst_field,
                   dictionary)


