# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.sign_success

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class SignSuccess(object):

    """Implementation of the 'SignSuccess' model.

    TODO: type model description here.

    Attributes:
        signature_method_unique_id (string): The unique id retrieved from the
            signature method provider
        first_name (string): The signers first name
        middle_name (string): The signers middle name
        last_name (string): The signers last name
        full_name (string): The signers full name
        date_of_birth (string): The signers date of birth
        signature_method (SignatureMethod): The signaturemethod used to sign
            the document
        signed_time (datetime): Signed time (ISO 8601)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signature_method_unique_id":'signatureMethodUniqueId',
        "first_name":'firstName',
        "middle_name":'middleName',
        "last_name":'lastName',
        "full_name":'fullName',
        "date_of_birth":'dateOfBirth',
        "signature_method":'signatureMethod',
        "signed_time":'signedTime'
    }

    def __init__(self,
                 signature_method_unique_id=None,
                 first_name=None,
                 middle_name=None,
                 last_name=None,
                 full_name=None,
                 date_of_birth=None,
                 signature_method=None,
                 signed_time=None,
                 additional_properties = {}):
        """Constructor for the SignSuccess class"""

        # Initialize members of the class
        self.signature_method_unique_id = signature_method_unique_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.signature_method = signature_method
        self.signed_time = APIHelper.RFC3339DateTime(signed_time) if signed_time else None

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
        signature_method_unique_id = dictionary.get('signatureMethodUniqueId')
        first_name = dictionary.get('firstName')
        middle_name = dictionary.get('middleName')
        last_name = dictionary.get('lastName')
        full_name = dictionary.get('fullName')
        date_of_birth = dictionary.get('dateOfBirth')
        signature_method = dictionary.get('signatureMethod')
        signed_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("signedTime")).datetime if dictionary.get("signedTime") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(signature_method_unique_id,
                   first_name,
                   middle_name,
                   last_name,
                   full_name,
                   date_of_birth,
                   signature_method,
                   signed_time,
                   dictionary)


