# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.sdo_signers

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.certificate

class SDOSigners(object):

    """Implementation of the 'SDOSigners' model.

    TODO: type model description here.

    Attributes:
        certificate (Certificate): TODO: type description here.
        name (string): TODO: type description here.
        date_of_birth (datetime): TODO: type description here.
        pid (string): TODO: type description here.
        ssn (string): TODO: type description here.
        signed_timestamp (datetime): TODO: type description here.
        valid (bool): TODO: type description here.
        ocsp (string): TODO: type description here.
        environment (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "certificate":'certificate',
        "name":'name',
        "date_of_birth":'dateOfBirth',
        "pid":'pid',
        "ssn":'ssn',
        "signed_timestamp":'signedTimestamp',
        "valid":'valid',
        "ocsp":'ocsp',
        "environment":'environment'
    }

    def __init__(self,
                 certificate=None,
                 name=None,
                 date_of_birth=None,
                 pid=None,
                 ssn=None,
                 signed_timestamp=None,
                 valid=None,
                 ocsp=None,
                 environment=None,
                 additional_properties = {}):
        """Constructor for the SDOSigners class"""

        # Initialize members of the class
        self.certificate = certificate
        self.name = name
        self.date_of_birth = APIHelper.RFC3339DateTime(date_of_birth) if date_of_birth else None
        self.pid = pid
        self.ssn = ssn
        self.signed_timestamp = APIHelper.RFC3339DateTime(signed_timestamp) if signed_timestamp else None
        self.valid = valid
        self.ocsp = ocsp
        self.environment = environment

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
        certificate = idfy_rest_client.models.certificate.Certificate.from_dictionary(dictionary.get('certificate')) if dictionary.get('certificate') else None
        name = dictionary.get('name')
        date_of_birth = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateOfBirth")).datetime if dictionary.get("dateOfBirth") else None
        pid = dictionary.get('pid')
        ssn = dictionary.get('ssn')
        signed_timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("signedTimestamp")).datetime if dictionary.get("signedTimestamp") else None
        valid = dictionary.get('valid')
        ocsp = dictionary.get('ocsp')
        environment = dictionary.get('environment')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(certificate,
                   name,
                   date_of_birth,
                   pid,
                   ssn,
                   signed_timestamp,
                   valid,
                   ocsp,
                   environment,
                   dictionary)


