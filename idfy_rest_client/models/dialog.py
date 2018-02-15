# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.dialog

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Dialog(object):

    """Implementation of the 'Dialog' model.

    TODO: type model description here.

    Attributes:
        title (string): The dialog title
        message (string): The dialog text

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title":'title',
        "message":'message'
    }

    def __init__(self,
                 title=None,
                 message=None,
                 additional_properties = {}):
        """Constructor for the Dialog class"""

        # Initialize members of the class
        self.title = title
        self.message = message

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
        title = dictionary.get('title')
        message = dictionary.get('message')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(title,
                   message,
                   dictionary)


