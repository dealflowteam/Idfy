# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_tidligere_navn_adresse

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class PersonTidligereNavnAdresse(object):

    """Implementation of the 'Person.TidligereNavnAdresse' model.

    TODO: type model description here.

    Attributes:
        tidligere_navn_adresse_1_field (string): TODO: type description here.
        endrings_dato_field (datetime): TODO: type description here.
        endrings_type_field (string): TODO: type description here.
        tidligere_post_adresse_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tidligere_navn_adresse_1_field":'tidligereNavnAdresse1Field',
        "endrings_dato_field":'endringsDatoField',
        "endrings_type_field":'endringsTypeField',
        "tidligere_post_adresse_field":'tidligerePostAdresseField'
    }

    def __init__(self,
                 tidligere_navn_adresse_1_field=None,
                 endrings_dato_field=None,
                 endrings_type_field=None,
                 tidligere_post_adresse_field=None,
                 additional_properties = {}):
        """Constructor for the PersonTidligereNavnAdresse class"""

        # Initialize members of the class
        self.tidligere_navn_adresse_1_field = tidligere_navn_adresse_1_field
        self.endrings_dato_field = APIHelper.RFC3339DateTime(endrings_dato_field) if endrings_dato_field else None
        self.endrings_type_field = endrings_type_field
        self.tidligere_post_adresse_field = tidligere_post_adresse_field

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
        tidligere_navn_adresse_1_field = dictionary.get('tidligereNavnAdresse1Field')
        endrings_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("endringsDatoField")).datetime if dictionary.get("endringsDatoField") else None
        endrings_type_field = dictionary.get('endringsTypeField')
        tidligere_post_adresse_field = dictionary.get('tidligerePostAdresseField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(tidligere_navn_adresse_1_field,
                   endrings_dato_field,
                   endrings_type_field,
                   tidligere_post_adresse_field,
                   dictionary)


