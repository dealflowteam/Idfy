# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Signature(object):

    """Implementation of the 'Signature' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        date_of_birth (string): TODO: type description here.
        role (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'Name',
        "date_of_birth":'DateOfBirth',
        "role":'Role'
    }

    def __init__(self,
                 name=None,
                 date_of_birth=None,
                 role=None,
                 additional_properties = {}):
        """Constructor for the Signature class"""

        # Initialize members of the class
        self.name = name
        self.date_of_birth = date_of_birth
        self.role = role

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
        name = dictionary.get('Name')
        date_of_birth = dictionary.get('DateOfBirth')
        role = dictionary.get('Role')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   date_of_birth,
                   role,
                   dictionary)


