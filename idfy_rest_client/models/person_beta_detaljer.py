# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_beta_detaljer

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class PersonBetaDetaljer(object):

    """Implementation of the 'Person.BetaDetaljer' model.

    TODO: type model description here.

    Attributes:
        registrert_dato_field (datetime): TODO: type description here.
        beta_gruppe_kode_field (string): TODO: type description here.
        beta_gruppe_tekst_field (string): TODO: type description here.
        beta_type_field (string): TODO: type description here.
        beta_tekst_field (string): TODO: type description here.
        beta_belop_field (long|int): TODO: type description here.
        kilde_kode_field (string): TODO: type description here.
        kilde_tekst_field (string): TODO: type description here.
        kilde_referansenr_field (long|int): TODO: type description here.
        status_anmerkning_field (string): TODO: type description here.
        status_dato_field (datetime): TODO: type description here.
        kreditor_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "registrert_dato_field":'registrertDatoField',
        "beta_gruppe_kode_field":'betaGruppeKodeField',
        "beta_gruppe_tekst_field":'betaGruppeTekstField',
        "beta_type_field":'betaTypeField',
        "beta_tekst_field":'betaTekstField',
        "beta_belop_field":'betaBelopField',
        "kilde_kode_field":'kildeKodeField',
        "kilde_tekst_field":'kildeTekstField',
        "kilde_referansenr_field":'kildeReferansenrField',
        "status_anmerkning_field":'statusAnmerkningField',
        "status_dato_field":'statusDatoField',
        "kreditor_field":'kreditorField'
    }

    def __init__(self,
                 registrert_dato_field=None,
                 beta_gruppe_kode_field=None,
                 beta_gruppe_tekst_field=None,
                 beta_type_field=None,
                 beta_tekst_field=None,
                 beta_belop_field=None,
                 kilde_kode_field=None,
                 kilde_tekst_field=None,
                 kilde_referansenr_field=None,
                 status_anmerkning_field=None,
                 status_dato_field=None,
                 kreditor_field=None,
                 additional_properties = {}):
        """Constructor for the PersonBetaDetaljer class"""

        # Initialize members of the class
        self.registrert_dato_field = APIHelper.RFC3339DateTime(registrert_dato_field) if registrert_dato_field else None
        self.beta_gruppe_kode_field = beta_gruppe_kode_field
        self.beta_gruppe_tekst_field = beta_gruppe_tekst_field
        self.beta_type_field = beta_type_field
        self.beta_tekst_field = beta_tekst_field
        self.beta_belop_field = beta_belop_field
        self.kilde_kode_field = kilde_kode_field
        self.kilde_tekst_field = kilde_tekst_field
        self.kilde_referansenr_field = kilde_referansenr_field
        self.status_anmerkning_field = status_anmerkning_field
        self.status_dato_field = APIHelper.RFC3339DateTime(status_dato_field) if status_dato_field else None
        self.kreditor_field = kreditor_field

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
        registrert_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("registrertDatoField")).datetime if dictionary.get("registrertDatoField") else None
        beta_gruppe_kode_field = dictionary.get('betaGruppeKodeField')
        beta_gruppe_tekst_field = dictionary.get('betaGruppeTekstField')
        beta_type_field = dictionary.get('betaTypeField')
        beta_tekst_field = dictionary.get('betaTekstField')
        beta_belop_field = dictionary.get('betaBelopField')
        kilde_kode_field = dictionary.get('kildeKodeField')
        kilde_tekst_field = dictionary.get('kildeTekstField')
        kilde_referansenr_field = dictionary.get('kildeReferansenrField')
        status_anmerkning_field = dictionary.get('statusAnmerkningField')
        status_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("statusDatoField")).datetime if dictionary.get("statusDatoField") else None
        kreditor_field = dictionary.get('kreditorField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(registrert_dato_field,
                   beta_gruppe_kode_field,
                   beta_gruppe_tekst_field,
                   beta_type_field,
                   beta_tekst_field,
                   beta_belop_field,
                   kilde_kode_field,
                   kilde_tekst_field,
                   kilde_referansenr_field,
                   status_anmerkning_field,
                   status_dato_field,
                   kreditor_field,
                   dictionary)


