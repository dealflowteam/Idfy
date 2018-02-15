# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_losore

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class PersonLosore(object):

    """Implementation of the 'Person.Losore' model.

    TODO: type model description here.

    Attributes:
        ajour_dato_field (datetime): TODO: type description here.
        spes_tekst_1_field (string): TODO: type description here.
        spes_tekst_2_field (string): TODO: type description here.
        spes_tekst_3_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ajour_dato_field":'ajourDatoField',
        "spes_tekst_1_field":'spesTekst1Field',
        "spes_tekst_2_field":'spesTekst2Field',
        "spes_tekst_3_field":'spesTekst3Field'
    }

    def __init__(self,
                 ajour_dato_field=None,
                 spes_tekst_1_field=None,
                 spes_tekst_2_field=None,
                 spes_tekst_3_field=None,
                 additional_properties = {}):
        """Constructor for the PersonLosore class"""

        # Initialize members of the class
        self.ajour_dato_field = APIHelper.RFC3339DateTime(ajour_dato_field) if ajour_dato_field else None
        self.spes_tekst_1_field = spes_tekst_1_field
        self.spes_tekst_2_field = spes_tekst_2_field
        self.spes_tekst_3_field = spes_tekst_3_field

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
        ajour_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("ajourDatoField")).datetime if dictionary.get("ajourDatoField") else None
        spes_tekst_1_field = dictionary.get('spesTekst1Field')
        spes_tekst_2_field = dictionary.get('spesTekst2Field')
        spes_tekst_3_field = dictionary.get('spesTekst3Field')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(ajour_dato_field,
                   spes_tekst_1_field,
                   spes_tekst_2_field,
                   spes_tekst_3_field,
                   dictionary)


