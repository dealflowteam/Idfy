# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.results_206

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Results206(object):

    """Implementation of the 'Results206' model.

    TODO: type model description here.

    Attributes:
        rights_and_prokura (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rights_and_prokura":'rightsAndProkura'
    }

    def __init__(self,
                 rights_and_prokura=None,
                 additional_properties = {}):
        """Constructor for the Results206 class"""

        # Initialize members of the class
        self.rights_and_prokura = rights_and_prokura

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
        rights_and_prokura = dictionary.get('rightsAndProkura')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(rights_and_prokura,
                   dictionary)


