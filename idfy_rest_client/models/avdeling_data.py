# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.avdeling_data

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class AvdelingData(object):

    """Implementation of the 'AvdelingData' model.

    TODO: type model description here.

    Attributes:
        antall_ansatte_field (int): TODO: type description here.
        antall_ansatte_field_specified (bool): TODO: type description here.
        telefon_field (int): TODO: type description here.
        telefon_field_specified (bool): TODO: type description here.
        telefax_field (int): TODO: type description here.
        telefax_field_specified (bool): TODO: type description here.
        stiftet_dato_field (datetime): TODO: type description here.
        bransje_kode_field (string): TODO: type description here.
        bransje_tekst_field (string): TODO: type description here.
        daglig_leder_field (string): TODO: type description here.
        hovedforetak_orgnr_field (int): TODO: type description here.
        hovedforetak_orgnr_field_specified (bool): TODO: type description
            here.
        hovedforetak_dunsnr_field (int): TODO: type description here.
        hovedforetak_dunsnr_field_specified (bool): TODO: type description
            here.
        hovedforetak_navn_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "antall_ansatte_field":'antallAnsatteField',
        "antall_ansatte_field_specified":'antallAnsatteFieldSpecified',
        "telefon_field":'telefonField',
        "telefon_field_specified":'telefonFieldSpecified',
        "telefax_field":'telefaxField',
        "telefax_field_specified":'telefaxFieldSpecified',
        "stiftet_dato_field":'stiftetDatoField',
        "bransje_kode_field":'bransjeKodeField',
        "bransje_tekst_field":'bransjeTekstField',
        "daglig_leder_field":'dagligLederField',
        "hovedforetak_orgnr_field":'hovedforetakOrgnrField',
        "hovedforetak_orgnr_field_specified":'hovedforetakOrgnrFieldSpecified',
        "hovedforetak_dunsnr_field":'hovedforetakDunsnrField',
        "hovedforetak_dunsnr_field_specified":'hovedforetakDunsnrFieldSpecified',
        "hovedforetak_navn_field":'hovedforetakNavnField'
    }

    def __init__(self,
                 antall_ansatte_field=None,
                 antall_ansatte_field_specified=None,
                 telefon_field=None,
                 telefon_field_specified=None,
                 telefax_field=None,
                 telefax_field_specified=None,
                 stiftet_dato_field=None,
                 bransje_kode_field=None,
                 bransje_tekst_field=None,
                 daglig_leder_field=None,
                 hovedforetak_orgnr_field=None,
                 hovedforetak_orgnr_field_specified=None,
                 hovedforetak_dunsnr_field=None,
                 hovedforetak_dunsnr_field_specified=None,
                 hovedforetak_navn_field=None,
                 additional_properties = {}):
        """Constructor for the AvdelingData class"""

        # Initialize members of the class
        self.antall_ansatte_field = antall_ansatte_field
        self.antall_ansatte_field_specified = antall_ansatte_field_specified
        self.telefon_field = telefon_field
        self.telefon_field_specified = telefon_field_specified
        self.telefax_field = telefax_field
        self.telefax_field_specified = telefax_field_specified
        self.stiftet_dato_field = APIHelper.RFC3339DateTime(stiftet_dato_field) if stiftet_dato_field else None
        self.bransje_kode_field = bransje_kode_field
        self.bransje_tekst_field = bransje_tekst_field
        self.daglig_leder_field = daglig_leder_field
        self.hovedforetak_orgnr_field = hovedforetak_orgnr_field
        self.hovedforetak_orgnr_field_specified = hovedforetak_orgnr_field_specified
        self.hovedforetak_dunsnr_field = hovedforetak_dunsnr_field
        self.hovedforetak_dunsnr_field_specified = hovedforetak_dunsnr_field_specified
        self.hovedforetak_navn_field = hovedforetak_navn_field

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
        antall_ansatte_field = dictionary.get('antallAnsatteField')
        antall_ansatte_field_specified = dictionary.get('antallAnsatteFieldSpecified')
        telefon_field = dictionary.get('telefonField')
        telefon_field_specified = dictionary.get('telefonFieldSpecified')
        telefax_field = dictionary.get('telefaxField')
        telefax_field_specified = dictionary.get('telefaxFieldSpecified')
        stiftet_dato_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("stiftetDatoField")).datetime if dictionary.get("stiftetDatoField") else None
        bransje_kode_field = dictionary.get('bransjeKodeField')
        bransje_tekst_field = dictionary.get('bransjeTekstField')
        daglig_leder_field = dictionary.get('dagligLederField')
        hovedforetak_orgnr_field = dictionary.get('hovedforetakOrgnrField')
        hovedforetak_orgnr_field_specified = dictionary.get('hovedforetakOrgnrFieldSpecified')
        hovedforetak_dunsnr_field = dictionary.get('hovedforetakDunsnrField')
        hovedforetak_dunsnr_field_specified = dictionary.get('hovedforetakDunsnrFieldSpecified')
        hovedforetak_navn_field = dictionary.get('hovedforetakNavnField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(antall_ansatte_field,
                   antall_ansatte_field_specified,
                   telefon_field,
                   telefon_field_specified,
                   telefax_field,
                   telefax_field_specified,
                   stiftet_dato_field,
                   bransje_kode_field,
                   bransje_tekst_field,
                   daglig_leder_field,
                   hovedforetak_orgnr_field,
                   hovedforetak_orgnr_field_specified,
                   hovedforetak_dunsnr_field,
                   hovedforetak_dunsnr_field_specified,
                   hovedforetak_navn_field,
                   dictionary)


