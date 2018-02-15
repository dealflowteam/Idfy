# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.datterselskap

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Datterselskap(object):

    """Implementation of the 'Datterselskap' model.

    TODO: type model description here.

    Attributes:
        orgnr_field (long|int): TODO: type description here.
        kode_type_field (string): TODO: type description here.
        kode_tekst_field (string): TODO: type description here.
        navn_field (string): TODO: type description here.
        postnr_field (int): TODO: type description here.
        poststed_field (string): TODO: type description here.
        eierandel_field (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "orgnr_field":'orgnrField',
        "kode_type_field":'kodeTypeField',
        "kode_tekst_field":'kodeTekstField',
        "navn_field":'navnField',
        "postnr_field":'postnrField',
        "poststed_field":'poststedField',
        "eierandel_field":'eierandelField'
    }

    def __init__(self,
                 orgnr_field=None,
                 kode_type_field=None,
                 kode_tekst_field=None,
                 navn_field=None,
                 postnr_field=None,
                 poststed_field=None,
                 eierandel_field=None,
                 additional_properties = {}):
        """Constructor for the Datterselskap class"""

        # Initialize members of the class
        self.orgnr_field = orgnr_field
        self.kode_type_field = kode_type_field
        self.kode_tekst_field = kode_tekst_field
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
        kode_type_field = dictionary.get('kodeTypeField')
        kode_tekst_field = dictionary.get('kodeTekstField')
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
                   kode_type_field,
                   kode_tekst_field,
                   navn_field,
                   postnr_field,
                   poststed_field,
                   eierandel_field,
                   dictionary)


