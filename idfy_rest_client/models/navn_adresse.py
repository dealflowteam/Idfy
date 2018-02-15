# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.navn_adresse

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class NavnAdresse(object):

    """Implementation of the 'NavnAdresse' model.

    TODO: type model description here.

    Attributes:
        kode_type_field (string): TODO: type description here.
        kode_tekst_field (string): TODO: type description here.
        navn_field (string): TODO: type description here.
        gate_adresse_field (string): TODO: type description here.
        gate_postboks_field (int): TODO: type description here.
        gate_postnr_field (int): TODO: type description here.
        gate_poststed_field (string): TODO: type description here.
        post_adresse_field (string): TODO: type description here.
        post_postboks_field (int): TODO: type description here.
        post_postnr_field (int): TODO: type description here.
        post_poststed_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kode_type_field":'kodeTypeField',
        "kode_tekst_field":'kodeTekstField',
        "navn_field":'navnField',
        "gate_adresse_field":'gateAdresseField',
        "gate_postboks_field":'gatePostboksField',
        "gate_postnr_field":'gatePostnrField',
        "gate_poststed_field":'gatePoststedField',
        "post_adresse_field":'postAdresseField',
        "post_postboks_field":'postPostboksField',
        "post_postnr_field":'postPostnrField',
        "post_poststed_field":'postPoststedField'
    }

    def __init__(self,
                 kode_type_field=None,
                 kode_tekst_field=None,
                 navn_field=None,
                 gate_adresse_field=None,
                 gate_postboks_field=None,
                 gate_postnr_field=None,
                 gate_poststed_field=None,
                 post_adresse_field=None,
                 post_postboks_field=None,
                 post_postnr_field=None,
                 post_poststed_field=None,
                 additional_properties = {}):
        """Constructor for the NavnAdresse class"""

        # Initialize members of the class
        self.kode_type_field = kode_type_field
        self.kode_tekst_field = kode_tekst_field
        self.navn_field = navn_field
        self.gate_adresse_field = gate_adresse_field
        self.gate_postboks_field = gate_postboks_field
        self.gate_postnr_field = gate_postnr_field
        self.gate_poststed_field = gate_poststed_field
        self.post_adresse_field = post_adresse_field
        self.post_postboks_field = post_postboks_field
        self.post_postnr_field = post_postnr_field
        self.post_poststed_field = post_poststed_field

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
        kode_type_field = dictionary.get('kodeTypeField')
        kode_tekst_field = dictionary.get('kodeTekstField')
        navn_field = dictionary.get('navnField')
        gate_adresse_field = dictionary.get('gateAdresseField')
        gate_postboks_field = dictionary.get('gatePostboksField')
        gate_postnr_field = dictionary.get('gatePostnrField')
        gate_poststed_field = dictionary.get('gatePoststedField')
        post_adresse_field = dictionary.get('postAdresseField')
        post_postboks_field = dictionary.get('postPostboksField')
        post_postnr_field = dictionary.get('postPostnrField')
        post_poststed_field = dictionary.get('postPoststedField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(kode_type_field,
                   kode_tekst_field,
                   navn_field,
                   gate_adresse_field,
                   gate_postboks_field,
                   gate_postnr_field,
                   gate_poststed_field,
                   post_adresse_field,
                   post_postboks_field,
                   post_postnr_field,
                   post_poststed_field,
                   dictionary)


