# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_identifikasjon

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonIdentifikasjon(object):

    """Implementation of the 'Person.Identifikasjon' model.

    TODO: type model description here.

    Attributes:
        internref_field (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "internref_field":'internrefField'
    }

    def __init__(self,
                 internref_field=None,
                 additional_properties = {}):
        """Constructor for the PersonIdentifikasjon class"""

        # Initialize members of the class
        self.internref_field = internref_field

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
        internref_field = dictionary.get('internrefField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(internref_field,
                   dictionary)


