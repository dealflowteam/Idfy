# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_entity_address

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class LeiEntityAddress(object):

    """Implementation of the 'LeiEntityAddress' model.

    TODO: type model description here.

    Attributes:
        city (string): TODO: type description here.
        country (string): TODO: type description here.
        first_address_line (string): TODO: type description here.
        additional_address_line (list of string): TODO: type description
            here.
        postal_code (string): TODO: type description here.
        region (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "city":'City',
        "country":'Country',
        "first_address_line":'FirstAddressLine',
        "additional_address_line":'AdditionalAddressLine',
        "postal_code":'PostalCode',
        "region":'Region'
    }

    def __init__(self,
                 city=None,
                 country=None,
                 first_address_line=None,
                 additional_address_line=None,
                 postal_code=None,
                 region=None,
                 additional_properties = {}):
        """Constructor for the LeiEntityAddress class"""

        # Initialize members of the class
        self.city = city
        self.country = country
        self.first_address_line = first_address_line
        self.additional_address_line = additional_address_line
        self.postal_code = postal_code
        self.region = region

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
        city = dictionary.get('City')
        country = dictionary.get('Country')
        first_address_line = dictionary.get('FirstAddressLine')
        additional_address_line = dictionary.get('AdditionalAddressLine')
        postal_code = dictionary.get('PostalCode')
        region = dictionary.get('Region')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(city,
                   country,
                   first_address_line,
                   additional_address_line,
                   postal_code,
                   region,
                   dictionary)


