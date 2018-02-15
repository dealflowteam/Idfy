# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_eiendom_liste

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonEiendomListe(object):

    """Implementation of the 'Person.EiendomListe' model.

    TODO: type model description here.

    Attributes:
        kommunenr_field (string): TODO: type description here.
        kommune_navn_field (string): TODO: type description here.
        gardnr_field (int): TODO: type description here.
        bruksnr_field (int): TODO: type description here.
        festenr_field (int): TODO: type description here.
        seksjonsnr_field (int): TODO: type description here.
        type_field (string): TODO: type description here.
        andel_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kommunenr_field":'kommunenrField',
        "kommune_navn_field":'kommuneNavnField',
        "gardnr_field":'gardnrField',
        "bruksnr_field":'bruksnrField',
        "festenr_field":'festenrField',
        "seksjonsnr_field":'seksjonsnrField',
        "type_field":'typeField',
        "andel_field":'andelField'
    }

    def __init__(self,
                 kommunenr_field=None,
                 kommune_navn_field=None,
                 gardnr_field=None,
                 bruksnr_field=None,
                 festenr_field=None,
                 seksjonsnr_field=None,
                 type_field=None,
                 andel_field=None,
                 additional_properties = {}):
        """Constructor for the PersonEiendomListe class"""

        # Initialize members of the class
        self.kommunenr_field = kommunenr_field
        self.kommune_navn_field = kommune_navn_field
        self.gardnr_field = gardnr_field
        self.bruksnr_field = bruksnr_field
        self.festenr_field = festenr_field
        self.seksjonsnr_field = seksjonsnr_field
        self.type_field = type_field
        self.andel_field = andel_field

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
        kommunenr_field = dictionary.get('kommunenrField')
        kommune_navn_field = dictionary.get('kommuneNavnField')
        gardnr_field = dictionary.get('gardnrField')
        bruksnr_field = dictionary.get('bruksnrField')
        festenr_field = dictionary.get('festenrField')
        seksjonsnr_field = dictionary.get('seksjonsnrField')
        type_field = dictionary.get('typeField')
        andel_field = dictionary.get('andelField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(kommunenr_field,
                   kommune_navn_field,
                   gardnr_field,
                   bruksnr_field,
                   festenr_field,
                   seksjonsnr_field,
                   type_field,
                   andel_field,
                   dictionary)


