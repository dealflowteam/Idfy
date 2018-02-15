# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.address

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Address(object):

    """Implementation of the 'Address' model.

    Company address

    Attributes:
        address_1 (string): TODO: type description here.
        address_2 (string): TODO: type description here.
        postal_code (string): TODO: type description here.
        city (string): TODO: type description here.
        country (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_1":'Address1',
        "address_2":'Address2',
        "postal_code":'PostalCode',
        "city":'City',
        "country":'Country'
    }

    def __init__(self,
                 address_1=None,
                 address_2=None,
                 postal_code=None,
                 city=None,
                 country=None,
                 additional_properties = {}):
        """Constructor for the Address class"""

        # Initialize members of the class
        self.address_1 = address_1
        self.address_2 = address_2
        self.postal_code = postal_code
        self.city = city
        self.country = country

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
        address_1 = dictionary.get('Address1')
        address_2 = dictionary.get('Address2')
        postal_code = dictionary.get('PostalCode')
        city = dictionary.get('City')
        country = dictionary.get('Country')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(address_1,
                   address_2,
                   postal_code,
                   city,
                   country,
                   dictionary)


