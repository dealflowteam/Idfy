# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signers

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Signers(object):

    """Implementation of the 'Signers' model.

    TODO: type model description here.

    Attributes:
        identificator (string): TODO: type description here.
        identificator_type (IdentificatorType): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "identificator":'identificator',
        "identificator_type":'identificatorType'
    }

    def __init__(self,
                 identificator=None,
                 identificator_type=None,
                 additional_properties = {}):
        """Constructor for the Signers class"""

        # Initialize members of the class
        self.identificator = identificator
        self.identificator_type = identificator_type

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
        identificator = dictionary.get('identificator')
        identificator_type = dictionary.get('identificatorType')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(identificator,
                   identificator_type,
                   dictionary)


