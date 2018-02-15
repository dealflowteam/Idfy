# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.historisk_rating

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class HistoriskRating(object):

    """Implementation of the 'HistoriskRating' model.

    TODO: type model description here.

    Attributes:
        endr_ar_field (int): TODO: type description here.
        endr_mnd_field (int): TODO: type description here.
        rating_field (string): TODO: type description here.
        limit_field (int): TODO: type description here.
        aktuell_hendelse_field (string): TODO: type description here.
        regn_ar_field (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endr_ar_field":'endrArField',
        "endr_mnd_field":'endrMndField',
        "rating_field":'ratingField',
        "limit_field":'limitField',
        "aktuell_hendelse_field":'aktuellHendelseField',
        "regn_ar_field":'regnArField'
    }

    def __init__(self,
                 endr_ar_field=None,
                 endr_mnd_field=None,
                 rating_field=None,
                 limit_field=None,
                 aktuell_hendelse_field=None,
                 regn_ar_field=None,
                 additional_properties = {}):
        """Constructor for the HistoriskRating class"""

        # Initialize members of the class
        self.endr_ar_field = endr_ar_field
        self.endr_mnd_field = endr_mnd_field
        self.rating_field = rating_field
        self.limit_field = limit_field
        self.aktuell_hendelse_field = aktuell_hendelse_field
        self.regn_ar_field = regn_ar_field

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
        endr_ar_field = dictionary.get('endrArField')
        endr_mnd_field = dictionary.get('endrMndField')
        rating_field = dictionary.get('ratingField')
        limit_field = dictionary.get('limitField')
        aktuell_hendelse_field = dictionary.get('aktuellHendelseField')
        regn_ar_field = dictionary.get('regnArField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(endr_ar_field,
                   endr_mnd_field,
                   rating_field,
                   limit_field,
                   aktuell_hendelse_field,
                   regn_ar_field,
                   dictionary)


