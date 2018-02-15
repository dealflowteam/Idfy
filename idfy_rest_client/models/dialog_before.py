# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.dialog_before

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class DialogBefore(object):

    """Implementation of the 'DialogBefore' model.

    TODO: type model description here.

    Attributes:
        use_check_box (bool): Adds a checkbox the user have to check to
            confirm that the have read the dialog before they can continue
        title (string): The dialog title
        message (string): The dialog text

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "use_check_box":'useCheckBox',
        "title":'title',
        "message":'message'
    }

    def __init__(self,
                 use_check_box=None,
                 title=None,
                 message=None,
                 additional_properties = {}):
        """Constructor for the DialogBefore class"""

        # Initialize members of the class
        self.use_check_box = use_check_box
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
        use_check_box = dictionary.get('useCheckBox')
        title = dictionary.get('title')
        message = dictionary.get('message')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(use_check_box,
                   title,
                   message,
                   dictionary)


