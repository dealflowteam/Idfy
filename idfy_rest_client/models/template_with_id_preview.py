# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.template_with_id_preview

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class TemplateWithIdPreview(object):

    """Implementation of the 'TemplateWithIdPreview' model.

    TODO: type model description here.

    Attributes:
        primary_language (PrimaryLanguage): Primary language to use in the
            preview (required)
        secondary_language (SecondaryLanguage): Secondary language to use in
            the prewview (optional)
        xml_signature (string): Xml package signature in base64 encoding

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "primary_language":'PrimaryLanguage',
        "secondary_language":'SecondaryLanguage',
        "xml_signature":'XmlSignature'
    }

    def __init__(self,
                 primary_language=None,
                 secondary_language=None,
                 xml_signature=None,
                 additional_properties = {}):
        """Constructor for the TemplateWithIdPreview class"""

        # Initialize members of the class
        self.primary_language = primary_language
        self.secondary_language = secondary_language
        self.xml_signature = xml_signature

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
        primary_language = dictionary.get('PrimaryLanguage')
        secondary_language = dictionary.get('SecondaryLanguage')
        xml_signature = dictionary.get('XmlSignature')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(primary_language,
                   secondary_language,
                   xml_signature,
                   dictionary)


