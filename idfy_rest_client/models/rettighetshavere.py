# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.rettighetshavere

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class Rettighetshavere(object):

    """Implementation of the 'Rettighetshavere' model.

    TODO: type model description here.

    Attributes:
        internreferanse_field (long|int): TODO: type description here.
        fodt_dato_field (datetime): TODO: type description here.
        fodt_dato_field_specified (bool): TODO: type description here.
        navn_field (string): TODO: type description here.
        adresse_field (string): TODO: type description here.
        postnr_field (int): TODO: type description here.
        poststed_field (string): TODO: type description here.
        andel_field (float): TODO: type description here.
        indirekte_eier_field (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "internreferanse_field":'internreferanseField',
        "fodt_dato_field":'fodtDatoField',
        "fodt_dato_field_specified":'fodtDatoFieldSpecified',
        "navn_field":'navnField',
        "adresse_field":'adresseField',
        "postnr_field":'postnrField',
        "poststed_field":'poststedField',
        "andel_field":'andelField',
        "indirekte_eier_field":'indirekteEierField'
    }

    def __init__(self,
                 internreferanse_field=None,
                 fodt_dato_field=None,
                 fodt_dato_field_specified=None,
                 navn_field=None,
                 adresse_field=None,
                 postnr_field=None,
                 poststed_field=None,
                 andel_field=None,
                 indirekte_eier_field=None,
                 additional_properties = {}):
        """Constructor for the Rettighetshavere class"""

        # Initialize members of the class
        self.internreferanse_field = internreferanse_field
        self.fodt_dato_field = APIHelper.RFC3339DateTime(fodt_dato_field) if fodt_dato_field else None
        self.fodt_dato_field_specified = fodt_dato_field_specified
        self.navn_field = navn_field
        self.adresse_field = adresse_field
        self.postnr_field = postnr_field
        self.poststed_field = poststed_field
        self.andel_field = andel_field
        self.indirekte_eier_field = indirekte_eier_field

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
        internreferanse_field = dictionary.get('internreferanseField')
        fodt_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("fodtDatoField")).datetime if dictionary.get("fodtDatoField") else None
        fodt_dato_field_specified = dictionary.get('fodtDatoFieldSpecified')
        navn_field = dictionary.get('navnField')
        adresse_field = dictionary.get('adresseField')
        postnr_field = dictionary.get('postnrField')
        poststed_field = dictionary.get('poststedField')
        andel_field = dictionary.get('andelField')
        indirekte_eier_field = dictionary.get('indirekteEierField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(internreferanse_field,
                   fodt_dato_field,
                   fodt_dato_field_specified,
                   navn_field,
                   adresse_field,
                   postnr_field,
                   poststed_field,
                   andel_field,
                   indirekte_eier_field,
                   dictionary)


