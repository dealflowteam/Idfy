# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.verv

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class Verv(object):

    """Implementation of the 'Verv' model.

    TODO: type model description here.

    Attributes:
        intern_ref_field (long|int): TODO: type description here.
        fodt_dato_field (datetime): TODO: type description here.
        fodt_dato_field_specified (bool): TODO: type description here.
        navn_field (string): TODO: type description here.
        telefon_field (list of string): TODO: type description here.
        postnr_field (int): TODO: type description here.
        poststed_field (string): TODO: type description here.
        verv_kode_field (string): TODO: type description here.
        verv_tekst_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "intern_ref_field":'internRefField',
        "fodt_dato_field":'fodtDatoField',
        "fodt_dato_field_specified":'fodtDatoFieldSpecified',
        "navn_field":'navnField',
        "telefon_field":'telefonField',
        "postnr_field":'postnrField',
        "poststed_field":'poststedField',
        "verv_kode_field":'vervKodeField',
        "verv_tekst_field":'vervTekstField'
    }

    def __init__(self,
                 intern_ref_field=None,
                 fodt_dato_field=None,
                 fodt_dato_field_specified=None,
                 navn_field=None,
                 telefon_field=None,
                 postnr_field=None,
                 poststed_field=None,
                 verv_kode_field=None,
                 verv_tekst_field=None,
                 additional_properties = {}):
        """Constructor for the Verv class"""

        # Initialize members of the class
        self.intern_ref_field = intern_ref_field
        self.fodt_dato_field = APIHelper.RFC3339DateTime(fodt_dato_field) if fodt_dato_field else None
        self.fodt_dato_field_specified = fodt_dato_field_specified
        self.navn_field = navn_field
        self.telefon_field = telefon_field
        self.postnr_field = postnr_field
        self.poststed_field = poststed_field
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
        intern_ref_field = dictionary.get('internRefField')
        fodt_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("fodtDatoField")).datetime if dictionary.get("fodtDatoField") else None
        fodt_dato_field_specified = dictionary.get('fodtDatoFieldSpecified')
        navn_field = dictionary.get('navnField')
        telefon_field = dictionary.get('telefonField')
        postnr_field = dictionary.get('postnrField')
        poststed_field = dictionary.get('poststedField')
        verv_kode_field = dictionary.get('vervKodeField')
        verv_tekst_field = dictionary.get('vervTekstField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(intern_ref_field,
                   fodt_dato_field,
                   fodt_dato_field_specified,
                   navn_field,
                   telefon_field,
                   postnr_field,
                   poststed_field,
                   verv_kode_field,
                   verv_tekst_field,
                   dictionary)


