# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.resources

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Resources(object):

    """Implementation of the 'Resources' model.

    Logo / Styling

    Attributes:
        logo_url (string): The logo uploaded to this account
        css_url (string): Custom css uploaded to this account

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "logo_url":'LogoUrl',
        "css_url":'CssUrl'
    }

    def __init__(self,
                 logo_url=None,
                 css_url=None,
                 additional_properties = {}):
        """Constructor for the Resources class"""

        # Initialize members of the class
        self.logo_url = logo_url
        self.css_url = css_url

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
        logo_url = dictionary.get('LogoUrl')
        css_url = dictionary.get('CssUrl')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(logo_url,
                   css_url,
                   dictionary)


