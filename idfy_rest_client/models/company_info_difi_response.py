# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.company_info_difi_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class CompanyInfoDifiResponse(object):

    """Implementation of the 'CompanyInfoDifiResponse' model.

    TODO: type model description here.

    Attributes:
        org_nr (string): TODO: type description here.
        org_name (string): TODO: type description here.
        address (string): TODO: type description here.
        postal_code (string): TODO: type description here.
        city (string): TODO: type description here.
        website (string): TODO: type description here.
        country (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "org_nr":'OrgNr',
        "org_name":'OrgName',
        "address":'Address',
        "postal_code":'PostalCode',
        "city":'City',
        "website":'Website',
        "country":'Country'
    }

    def __init__(self,
                 org_nr=None,
                 org_name=None,
                 address=None,
                 postal_code=None,
                 city=None,
                 website=None,
                 country=None,
                 additional_properties = {}):
        """Constructor for the CompanyInfoDifiResponse class"""

        # Initialize members of the class
        self.org_nr = org_nr
        self.org_name = org_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.website = website
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
        org_nr = dictionary.get('OrgNr')
        org_name = dictionary.get('OrgName')
        address = dictionary.get('Address')
        postal_code = dictionary.get('PostalCode')
        city = dictionary.get('City')
        website = dictionary.get('Website')
        country = dictionary.get('Country')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(org_nr,
                   org_name,
                   address,
                   postal_code,
                   city,
                   website,
                   country,
                   dictionary)


