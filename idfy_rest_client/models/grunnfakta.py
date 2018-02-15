# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.grunnfakta

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.bransje_data
import idfy_rest_client.models.ansatte_data

class Grunnfakta(object):

    """Implementation of the 'Grunnfakta' model.

    TODO: type model description here.

    Attributes:
        selsk_form_kode_field (string): TODO: type description here.
        selsk_form_tekst_field (string): TODO: type description here.
        etablert_ar_field (int): TODO: type description here.
        etablert_ar_field_specified (bool): TODO: type description here.
        stiftet_dato_field (datetime): TODO: type description here.
        aksjekapital_field (long|int): TODO: type description here.
        aksjekapital_status_field (string): TODO: type description here.
        registrert_sted_field (string): TODO: type description here.
        registrert_dato_field (datetime): TODO: type description here.
        revisor_orgnr_field (int): TODO: type description here.
        revisor_navn_field (string): TODO: type description here.
        bank_regnr_field (int): TODO: type description here.
        bank_navn_field (string): TODO: type description here.
        bransje_data_field (list of BransjeData): TODO: type description
            here.
        ansatte_data_field (list of AnsatteData): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "selsk_form_kode_field":'selskFormKodeField',
        "selsk_form_tekst_field":'selskFormTekstField',
        "etablert_ar_field":'etablertArField',
        "etablert_ar_field_specified":'etablertArFieldSpecified',
        "stiftet_dato_field":'stiftetDatoField',
        "aksjekapital_field":'aksjekapitalField',
        "aksjekapital_status_field":'aksjekapitalStatusField',
        "registrert_sted_field":'registrertStedField',
        "registrert_dato_field":'registrertDatoField',
        "revisor_orgnr_field":'revisorOrgnrField',
        "revisor_navn_field":'revisorNavnField',
        "bank_regnr_field":'bankRegnrField',
        "bank_navn_field":'bankNavnField',
        "bransje_data_field":'bransjeDataField',
        "ansatte_data_field":'ansatteDataField'
    }

    def __init__(self,
                 selsk_form_kode_field=None,
                 selsk_form_tekst_field=None,
                 etablert_ar_field=None,
                 etablert_ar_field_specified=None,
                 stiftet_dato_field=None,
                 aksjekapital_field=None,
                 aksjekapital_status_field=None,
                 registrert_sted_field=None,
                 registrert_dato_field=None,
                 revisor_orgnr_field=None,
                 revisor_navn_field=None,
                 bank_regnr_field=None,
                 bank_navn_field=None,
                 bransje_data_field=None,
                 ansatte_data_field=None,
                 additional_properties = {}):
        """Constructor for the Grunnfakta class"""

        # Initialize members of the class
        self.selsk_form_kode_field = selsk_form_kode_field
        self.selsk_form_tekst_field = selsk_form_tekst_field
        self.etablert_ar_field = etablert_ar_field
        self.etablert_ar_field_specified = etablert_ar_field_specified
        self.stiftet_dato_field = APIHelper.RFC3339DateTime(stiftet_dato_field) if stiftet_dato_field else None
        self.aksjekapital_field = aksjekapital_field
        self.aksjekapital_status_field = aksjekapital_status_field
        self.registrert_sted_field = registrert_sted_field
        self.registrert_dato_field = APIHelper.RFC3339DateTime(registrert_dato_field) if registrert_dato_field else None
        self.revisor_orgnr_field = revisor_orgnr_field
        self.revisor_navn_field = revisor_navn_field
        self.bank_regnr_field = bank_regnr_field
        self.bank_navn_field = bank_navn_field
        self.bransje_data_field = bransje_data_field
        self.ansatte_data_field = ansatte_data_field

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
        selsk_form_kode_field = dictionary.get('selskFormKodeField')
        selsk_form_tekst_field = dictionary.get('selskFormTekstField')
        etablert_ar_field = dictionary.get('etablertArField')
        etablert_ar_field_specified = dictionary.get('etablertArFieldSpecified')
        stiftet_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("stiftetDatoField")).datetime if dictionary.get("stiftetDatoField") else None
        aksjekapital_field = dictionary.get('aksjekapitalField')
        aksjekapital_status_field = dictionary.get('aksjekapitalStatusField')
        registrert_sted_field = dictionary.get('registrertStedField')
        registrert_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("registrertDatoField")).datetime if dictionary.get("registrertDatoField") else None
        revisor_orgnr_field = dictionary.get('revisorOrgnrField')
        revisor_navn_field = dictionary.get('revisorNavnField')
        bank_regnr_field = dictionary.get('bankRegnrField')
        bank_navn_field = dictionary.get('bankNavnField')
        bransje_data_field = None
        if dictionary.get('bransjeDataField') != None:
            bransje_data_field = list()
            for structure in dictionary.get('bransjeDataField'):
                bransje_data_field.append(idfy_rest_client.models.bransje_data.BransjeData.from_dictionary(structure))
        ansatte_data_field = None
        if dictionary.get('ansatteDataField') != None:
            ansatte_data_field = list()
            for structure in dictionary.get('ansatteDataField'):
                ansatte_data_field.append(idfy_rest_client.models.ansatte_data.AnsatteData.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(selsk_form_kode_field,
                   selsk_form_tekst_field,
                   etablert_ar_field,
                   etablert_ar_field_specified,
                   stiftet_dato_field,
                   aksjekapital_field,
                   aksjekapital_status_field,
                   registrert_sted_field,
                   registrert_dato_field,
                   revisor_orgnr_field,
                   revisor_navn_field,
                   bank_regnr_field,
                   bank_navn_field,
                   bransje_data_field,
                   ansatte_data_field,
                   dictionary)


