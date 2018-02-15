# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_delomrader

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonDelomrader(object):

    """Implementation of the 'Person.Delomrader' model.

    TODO: type model description here.

    Attributes:
        delomrade_kode_field (string): TODO: type description here.
        delomrade_tekst_field (string): TODO: type description here.
        bedommelse_kode_field (string): TODO: type description here.
        bedommelse_tekst_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delomrade_kode_field":'delomradeKodeField',
        "delomrade_tekst_field":'delomradeTekstField',
        "bedommelse_kode_field":'bedommelseKodeField',
        "bedommelse_tekst_field":'bedommelseTekstField'
    }

    def __init__(self,
                 delomrade_kode_field=None,
                 delomrade_tekst_field=None,
                 bedommelse_kode_field=None,
                 bedommelse_tekst_field=None,
                 additional_properties = {}):
        """Constructor for the PersonDelomrader class"""

        # Initialize members of the class
        self.delomrade_kode_field = delomrade_kode_field
        self.delomrade_tekst_field = delomrade_tekst_field
        self.bedommelse_kode_field = bedommelse_kode_field
        self.bedommelse_tekst_field = bedommelse_tekst_field

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
        delomrade_kode_field = dictionary.get('delomradeKodeField')
        delomrade_tekst_field = dictionary.get('delomradeTekstField')
        bedommelse_kode_field = dictionary.get('bedommelseKodeField')
        bedommelse_tekst_field = dictionary.get('bedommelseTekstField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(delomrade_kode_field,
                   delomrade_tekst_field,
                   bedommelse_kode_field,
                   bedommelse_tekst_field,
                   dictionary)


