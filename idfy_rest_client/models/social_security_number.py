# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.social_security_number

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class SocialSecurityNumber(object):

    """Implementation of the 'SocialSecurityNumber' model.

    TODO: type model description here.

    Attributes:
        value (string): The social security number
        country_code (string): Iso 3166-1 Alfa-2 (2 letters) country code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value":'value',
        "country_code":'countryCode'
    }

    def __init__(self,
                 value=None,
                 country_code=None,
                 additional_properties = {}):
        """Constructor for the SocialSecurityNumber class"""

        # Initialize members of the class
        self.value = value
        self.country_code = country_code

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
        value = dictionary.get('value')
        country_code = dictionary.get('countryCode')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(value,
                   country_code,
                   dictionary)


