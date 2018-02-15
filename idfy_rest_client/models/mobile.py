# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.mobile

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Mobile(object):

    """Implementation of the 'Mobile' model.

    TODO: type model description here.

    Attributes:
        country_code (string): TODO: type description here.
        number (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country_code":'countryCode',
        "number":'number'
    }

    def __init__(self,
                 country_code=None,
                 number=None,
                 additional_properties = {}):
        """Constructor for the Mobile class"""

        # Initialize members of the class
        self.country_code = country_code
        self.number = number

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
        country_code = dictionary.get('countryCode')
        number = dictionary.get('number')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(country_code,
                   number,
                   dictionary)


