# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.address_list

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class AddressList(object):

    """Implementation of the 'AddressList' model.

    TODO: type model description here.

    Attributes:
        country_name (string): TODO: type description here.
        country_code (string): TODO: type description here.
        street (string): TODO: type description here.
        post_code (string): TODO: type description here.
        city (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country_name":'countryName',
        "country_code":'countryCode',
        "street":'street',
        "post_code":'postCode',
        "city":'city'
    }

    def __init__(self,
                 country_name=None,
                 country_code=None,
                 street=None,
                 post_code=None,
                 city=None,
                 additional_properties = {}):
        """Constructor for the AddressList class"""

        # Initialize members of the class
        self.country_name = country_name
        self.country_code = country_code
        self.street = street
        self.post_code = post_code
        self.city = city

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
        country_name = dictionary.get('countryName')
        country_code = dictionary.get('countryCode')
        street = dictionary.get('street')
        post_code = dictionary.get('postCode')
        city = dictionary.get('city')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(country_name,
                   country_code,
                   street,
                   post_code,
                   city,
                   dictionary)


