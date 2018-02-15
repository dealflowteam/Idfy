# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_verv_data

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonVervData(object):

    """Implementation of the 'Person.VervData' model.

    TODO: type model description here.

    Attributes:
        verv_kode_field (string): TODO: type description here.
        verv_tekst_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "verv_kode_field":'vervKodeField',
        "verv_tekst_field":'vervTekstField'
    }

    def __init__(self,
                 verv_kode_field=None,
                 verv_tekst_field=None,
                 additional_properties = {}):
        """Constructor for the PersonVervData class"""

        # Initialize members of the class
        self.verv_kode_field = verv_kode_field
        self.verv_tekst_field = verv_tekst_field

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
        verv_kode_field = dictionary.get('vervKodeField')
        verv_tekst_field = dictionary.get('vervTekstField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(verv_kode_field,
                   verv_tekst_field,
                   dictionary)


