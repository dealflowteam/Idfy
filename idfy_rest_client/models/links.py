# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.links

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Links(object):

    """Implementation of the 'Links' model.

    TODO: type model description here.

    Attributes:
        next (string): TODO: type description here.
        previous (string): TODO: type description here.
        first (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "next":'next',
        "previous":'previous',
        "first":'first'
    }

    def __init__(self,
                 next=None,
                 previous=None,
                 first=None,
                 additional_properties = {}):
        """Constructor for the Links class"""

        # Initialize members of the class
        self.next = next
        self.previous = previous
        self.first = first

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
        next = dictionary.get('next')
        previous = dictionary.get('previous')
        first = dictionary.get('first')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(next,
                   previous,
                   first,
                   dictionary)


