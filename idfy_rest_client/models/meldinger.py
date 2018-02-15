# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.meldinger

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Meldinger(object):

    """Implementation of the 'Meldinger' model.

    TODO: type model description here.

    Attributes:
        meldings_kode_field (int): TODO: type description here.
        meldings_tekst_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "meldings_kode_field":'meldingsKodeField',
        "meldings_tekst_field":'meldingsTekstField'
    }

    def __init__(self,
                 meldings_kode_field=None,
                 meldings_tekst_field=None,
                 additional_properties = {}):
        """Constructor for the Meldinger class"""

        # Initialize members of the class
        self.meldings_kode_field = meldings_kode_field
        self.meldings_tekst_field = meldings_tekst_field

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
        meldings_kode_field = dictionary.get('meldingsKodeField')
        meldings_tekst_field = dictionary.get('meldingsTekstField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(meldings_kode_field,
                   meldings_tekst_field,
                   dictionary)


