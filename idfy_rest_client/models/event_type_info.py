# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.event_type_info

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class EventTypeInfo(object):

    """Implementation of the 'EventTypeInfo' model.

    TODO: type model description here.

    Attributes:
        id (Id): TODO: type description here.
        name (string): TODO: type description here.
        description (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "description":'description'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 additional_properties = {}):
        """Constructor for the EventTypeInfo class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.description = description

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
        description = dictionary.get('description')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   description,
                   dictionary)


