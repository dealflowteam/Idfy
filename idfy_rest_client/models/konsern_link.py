# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.konsern_link

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class KonsernLink(object):

    """Implementation of the 'KonsernLink' model.

    TODO: type model description here.

    Attributes:
        orgnr_overste_mor_field (int): TODO: type description here.
        orgnr_naermeste_mor_field (int): TODO: type description here.
        lopenr_field (int): TODO: type description here.
        niva_deltagende_field (int): TODO: type description here.
        landkode_deltagende_field (string): TODO: type description here.
        orgnr_deltagende_field (int): TODO: type description here.
        navn_deltagende_field (string): TODO: type description here.
        eierandel_deltagende_field (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "orgnr_overste_mor_field":'orgnrOversteMorField',
        "orgnr_naermeste_mor_field":'orgnrNaermesteMorField',
        "lopenr_field":'lopenrField',
        "niva_deltagende_field":'nivaDeltagendeField',
        "landkode_deltagende_field":'landkodeDeltagendeField',
        "orgnr_deltagende_field":'orgnrDeltagendeField',
        "navn_deltagende_field":'navnDeltagendeField',
        "eierandel_deltagende_field":'eierandelDeltagendeField'
    }

    def __init__(self,
                 orgnr_overste_mor_field=None,
                 orgnr_naermeste_mor_field=None,
                 lopenr_field=None,
                 niva_deltagende_field=None,
                 landkode_deltagende_field=None,
                 orgnr_deltagende_field=None,
                 navn_deltagende_field=None,
                 eierandel_deltagende_field=None,
                 additional_properties = {}):
        """Constructor for the KonsernLink class"""

        # Initialize members of the class
        self.orgnr_overste_mor_field = orgnr_overste_mor_field
        self.orgnr_naermeste_mor_field = orgnr_naermeste_mor_field
        self.lopenr_field = lopenr_field
        self.niva_deltagende_field = niva_deltagende_field
        self.landkode_deltagende_field = landkode_deltagende_field
        self.orgnr_deltagende_field = orgnr_deltagende_field
        self.navn_deltagende_field = navn_deltagende_field
        self.eierandel_deltagende_field = eierandel_deltagende_field

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
        orgnr_overste_mor_field = dictionary.get('orgnrOversteMorField')
        orgnr_naermeste_mor_field = dictionary.get('orgnrNaermesteMorField')
        lopenr_field = dictionary.get('lopenrField')
        niva_deltagende_field = dictionary.get('nivaDeltagendeField')
        landkode_deltagende_field = dictionary.get('landkodeDeltagendeField')
        orgnr_deltagende_field = dictionary.get('orgnrDeltagendeField')
        navn_deltagende_field = dictionary.get('navnDeltagendeField')
        eierandel_deltagende_field = dictionary.get('eierandelDeltagendeField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(orgnr_overste_mor_field,
                   orgnr_naermeste_mor_field,
                   lopenr_field,
                   niva_deltagende_field,
                   landkode_deltagende_field,
                   orgnr_deltagende_field,
                   navn_deltagende_field,
                   eierandel_deltagende_field,
                   dictionary)


