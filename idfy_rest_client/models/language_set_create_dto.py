# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.language_set_create_dto

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class LanguageSetCreateDTO(object):

    """Implementation of the 'LanguageSetCreateDTO' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        is_active (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "is_active":'isActive'
    }

    def __init__(self,
                 name=None,
                 is_active=None,
                 additional_properties = {}):
        """Constructor for the LanguageSetCreateDTO class"""

        # Initialize members of the class
        self.name = name
        self.is_active = is_active

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
        name = dictionary.get('name')
        is_active = dictionary.get('isActive')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   is_active,
                   dictionary)


