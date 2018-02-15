# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_person_information

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class PersonPersonInformation(object):

    """Implementation of the 'Person.PersonInformation' model.

    TODO: type model description here.

    Attributes:
        firstname (string): TODO: type description here.
        middlename (string): TODO: type description here.
        lastname (string): TODO: type description here.
        date_of_birth (string): TODO: type description here.
        address (string): TODO: type description here.
        zip_code (string): TODO: type description here.
        city (string): TODO: type description here.
        mobile (string): TODO: type description here.
        phone (string): TODO: type description here.
        gender (string): TODO: type description here.
        raw_json (string): TODO: type description here.
        request_id (string): TODO: type description here.
        dead (datetime): TODO: type description here.
        source (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "firstname":'Firstname',
        "middlename":'Middlename',
        "lastname":'Lastname',
        "date_of_birth":'DateOfBirth',
        "address":'Address',
        "zip_code":'ZipCode',
        "city":'City',
        "mobile":'Mobile',
        "phone":'Phone',
        "gender":'Gender',
        "raw_json":'RawJson',
        "request_id":'RequestId',
        "dead":'Dead',
        "source":'Source'
    }

    def __init__(self,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 date_of_birth=None,
                 address=None,
                 zip_code=None,
                 city=None,
                 mobile=None,
                 phone=None,
                 gender=None,
                 raw_json=None,
                 request_id=None,
                 dead=None,
                 source=None,
                 additional_properties = {}):
        """Constructor for the PersonPersonInformation class"""

        # Initialize members of the class
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.mobile = mobile
        self.phone = phone
        self.gender = gender
        self.raw_json = raw_json
        self.request_id = request_id
        self.dead = APIHelper.RFC3339DateTime(dead) if dead else None
        self.source = source

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
        firstname = dictionary.get('Firstname')
        middlename = dictionary.get('Middlename')
        lastname = dictionary.get('Lastname')
        date_of_birth = dictionary.get('DateOfBirth')
        address = dictionary.get('Address')
        zip_code = dictionary.get('ZipCode')
        city = dictionary.get('City')
        mobile = dictionary.get('Mobile')
        phone = dictionary.get('Phone')
        gender = dictionary.get('Gender')
        raw_json = dictionary.get('RawJson')
        request_id = dictionary.get('RequestId')
        dead = APIHelper.RFC3339DateTime.from_value(dictionary.get("Dead")).datetime if dictionary.get("Dead") else None
        source = dictionary.get('Source')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(firstname,
                   middlename,
                   lastname,
                   date_of_birth,
                   address,
                   zip_code,
                   city,
                   mobile,
                   phone,
                   gender,
                   raw_json,
                   request_id,
                   dead,
                   source,
                   dictionary)


