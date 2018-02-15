# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.claim_lite

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class ClaimLite(object):

    """Implementation of the 'ClaimLite' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        value (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'Type',
        "value":'Value'
    }

    def __init__(self,
                 mtype=None,
                 value=None,
                 additional_properties = {}):
        """Constructor for the ClaimLite class"""

        # Initialize members of the class
        self.mtype = mtype
        self.value = value

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
        mtype = dictionary.get('Type')
        value = dictionary.get('Value')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mtype,
                   value,
                   dictionary)


