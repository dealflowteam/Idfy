# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.organization_info

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class OrganizationInfo(object):

    """Implementation of the 'OrganizationInfo' model.

    TODO: type model description here.

    Attributes:
        org_no (string): TODO: type description here.
        company_name (string): TODO: type description here.
        country_code (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "org_no":'orgNo',
        "company_name":'companyName',
        "country_code":'countryCode'
    }

    def __init__(self,
                 org_no=None,
                 company_name=None,
                 country_code=None,
                 additional_properties = {}):
        """Constructor for the OrganizationInfo class"""

        # Initialize members of the class
        self.org_no = org_no
        self.company_name = company_name
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
        org_no = dictionary.get('orgNo')
        company_name = dictionary.get('companyName')
        country_code = dictionary.get('countryCode')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(org_no,
                   company_name,
                   country_code,
                   dictionary)


