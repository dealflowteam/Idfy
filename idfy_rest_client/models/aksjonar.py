# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.aksjonar

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class Aksjonar(object):

    """Implementation of the 'Aksjonar' model.

    TODO: type model description here.

    Attributes:
        orgnr_field (int): TODO: type description here.
        intern_ref_field (long|int): TODO: type description here.
        fodt_dato_field (datetime): TODO: type description here.
        navn_field (string): TODO: type description here.
        postnr_field (int): TODO: type description here.
        poststed_field (string): TODO: type description here.
        eierandel_field (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "orgnr_field":'orgnrField',
        "intern_ref_field":'internRefField',
        "fodt_dato_field":'fodtDatoField',
        "navn_field":'navnField',
        "postnr_field":'postnrField',
        "poststed_field":'poststedField',
        "eierandel_field":'eierandelField'
    }

    def __init__(self,
                 orgnr_field=None,
                 intern_ref_field=None,
                 fodt_dato_field=None,
                 navn_field=None,
                 postnr_field=None,
                 poststed_field=None,
                 eierandel_field=None,
                 additional_properties = {}):
        """Constructor for the Aksjonar class"""

        # Initialize members of the class
        self.orgnr_field = orgnr_field
        self.intern_ref_field = intern_ref_field
        self.fodt_dato_field = APIHelper.RFC3339DateTime(fodt_dato_field) if fodt_dato_field else None
        self.navn_field = navn_field
        self.postnr_field = postnr_field
        self.poststed_field = poststed_field
        self.eierandel_field = eierandel_field

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
        intern_ref_field = dictionary.get('internRefField')
        fodt_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("fodtDatoField")).datetime if dictionary.get("fodtDatoField") else None
        navn_field = dictionary.get('navnField')
        postnr_field = dictionary.get('postnrField')
        poststed_field = dictionary.get('poststedField')
        eierandel_field = dictionary.get('eierandelField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(orgnr_field,
                   intern_ref_field,
                   fodt_dato_field,
                   navn_field,
                   postnr_field,
                   poststed_field,
                   eierandel_field,
                   dictionary)


