# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_eiendom_norge

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonEiendomNorge(object):

    """Implementation of the 'Person.EiendomNorge' model.

    TODO: type model description here.

    Attributes:
        svar_eiendom_norge_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "svar_eiendom_norge_field":'svarEiendomNorgeField'
    }

    def __init__(self,
                 svar_eiendom_norge_field=None,
                 additional_properties = {}):
        """Constructor for the PersonEiendomNorge class"""

        # Initialize members of the class
        self.svar_eiendom_norge_field = svar_eiendom_norge_field

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
        svar_eiendom_norge_field = dictionary.get('svarEiendomNorgeField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(svar_eiendom_norge_field,
                   dictionary)


