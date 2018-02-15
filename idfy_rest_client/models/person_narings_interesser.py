# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_narings_interesser

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class PersonNaringsInteresser(object):

    """Implementation of the 'Person.NaringsInteresser' model.

    TODO: type model description here.

    Attributes:
        orgnr_field (int): TODO: type description here.
        status_kode_field (string): TODO: type description here.
        status_tekst_field (string): TODO: type description here.
        status_dato_field (datetime): TODO: type description here.
        navn_field (string): TODO: type description here.
        selsk_form_field (string): TODO: type description here.
        rolle_field (string): TODO: type description here.
        eierandel_field (float): TODO: type description here.
        verv_kode_field (string): TODO: type description here.
        verv_tekst_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "orgnr_field":'orgnrField',
        "status_kode_field":'statusKodeField',
        "status_tekst_field":'statusTekstField',
        "status_dato_field":'statusDatoField',
        "navn_field":'navnField',
        "selsk_form_field":'selskFormField',
        "rolle_field":'rolleField',
        "eierandel_field":'eierandelField',
        "verv_kode_field":'vervKodeField',
        "verv_tekst_field":'vervTekstField'
    }

    def __init__(self,
                 orgnr_field=None,
                 status_kode_field=None,
                 status_tekst_field=None,
                 status_dato_field=None,
                 navn_field=None,
                 selsk_form_field=None,
                 rolle_field=None,
                 eierandel_field=None,
                 verv_kode_field=None,
                 verv_tekst_field=None,
                 additional_properties = {}):
        """Constructor for the PersonNaringsInteresser class"""

        # Initialize members of the class
        self.orgnr_field = orgnr_field
        self.status_kode_field = status_kode_field
        self.status_tekst_field = status_tekst_field
        self.status_dato_field = APIHelper.RFC3339DateTime(status_dato_field) if status_dato_field else None
        self.navn_field = navn_field
        self.selsk_form_field = selsk_form_field
        self.rolle_field = rolle_field
        self.eierandel_field = eierandel_field
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
        orgnr_field = dictionary.get('orgnrField')
        status_kode_field = dictionary.get('statusKodeField')
        status_tekst_field = dictionary.get('statusTekstField')
        status_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("statusDatoField")).datetime if dictionary.get("statusDatoField") else None
        navn_field = dictionary.get('navnField')
        selsk_form_field = dictionary.get('selskFormField')
        rolle_field = dictionary.get('rolleField')
        eierandel_field = dictionary.get('eierandelField')
        verv_kode_field = dictionary.get('vervKodeField')
        verv_tekst_field = dictionary.get('vervTekstField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(orgnr_field,
                   status_kode_field,
                   status_tekst_field,
                   status_dato_field,
                   navn_field,
                   selsk_form_field,
                   rolle_field,
                   eierandel_field,
                   verv_kode_field,
                   verv_tekst_field,
                   dictionary)


