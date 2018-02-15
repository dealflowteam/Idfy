# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_arsaks_data

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonArsaksData(object):

    """Implementation of the 'Person.ArsaksData' model.

    TODO: type model description here.

    Attributes:
        arsaks_kode_field (string): TODO: type description here.
        arsaks_tekst_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "arsaks_kode_field":'arsaksKodeField',
        "arsaks_tekst_field":'arsaksTekstField'
    }

    def __init__(self,
                 arsaks_kode_field=None,
                 arsaks_tekst_field=None,
                 additional_properties = {}):
        """Constructor for the PersonArsaksData class"""

        # Initialize members of the class
        self.arsaks_kode_field = arsaks_kode_field
        self.arsaks_tekst_field = arsaks_tekst_field

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
        arsaks_kode_field = dictionary.get('arsaksKodeField')
        arsaks_tekst_field = dictionary.get('arsaksTekstField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(arsaks_kode_field,
                   arsaks_tekst_field,
                   dictionary)


