# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.translation_dto

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class TranslationDTO(object):

    """Implementation of the 'TranslationDTO' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        key (string): TODO: type description here.
        value (string): TODO: type description here.
        language (string): TODO: type description here.
        default_value (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "key":'key',
        "value":'value',
        "language":'language',
        "default_value":'defaultValue'
    }

    def __init__(self,
                 id=None,
                 key=None,
                 value=None,
                 language=None,
                 default_value=None,
                 additional_properties = {}):
        """Constructor for the TranslationDTO class"""

        # Initialize members of the class
        self.id = id
        self.key = key
        self.value = value
        self.language = language
        self.default_value = default_value

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
        id = dictionary.get('id')
        key = dictionary.get('key')
        value = dictionary.get('value')
        language = dictionary.get('language')
        default_value = dictionary.get('defaultValue')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   key,
                   value,
                   language,
                   default_value,
                   dictionary)


