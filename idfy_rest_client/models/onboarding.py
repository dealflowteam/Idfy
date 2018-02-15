# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.onboarding

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Onboarding(object):

    """Implementation of the 'Onboarding' model.

    TODO: type model description here.

    Attributes:
        heading (string): TODO: type description here.
        lead_paragraph (string): TODO: type description here.
        logo_url (string): TODO: type description here.
        return_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "heading":'Heading',
        "lead_paragraph":'LeadParagraph',
        "logo_url":'LogoUrl',
        "return_url":'ReturnUrl'
    }

    def __init__(self,
                 heading=None,
                 lead_paragraph=None,
                 logo_url=None,
                 return_url=None,
                 additional_properties = {}):
        """Constructor for the Onboarding class"""

        # Initialize members of the class
        self.heading = heading
        self.lead_paragraph = lead_paragraph
        self.logo_url = logo_url
        self.return_url = return_url

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
        heading = dictionary.get('Heading')
        lead_paragraph = dictionary.get('LeadParagraph')
        logo_url = dictionary.get('LogoUrl')
        return_url = dictionary.get('ReturnUrl')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(heading,
                   lead_paragraph,
                   logo_url,
                   return_url,
                   dictionary)


