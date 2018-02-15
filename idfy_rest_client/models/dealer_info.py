# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.dealer_info

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class DealerInfo(object):

    """Implementation of the 'DealerInfo' model.

    Dealer information

    Attributes:
        id (uuid|string): TODO: type description here.
        reference (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'Id',
        "reference":'Reference'
    }

    def __init__(self,
                 id=None,
                 reference=None,
                 additional_properties = {}):
        """Constructor for the DealerInfo class"""

        # Initialize members of the class
        self.id = id
        self.reference = reference

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
        id = dictionary.get('Id')
        reference = dictionary.get('Reference')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   reference,
                   dictionary)


