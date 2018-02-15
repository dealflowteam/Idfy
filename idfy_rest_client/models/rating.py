# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.rating

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Rating(object):

    """Implementation of the 'Rating' model.

    TODO: type model description here.

    Attributes:
        rating_1_field (string): TODO: type description here.
        rating_beskrivelse_field (string): TODO: type description here.
        limit_field (int): TODO: type description here.
        aktuell_hendelse_field (string): TODO: type description here.
        delb_grunnfakta_field (string): TODO: type description here.
        delb_eier_jurdisk_field (string): TODO: type description here.
        delb_okonomi_field (string): TODO: type description here.
        delb_betalingserfaring_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rating_1_field":'rating1Field',
        "rating_beskrivelse_field":'ratingBeskrivelseField',
        "limit_field":'limitField',
        "aktuell_hendelse_field":'aktuellHendelseField',
        "delb_grunnfakta_field":'delbGrunnfaktaField',
        "delb_eier_jurdisk_field":'delbEierJurdiskField',
        "delb_okonomi_field":'delbOkonomiField',
        "delb_betalingserfaring_field":'delbBetalingserfaringField'
    }

    def __init__(self,
                 rating_1_field=None,
                 rating_beskrivelse_field=None,
                 limit_field=None,
                 aktuell_hendelse_field=None,
                 delb_grunnfakta_field=None,
                 delb_eier_jurdisk_field=None,
                 delb_okonomi_field=None,
                 delb_betalingserfaring_field=None,
                 additional_properties = {}):
        """Constructor for the Rating class"""

        # Initialize members of the class
        self.rating_1_field = rating_1_field
        self.rating_beskrivelse_field = rating_beskrivelse_field
        self.limit_field = limit_field
        self.aktuell_hendelse_field = aktuell_hendelse_field
        self.delb_grunnfakta_field = delb_grunnfakta_field
        self.delb_eier_jurdisk_field = delb_eier_jurdisk_field
        self.delb_okonomi_field = delb_okonomi_field
        self.delb_betalingserfaring_field = delb_betalingserfaring_field

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
        rating_1_field = dictionary.get('rating1Field')
        rating_beskrivelse_field = dictionary.get('ratingBeskrivelseField')
        limit_field = dictionary.get('limitField')
        aktuell_hendelse_field = dictionary.get('aktuellHendelseField')
        delb_grunnfakta_field = dictionary.get('delbGrunnfaktaField')
        delb_eier_jurdisk_field = dictionary.get('delbEierJurdiskField')
        delb_okonomi_field = dictionary.get('delbOkonomiField')
        delb_betalingserfaring_field = dictionary.get('delbBetalingserfaringField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(rating_1_field,
                   rating_beskrivelse_field,
                   limit_field,
                   aktuell_hendelse_field,
                   delb_grunnfakta_field,
                   delb_eier_jurdisk_field,
                   delb_okonomi_field,
                   delb_betalingserfaring_field,
                   dictionary)


