# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.nokkeltall_foretak

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class NokkeltallForetak(object):

    """Implementation of the 'NokkeltallForetak' model.

    TODO: type model description here.

    Attributes:
        regnskaps_av_ar_field (int): TODO: type description here.
        regnskaps_av_mnd_field (int): TODO: type description here.
        overskuddsprosent_field (float): TODO: type description here.
        rentedekningsgrad_field (float): TODO: type description here.
        totalrentabilitet_field (float): TODO: type description here.
        e_k_rentabilitet_field (float): TODO: type description here.
        lang_lagerfinans_field (float): TODO: type description here.
        gjennomsnitt_lager_field (float): TODO: type description here.
        egenkapital_andel_field (float): TODO: type description here.
        tapsbuffer_field (float): TODO: type description here.
        fremmedkapital_kostnad_field (float): TODO: type description here.
        likviditetsgrad_1_field (float): TODO: type description here.
        likviditetsgrad_2_field (float): TODO: type description here.
        likvider_prosent_salg_field (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "regnskaps_av_ar_field":'regnskapsAvArField',
        "regnskaps_av_mnd_field":'regnskapsAvMndField',
        "overskuddsprosent_field":'overskuddsprosentField',
        "rentedekningsgrad_field":'rentedekningsgradField',
        "totalrentabilitet_field":'totalrentabilitetField',
        "e_k_rentabilitet_field":'eKRentabilitetField',
        "lang_lagerfinans_field":'langLagerfinansField',
        "gjennomsnitt_lager_field":'gjennomsnittLagerField',
        "egenkapital_andel_field":'egenkapitalAndelField',
        "tapsbuffer_field":'tapsbufferField',
        "fremmedkapital_kostnad_field":'fremmedkapitalKostnadField',
        "likviditetsgrad_1_field":'likviditetsgrad1Field',
        "likviditetsgrad_2_field":'likviditetsgrad2Field',
        "likvider_prosent_salg_field":'likviderProsentSalgField'
    }

    def __init__(self,
                 regnskaps_av_ar_field=None,
                 regnskaps_av_mnd_field=None,
                 overskuddsprosent_field=None,
                 rentedekningsgrad_field=None,
                 totalrentabilitet_field=None,
                 e_k_rentabilitet_field=None,
                 lang_lagerfinans_field=None,
                 gjennomsnitt_lager_field=None,
                 egenkapital_andel_field=None,
                 tapsbuffer_field=None,
                 fremmedkapital_kostnad_field=None,
                 likviditetsgrad_1_field=None,
                 likviditetsgrad_2_field=None,
                 likvider_prosent_salg_field=None,
                 additional_properties = {}):
        """Constructor for the NokkeltallForetak class"""

        # Initialize members of the class
        self.regnskaps_av_ar_field = regnskaps_av_ar_field
        self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        self.overskuddsprosent_field = overskuddsprosent_field
        self.rentedekningsgrad_field = rentedekningsgrad_field
        self.totalrentabilitet_field = totalrentabilitet_field
        self.e_k_rentabilitet_field = e_k_rentabilitet_field
        self.lang_lagerfinans_field = lang_lagerfinans_field
        self.gjennomsnitt_lager_field = gjennomsnitt_lager_field
        self.egenkapital_andel_field = egenkapital_andel_field
        self.tapsbuffer_field = tapsbuffer_field
        self.fremmedkapital_kostnad_field = fremmedkapital_kostnad_field
        self.likviditetsgrad_1_field = likviditetsgrad_1_field
        self.likviditetsgrad_2_field = likviditetsgrad_2_field
        self.likvider_prosent_salg_field = likvider_prosent_salg_field

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
        overskuddsprosent_field = dictionary.get('overskuddsprosentField')
        rentedekningsgrad_field = dictionary.get('rentedekningsgradField')
        totalrentabilitet_field = dictionary.get('totalrentabilitetField')
        e_k_rentabilitet_field = dictionary.get('eKRentabilitetField')
        lang_lagerfinans_field = dictionary.get('langLagerfinansField')
        gjennomsnitt_lager_field = dictionary.get('gjennomsnittLagerField')
        egenkapital_andel_field = dictionary.get('egenkapitalAndelField')
        tapsbuffer_field = dictionary.get('tapsbufferField')
        fremmedkapital_kostnad_field = dictionary.get('fremmedkapitalKostnadField')
        likviditetsgrad_1_field = dictionary.get('likviditetsgrad1Field')
        likviditetsgrad_2_field = dictionary.get('likviditetsgrad2Field')
        likvider_prosent_salg_field = dictionary.get('likviderProsentSalgField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(regnskaps_av_ar_field,
                   regnskaps_av_mnd_field,
                   overskuddsprosent_field,
                   rentedekningsgrad_field,
                   totalrentabilitet_field,
                   e_k_rentabilitet_field,
                   lang_lagerfinans_field,
                   gjennomsnitt_lager_field,
                   egenkapital_andel_field,
                   tapsbuffer_field,
                   fremmedkapital_kostnad_field,
                   likviditetsgrad_1_field,
                   likviditetsgrad_2_field,
                   likvider_prosent_salg_field,
                   dictionary)


