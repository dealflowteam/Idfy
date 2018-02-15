# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.company_information_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class CompanyInformationResponse(object):

    """Implementation of the 'CompanyInformationResponse' model.

    TODO: type model description here.

    Attributes:
        org_nr (string): TODO: type description here.
        org_name (string): TODO: type description here.
        address (string): TODO: type description here.
        postal_code (string): TODO: type description here.
        city (string): TODO: type description here.
        country (string): TODO: type description here.
        raw_json (string): TODO: type description here.
        phone (string): TODO: type description here.
        mobile (string): TODO: type description here.
        request_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "org_nr":'OrgNr',
        "org_name":'OrgName',
        "address":'Address',
        "postal_code":'PostalCode',
        "city":'City',
        "country":'Country',
        "raw_json":'RawJson',
        "phone":'Phone',
        "mobile":'Mobile',
        "request_id":'RequestId'
    }

    def __init__(self,
                 org_nr=None,
                 org_name=None,
                 address=None,
                 postal_code=None,
                 city=None,
                 country=None,
                 raw_json=None,
                 phone=None,
                 mobile=None,
                 request_id=None,
                 additional_properties = {}):
        """Constructor for the CompanyInformationResponse class"""

        # Initialize members of the class
        self.org_nr = org_nr
        self.org_name = org_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.raw_json = raw_json
        self.phone = phone
        self.mobile = mobile
        self.request_id = request_id

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
        country = dictionary.get('Country')
        raw_json = dictionary.get('RawJson')
        phone = dictionary.get('Phone')
        mobile = dictionary.get('Mobile')
        request_id = dictionary.get('RequestId')

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
                   country,
                   raw_json,
                   phone,
                   mobile,
                   request_id,
                   dictionary)


