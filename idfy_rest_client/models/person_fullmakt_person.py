# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_fullmakt_person

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.person_verv_data

class PersonFullmaktPerson(object):

    """Implementation of the 'Person.FullmaktPerson' model.

    TODO: type model description here.

    Attributes:
        internreferanse_field (long|int): TODO: type description here.
        fodt_dato_field (datetime): TODO: type description here.
        fodt_dato_field_specified (bool): TODO: type description here.
        navn_field (string): TODO: type description here.
        adresse_field (string): TODO: type description here.
        postnr_field (int): TODO: type description here.
        poststed_field (string): TODO: type description here.
        fullmakt_type_kode_field (string): TODO: type description here.
        fullmakt_type_tekst_field (string): TODO: type description here.
        fullmakt_kode_field (string): TODO: type description here.
        fullmakt_tekst_field (string): TODO: type description here.
        prioritet_field (int): TODO: type description here.
        prioritet_field_specified (bool): TODO: type description here.
        antall_field (int): TODO: type description here.
        antall_field_specified (bool): TODO: type description here.
        obligatorisk_field (bool): TODO: type description here.
        obligatorisk_field_specified (bool): TODO: type description here.
        verv_field (list of PersonVervData): TODO: type description here.

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
        "fullmakt_type_kode_field":'fullmaktTypeKodeField',
        "fullmakt_type_tekst_field":'fullmaktTypeTekstField',
        "fullmakt_kode_field":'fullmaktKodeField',
        "fullmakt_tekst_field":'fullmaktTekstField',
        "prioritet_field":'prioritetField',
        "prioritet_field_specified":'prioritetFieldSpecified',
        "antall_field":'antallField',
        "antall_field_specified":'antallFieldSpecified',
        "obligatorisk_field":'obligatoriskField',
        "obligatorisk_field_specified":'obligatoriskFieldSpecified',
        "verv_field":'vervField'
    }

    def __init__(self,
                 internreferanse_field=None,
                 fodt_dato_field=None,
                 fodt_dato_field_specified=None,
                 navn_field=None,
                 adresse_field=None,
                 postnr_field=None,
                 poststed_field=None,
                 fullmakt_type_kode_field=None,
                 fullmakt_type_tekst_field=None,
                 fullmakt_kode_field=None,
                 fullmakt_tekst_field=None,
                 prioritet_field=None,
                 prioritet_field_specified=None,
                 antall_field=None,
                 antall_field_specified=None,
                 obligatorisk_field=None,
                 obligatorisk_field_specified=None,
                 verv_field=None,
                 additional_properties = {}):
        """Constructor for the PersonFullmaktPerson class"""

        # Initialize members of the class
        self.internreferanse_field = internreferanse_field
        self.fodt_dato_field = APIHelper.RFC3339DateTime(fodt_dato_field) if fodt_dato_field else None
        self.fodt_dato_field_specified = fodt_dato_field_specified
        self.navn_field = navn_field
        self.adresse_field = adresse_field
        self.postnr_field = postnr_field
        self.poststed_field = poststed_field
        self.fullmakt_type_kode_field = fullmakt_type_kode_field
        self.fullmakt_type_tekst_field = fullmakt_type_tekst_field
        self.fullmakt_kode_field = fullmakt_kode_field
        self.fullmakt_tekst_field = fullmakt_tekst_field
        self.prioritet_field = prioritet_field
        self.prioritet_field_specified = prioritet_field_specified
        self.antall_field = antall_field
        self.antall_field_specified = antall_field_specified
        self.obligatorisk_field = obligatorisk_field
        self.obligatorisk_field_specified = obligatorisk_field_specified
        self.verv_field = verv_field

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
        fullmakt_type_kode_field = dictionary.get('fullmaktTypeKodeField')
        fullmakt_type_tekst_field = dictionary.get('fullmaktTypeTekstField')
        fullmakt_kode_field = dictionary.get('fullmaktKodeField')
        fullmakt_tekst_field = dictionary.get('fullmaktTekstField')
        prioritet_field = dictionary.get('prioritetField')
        prioritet_field_specified = dictionary.get('prioritetFieldSpecified')
        antall_field = dictionary.get('antallField')
        antall_field_specified = dictionary.get('antallFieldSpecified')
        obligatorisk_field = dictionary.get('obligatoriskField')
        obligatorisk_field_specified = dictionary.get('obligatoriskFieldSpecified')
        verv_field = None
        if dictionary.get('vervField') != None:
            verv_field = list()
            for structure in dictionary.get('vervField'):
                verv_field.append(idfy_rest_client.models.person_verv_data.PersonVervData.from_dictionary(structure))

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
                   fullmakt_type_kode_field,
                   fullmakt_type_tekst_field,
                   fullmakt_kode_field,
                   fullmakt_tekst_field,
                   prioritet_field,
                   prioritet_field_specified,
                   antall_field,
                   antall_field_specified,
                   obligatorisk_field,
                   obligatorisk_field_specified,
                   verv_field,
                   dictionary)


