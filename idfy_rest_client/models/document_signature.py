# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.document_signature

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.social_security_number

class DocumentSignature(object):

    """Implementation of the 'DocumentSignature' model.

    TODO: type model description here.

    Attributes:
        signature_method (SignatureMethod): The signature method used to sign
            the document
        full_name (string): Full name of the signer retrieved from the
            signature-method provider
        first_name (string): First name of the signer
        last_name (string): Last name of the signer
        middle_name (string): Middle name of the signer
        signed_time (datetime): The time signature was registered (ISO 8601)
        date_of_birth (string): The signers date of birth (ddMMyy)
        signature_method_unique_id (string): The signature method unique Id
        social_security_number (SocialSecurityNumber): The signers social
            security number, this will get a value if you specified that you
            wanted social security number in your request (if you are allowed
            to)
        client_ip (string): The Ip address of the signer

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signature_method":'signatureMethod',
        "full_name":'fullName',
        "first_name":'firstName',
        "last_name":'lastName',
        "middle_name":'middleName',
        "signed_time":'signedTime',
        "date_of_birth":'dateOfBirth',
        "signature_method_unique_id":'signatureMethodUniqueId',
        "social_security_number":'socialSecurityNumber',
        "client_ip":'clientIp'
    }

    def __init__(self,
                 signature_method=None,
                 full_name=None,
                 first_name=None,
                 last_name=None,
                 middle_name=None,
                 signed_time=None,
                 date_of_birth=None,
                 signature_method_unique_id=None,
                 social_security_number=None,
                 client_ip=None,
                 additional_properties = {}):
        """Constructor for the DocumentSignature class"""

        # Initialize members of the class
        self.signature_method = signature_method
        self.full_name = full_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.signed_time = APIHelper.RFC3339DateTime(signed_time) if signed_time else None
        self.date_of_birth = date_of_birth
        self.signature_method_unique_id = signature_method_unique_id
        self.social_security_number = social_security_number
        self.client_ip = client_ip

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
        signature_method = dictionary.get('signatureMethod')
        full_name = dictionary.get('fullName')
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        middle_name = dictionary.get('middleName')
        signed_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("signedTime")).datetime if dictionary.get("signedTime") else None
        date_of_birth = dictionary.get('dateOfBirth')
        signature_method_unique_id = dictionary.get('signatureMethodUniqueId')
        social_security_number = idfy_rest_client.models.social_security_number.SocialSecurityNumber.from_dictionary(dictionary.get('socialSecurityNumber')) if dictionary.get('socialSecurityNumber') else None
        client_ip = dictionary.get('clientIp')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(signature_method,
                   full_name,
                   first_name,
                   last_name,
                   middle_name,
                   signed_time,
                   date_of_birth,
                   signature_method_unique_id,
                   social_security_number,
                   client_ip,
                   dictionary)


