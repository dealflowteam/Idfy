# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_styling

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class SignatureStyling(object):

    """Implementation of the 'signatureStyling' model.

    TODO: type model description here.

    Attributes:
        color_theme (ColorTheme): Sets color theme for the application
        spinner (Spinner): Set the type of spinner to show in loading screens

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "color_theme":'colorTheme',
        "spinner":'spinner'
    }

    def __init__(self,
                 color_theme=None,
                 spinner=None,
                 additional_properties = {}):
        """Constructor for the SignatureStyling class"""

        # Initialize members of the class
        self.color_theme = color_theme
        self.spinner = spinner

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
        color_theme = dictionary.get('colorTheme')
        spinner = dictionary.get('spinner')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(color_theme,
                   spinner,
                   dictionary)


