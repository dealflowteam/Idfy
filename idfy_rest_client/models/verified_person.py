# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.verified_person

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class VerifiedPerson(object):

    """Implementation of the 'VerifiedPerson' model.

    Data retrieved before the actual screening (data enhancement).

    Attributes:
        status (list of string): Person status code, e.g. DECEASED, EMIGRATED
        deceased_date (datetime): Date of death
        emigrated_date (datetime): Date of emigration
        role (string): Role in company
        provider (string): Name of data provider
        name (string): Name of person
        gender (Gender): Gender of person
        nat_id_no (string): National Identification Number
        nationality (string): Two-letter code as specified in the ISO 3166
            standard
        birth_date (string): Date of birth for the person

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status":'status',
        "deceased_date":'deceasedDate',
        "emigrated_date":'emigratedDate',
        "role":'role',
        "provider":'provider',
        "name":'name',
        "gender":'gender',
        "nat_id_no":'natIdNo',
        "nationality":'nationality',
        "birth_date":'birthDate'
    }

    def __init__(self,
                 status=None,
                 deceased_date=None,
                 emigrated_date=None,
                 role=None,
                 provider=None,
                 name=None,
                 gender=None,
                 nat_id_no=None,
                 nationality=None,
                 birth_date=None,
                 additional_properties = {}):
        """Constructor for the VerifiedPerson class"""

        # Initialize members of the class
        self.status = status
        self.deceased_date = APIHelper.RFC3339DateTime(deceased_date) if deceased_date else None
        self.emigrated_date = APIHelper.RFC3339DateTime(emigrated_date) if emigrated_date else None
        self.role = role
        self.provider = provider
        self.name = name
        self.gender = gender
        self.nat_id_no = nat_id_no
        self.nationality = nationality
        self.birth_date = birth_date

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
        status = dictionary.get('status')
        deceased_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("deceasedDate")).datetime if dictionary.get("deceasedDate") else None
        emigrated_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("emigratedDate")).datetime if dictionary.get("emigratedDate") else None
        role = dictionary.get('role')
        provider = dictionary.get('provider')
        name = dictionary.get('name')
        gender = dictionary.get('gender')
        nat_id_no = dictionary.get('natIdNo')
        nationality = dictionary.get('nationality')
        birth_date = dictionary.get('birthDate')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(status,
                   deceased_date,
                   emigrated_date,
                   role,
                   provider,
                   name,
                   gender,
                   nat_id_no,
                   nationality,
                   birth_date,
                   dictionary)


