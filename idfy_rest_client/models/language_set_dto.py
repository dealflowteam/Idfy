# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.language_set_dto

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class LanguageSetDTO(object):

    """Implementation of the 'LanguageSetDTO' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        is_active (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "created_at":'createdAt',
        "updated_at":'updatedAt',
        "is_active":'isActive'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 created_at=None,
                 updated_at=None,
                 is_active=None,
                 additional_properties = {}):
        """Constructor for the LanguageSetDTO class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
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
        id = dictionary.get('id')
        name = dictionary.get('name')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdAt")).datetime if dictionary.get("createdAt") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updatedAt")).datetime if dictionary.get("updatedAt") else None
        is_active = dictionary.get('isActive')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   created_at,
                   updated_at,
                   is_active,
                   dictionary)


