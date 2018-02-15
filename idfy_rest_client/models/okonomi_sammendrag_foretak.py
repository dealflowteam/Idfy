# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.okonomi_sammendrag_foretak

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class OkonomiSammendragForetak(object):

    """Implementation of the 'OkonomiSammendragForetak' model.

    TODO: type model description here.

    Attributes:
        regnskaps_av_ar_field (int): TODO: type description here.
        regnskaps_av_mnd_field (int): TODO: type description here.
        totalinntekt_field (long|int): TODO: type description here.
        resultat_for_skatt_field (long|int): TODO: type description here.
        ars_resultat_field (long|int): TODO: type description here.
        sum_eiendeler_field (long|int): TODO: type description here.
        overskuddsprosent_field (float): TODO: type description here.
        totalrentabilitet_field (float): TODO: type description here.
        egenkapitalandel_field (float): TODO: type description here.
        likviditetsgrad_1_field (float): TODO: type description here.
        likviditetsgrad_2_field (float): TODO: type description here.
        overskuddsprosent_bransje_field (float): TODO: type description here.
        totalrentabilitet_bransje_field (float): TODO: type description here.
        egenkapitalandel_bransje_field (float): TODO: type description here.
        likviditetsgrad_1_bransje_field (float): TODO: type description here.
        likviditetsgrad_2_bransje_field (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "regnskaps_av_ar_field":'regnskapsAvArField',
        "regnskaps_av_mnd_field":'regnskapsAvMndField',
        "totalinntekt_field":'totalinntektField',
        "resultat_for_skatt_field":'resultatForSkattField',
        "ars_resultat_field":'arsResultatField',
        "sum_eiendeler_field":'sumEiendelerField',
        "overskuddsprosent_field":'overskuddsprosentField',
        "totalrentabilitet_field":'totalrentabilitetField',
        "egenkapitalandel_field":'egenkapitalandelField',
        "likviditetsgrad_1_field":'likviditetsgrad1Field',
        "likviditetsgrad_2_field":'likviditetsgrad2Field',
        "overskuddsprosent_bransje_field":'overskuddsprosentBransjeField',
        "totalrentabilitet_bransje_field":'totalrentabilitetBransjeField',
        "egenkapitalandel_bransje_field":'egenkapitalandelBransjeField',
        "likviditetsgrad_1_bransje_field":'likviditetsgrad1BransjeField',
        "likviditetsgrad_2_bransje_field":'likviditetsgrad2BransjeField'
    }

    def __init__(self,
                 regnskaps_av_ar_field=None,
                 regnskaps_av_mnd_field=None,
                 totalinntekt_field=None,
                 resultat_for_skatt_field=None,
                 ars_resultat_field=None,
                 sum_eiendeler_field=None,
                 overskuddsprosent_field=None,
                 totalrentabilitet_field=None,
                 egenkapitalandel_field=None,
                 likviditetsgrad_1_field=None,
                 likviditetsgrad_2_field=None,
                 overskuddsprosent_bransje_field=None,
                 totalrentabilitet_bransje_field=None,
                 egenkapitalandel_bransje_field=None,
                 likviditetsgrad_1_bransje_field=None,
                 likviditetsgrad_2_bransje_field=None,
                 additional_properties = {}):
        """Constructor for the OkonomiSammendragForetak class"""

        # Initialize members of the class
        self.regnskaps_av_ar_field = regnskaps_av_ar_field
        self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        self.totalinntekt_field = totalinntekt_field
        self.resultat_for_skatt_field = resultat_for_skatt_field
        self.ars_resultat_field = ars_resultat_field
        self.sum_eiendeler_field = sum_eiendeler_field
        self.overskuddsprosent_field = overskuddsprosent_field
        self.totalrentabilitet_field = totalrentabilitet_field
        self.egenkapitalandel_field = egenkapitalandel_field
        self.likviditetsgrad_1_field = likviditetsgrad_1_field
        self.likviditetsgrad_2_field = likviditetsgrad_2_field
        self.overskuddsprosent_bransje_field = overskuddsprosent_bransje_field
        self.totalrentabilitet_bransje_field = totalrentabilitet_bransje_field
        self.egenkapitalandel_bransje_field = egenkapitalandel_bransje_field
        self.likviditetsgrad_1_bransje_field = likviditetsgrad_1_bransje_field
        self.likviditetsgrad_2_bransje_field = likviditetsgrad_2_bransje_field

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
        regnskaps_av_ar_field = dictionary.get('regnskapsAvArField')
        regnskaps_av_mnd_field = dictionary.get('regnskapsAvMndField')
        totalinntekt_field = dictionary.get('totalinntektField')
        resultat_for_skatt_field = dictionary.get('resultatForSkattField')
        ars_resultat_field = dictionary.get('arsResultatField')
        sum_eiendeler_field = dictionary.get('sumEiendelerField')
        overskuddsprosent_field = dictionary.get('overskuddsprosentField')
        totalrentabilitet_field = dictionary.get('totalrentabilitetField')
        egenkapitalandel_field = dictionary.get('egenkapitalandelField')
        likviditetsgrad_1_field = dictionary.get('likviditetsgrad1Field')
        likviditetsgrad_2_field = dictionary.get('likviditetsgrad2Field')
        overskuddsprosent_bransje_field = dictionary.get('overskuddsprosentBransjeField')
        totalrentabilitet_bransje_field = dictionary.get('totalrentabilitetBransjeField')
        egenkapitalandel_bransje_field = dictionary.get('egenkapitalandelBransjeField')
        likviditetsgrad_1_bransje_field = dictionary.get('likviditetsgrad1BransjeField')
        likviditetsgrad_2_bransje_field = dictionary.get('likviditetsgrad2BransjeField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(regnskaps_av_ar_field,
                   regnskaps_av_mnd_field,
                   totalinntekt_field,
                   resultat_for_skatt_field,
                   ars_resultat_field,
                   sum_eiendeler_field,
                   overskuddsprosent_field,
                   totalrentabilitet_field,
                   egenkapitalandel_field,
                   likviditetsgrad_1_field,
                   likviditetsgrad_2_field,
                   overskuddsprosent_bransje_field,
                   totalrentabilitet_bransje_field,
                   egenkapitalandel_bransje_field,
                   likviditetsgrad_1_bransje_field,
                   likviditetsgrad_2_bransje_field,
                   dictionary)


