# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.pades_settings

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PadesSettings(object):

    """Implementation of the 'PadesSettings' model.

    TODO: type model description here.

    Attributes:
        primary_language (PrimaryLanguage): Set the primary language of the
            pades explanatory page. Defaults to english
        secondary_language (SecondaryLanguage): Set the secondary language of
            the pades explanatory page.
        pades_template_id (string): Include your own pades template

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "primary_language":'primaryLanguage',
        "secondary_language":'secondaryLanguage',
        "pades_template_id":'padesTemplateId'
    }

    def __init__(self,
                 primary_language=None,
                 secondary_language=None,
                 pades_template_id=None,
                 additional_properties = {}):
        """Constructor for the PadesSettings class"""

        # Initialize members of the class
        self.primary_language = primary_language
        self.secondary_language = secondary_language
        self.pades_template_id = pades_template_id

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
        primary_language = dictionary.get('primaryLanguage')
        secondary_language = dictionary.get('secondaryLanguage')
        pades_template_id = dictionary.get('padesTemplateId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(primary_language,
                   secondary_language,
                   pades_template_id,
                   dictionary)


