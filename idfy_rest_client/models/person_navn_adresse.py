# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_navn_adresse

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class PersonNavnAdresse(object):

    """Implementation of the 'Person.NavnAdresse' model.

    TODO: type model description here.

    Attributes:
        status_field (string): TODO: type description here.
        status_dato_field (datetime): TODO: type description here.
        fodselsdato_field (datetime): TODO: type description here.
        navn_field (string): TODO: type description here.
        adresse_field (string): TODO: type description here.
        postnr_field (string): TODO: type description here.
        poststed_field (string): TODO: type description here.
        kommune_field (string): TODO: type description here.
        fylke_field (string): TODO: type description here.
        alder_field (int): TODO: type description here.
        kjonn_field (string): TODO: type description here.
        telefon_field (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status_field":'statusField',
        "status_dato_field":'statusDatoField',
        "fodselsdato_field":'fodselsdatoField',
        "navn_field":'navnField',
        "adresse_field":'adresseField',
        "postnr_field":'postnrField',
        "poststed_field":'poststedField',
        "kommune_field":'kommuneField',
        "fylke_field":'fylkeField',
        "alder_field":'alderField',
        "kjonn_field":'kjonnField',
        "telefon_field":'telefonField'
    }

    def __init__(self,
                 status_field=None,
                 status_dato_field=None,
                 fodselsdato_field=None,
                 navn_field=None,
                 adresse_field=None,
                 postnr_field=None,
                 poststed_field=None,
                 kommune_field=None,
                 fylke_field=None,
                 alder_field=None,
                 kjonn_field=None,
                 telefon_field=None,
                 additional_properties = {}):
        """Constructor for the PersonNavnAdresse class"""

        # Initialize members of the class
        self.status_field = status_field
        self.status_dato_field = APIHelper.RFC3339DateTime(status_dato_field) if status_dato_field else None
        self.fodselsdato_field = APIHelper.RFC3339DateTime(fodselsdato_field) if fodselsdato_field else None
        self.navn_field = navn_field
        self.adresse_field = adresse_field
        self.postnr_field = postnr_field
        self.poststed_field = poststed_field
        self.kommune_field = kommune_field
        self.fylke_field = fylke_field
        self.alder_field = alder_field
        self.kjonn_field = kjonn_field
        self.telefon_field = telefon_field

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
        status_field = dictionary.get('statusField')
        status_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("statusDatoField")).datetime if dictionary.get("statusDatoField") else None
        fodselsdato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("fodselsdatoField")).datetime if dictionary.get("fodselsdatoField") else None
        navn_field = dictionary.get('navnField')
        adresse_field = dictionary.get('adresseField')
        postnr_field = dictionary.get('postnrField')
        poststed_field = dictionary.get('poststedField')
        kommune_field = dictionary.get('kommuneField')
        fylke_field = dictionary.get('fylkeField')
        alder_field = dictionary.get('alderField')
        kjonn_field = dictionary.get('kjonnField')
        telefon_field = dictionary.get('telefonField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(status_field,
                   status_dato_field,
                   fodselsdato_field,
                   navn_field,
                   adresse_field,
                   postnr_field,
                   poststed_field,
                   kommune_field,
                   fylke_field,
                   alder_field,
                   kjonn_field,
                   telefon_field,
                   dictionary)


