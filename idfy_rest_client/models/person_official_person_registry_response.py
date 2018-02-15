# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_official_person_registry_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonOfficialPersonRegistryResponse(object):

    """Implementation of the 'Person.OfficialPersonRegistryResponse' model.

    TODO: type model description here.

    Attributes:
        first_name (string): TODO: type description here.
        last_name (string): TODO: type description here.
        middle_name (string): TODO: type description here.
        fullname (string): TODO: type description here.
        address (string): TODO: type description here.
        address_2 (string): TODO: type description here.
        city (string): TODO: type description here.
        postal_code (string): TODO: type description here.
        gender (string): TODO: type description here.
        raw_json (string): TODO: type description here.
        request_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name":'FirstName',
        "last_name":'LastName',
        "middle_name":'MiddleName',
        "fullname":'Fullname',
        "address":'Address',
        "address_2":'Address2',
        "city":'City',
        "postal_code":'PostalCode',
        "gender":'Gender',
        "raw_json":'RawJson',
        "request_id":'RequestId'
    }

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 middle_name=None,
                 fullname=None,
                 address=None,
                 address_2=None,
                 city=None,
                 postal_code=None,
                 gender=None,
                 raw_json=None,
                 request_id=None,
                 additional_properties = {}):
        """Constructor for the PersonOfficialPersonRegistryResponse class"""

        # Initialize members of the class
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.fullname = fullname
        self.address = address
        self.address_2 = address_2
        self.city = city
        self.postal_code = postal_code
        self.gender = gender
        self.raw_json = raw_json
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
        first_name = dictionary.get('FirstName')
        last_name = dictionary.get('LastName')
        middle_name = dictionary.get('MiddleName')
        fullname = dictionary.get('Fullname')
        address = dictionary.get('Address')
        address_2 = dictionary.get('Address2')
        city = dictionary.get('City')
        postal_code = dictionary.get('PostalCode')
        gender = dictionary.get('Gender')
        raw_json = dictionary.get('RawJson')
        request_id = dictionary.get('RequestId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   middle_name,
                   fullname,
                   address,
                   address_2,
                   city,
                   postal_code,
                   gender,
                   raw_json,
                   request_id,
                   dictionary)


