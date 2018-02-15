# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_fullmakt_foretak

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.person_fullmakt_person

class PersonFullmaktForetak(object):

    """Implementation of the 'Person.FullmaktForetak' model.

    TODO: type model description here.

    Attributes:
        dunsnr_field (int): TODO: type description here.
        orgnr_field (int): TODO: type description here.
        navn_field (string): TODO: type description here.
        adresse_field (string): TODO: type description here.
        postnr_field (int): TODO: type description here.
        poststed_field (string): TODO: type description here.
        status_kode_field (string): TODO: type description here.
        status_tekst_field (string): TODO: type description here.
        selskapsform_field (string): TODO: type description here.
        prokura_kode_field (string): TODO: type description here.
        prokura_tekst_field (string): TODO: type description here.
        signatur_kode_field (string): TODO: type description here.
        signatur_tekst_field (string): TODO: type description here.
        fullmakt_person_field (list of PersonFullmaktPerson): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dunsnr_field":'dunsnrField',
        "orgnr_field":'orgnrField',
        "navn_field":'navnField',
        "adresse_field":'adresseField',
        "postnr_field":'postnrField',
        "poststed_field":'poststedField',
        "status_kode_field":'statusKodeField',
        "status_tekst_field":'statusTekstField',
        "selskapsform_field":'selskapsformField',
        "prokura_kode_field":'prokuraKodeField',
        "prokura_tekst_field":'prokuraTekstField',
        "signatur_kode_field":'signaturKodeField',
        "signatur_tekst_field":'signaturTekstField',
        "fullmakt_person_field":'fullmaktPersonField'
    }

    def __init__(self,
                 dunsnr_field=None,
                 orgnr_field=None,
                 navn_field=None,
                 adresse_field=None,
                 postnr_field=None,
                 poststed_field=None,
                 status_kode_field=None,
                 status_tekst_field=None,
                 selskapsform_field=None,
                 prokura_kode_field=None,
                 prokura_tekst_field=None,
                 signatur_kode_field=None,
                 signatur_tekst_field=None,
                 fullmakt_person_field=None,
                 additional_properties = {}):
        """Constructor for the PersonFullmaktForetak class"""

        # Initialize members of the class
        self.dunsnr_field = dunsnr_field
        self.orgnr_field = orgnr_field
        self.navn_field = navn_field
        self.adresse_field = adresse_field
        self.postnr_field = postnr_field
        self.poststed_field = poststed_field
        self.status_kode_field = status_kode_field
        self.status_tekst_field = status_tekst_field
        self.selskapsform_field = selskapsform_field
        self.prokura_kode_field = prokura_kode_field
        self.prokura_tekst_field = prokura_tekst_field
        self.signatur_kode_field = signatur_kode_field
        self.signatur_tekst_field = signatur_tekst_field
        self.fullmakt_person_field = fullmakt_person_field

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
        dunsnr_field = dictionary.get('dunsnrField')
        orgnr_field = dictionary.get('orgnrField')
        navn_field = dictionary.get('navnField')
        adresse_field = dictionary.get('adresseField')
        postnr_field = dictionary.get('postnrField')
        poststed_field = dictionary.get('poststedField')
        status_kode_field = dictionary.get('statusKodeField')
        status_tekst_field = dictionary.get('statusTekstField')
        selskapsform_field = dictionary.get('selskapsformField')
        prokura_kode_field = dictionary.get('prokuraKodeField')
        prokura_tekst_field = dictionary.get('prokuraTekstField')
        signatur_kode_field = dictionary.get('signaturKodeField')
        signatur_tekst_field = dictionary.get('signaturTekstField')
        fullmakt_person_field = None
        if dictionary.get('fullmaktPersonField') != None:
            fullmakt_person_field = list()
            for structure in dictionary.get('fullmaktPersonField'):
                fullmakt_person_field.append(idfy_rest_client.models.person_fullmakt_person.PersonFullmaktPerson.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(dunsnr_field,
                   orgnr_field,
                   navn_field,
                   adresse_field,
                   postnr_field,
                   poststed_field,
                   status_kode_field,
                   status_tekst_field,
                   selskapsform_field,
                   prokura_kode_field,
                   prokura_tekst_field,
                   signatur_kode_field,
                   signatur_tekst_field,
                   fullmakt_person_field,
                   dictionary)


