# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.certificate

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.x_509_certificate

class Certificate(object):

    """Implementation of the 'Certificate' model.

    TODO: type model description here.

    Attributes:
        issuer_name (string): TODO: type description here.
        subject_name (string): TODO: type description here.
        valid_from_date (datetime): TODO: type description here.
        valid_to_date (datetime): TODO: type description here.
        version_number (string): TODO: type description here.
        serial_number (string): TODO: type description here.
        key_algorithm (string): TODO: type description here.
        key_size (string): TODO: type description here.
        unique_id (string): TODO: type description here.
        originator (string): TODO: type description here.
        bank_name (string): TODO: type description here.
        date_of_birth (datetime): TODO: type description here.
        policy_oid (string): TODO: type description here.
        common_name (string): TODO: type description here.
        signing_certficate (string): TODO: type description here.
        x_509_certificate (X509Certificate): TODO: type description here.
        key_usage (string): TODO: type description here.
        email_address (object): TODO: type description here.
        signing_time (datetime): TODO: type description here.
        phone_number (string): TODO: type description here.
        certificate_type (CertificateType): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "issuer_name":'issuerName',
        "subject_name":'subjectName',
        "valid_from_date":'validFromDate',
        "valid_to_date":'validToDate',
        "version_number":'versionNumber',
        "serial_number":'serialNumber',
        "key_algorithm":'keyAlgorithm',
        "key_size":'keySize',
        "unique_id":'uniqueId',
        "originator":'originator',
        "bank_name":'bankName',
        "date_of_birth":'dateOfBirth',
        "policy_oid":'policyOid',
        "common_name":'commonName',
        "signing_certficate":'signingCertficate',
        "x_509_certificate":'x509Certificate',
        "key_usage":'keyUsage',
        "email_address":'emailAddress',
        "signing_time":'signingTime',
        "phone_number":'phoneNumber',
        "certificate_type":'certificateType'
    }

    def __init__(self,
                 issuer_name=None,
                 subject_name=None,
                 valid_from_date=None,
                 valid_to_date=None,
                 version_number=None,
                 serial_number=None,
                 key_algorithm=None,
                 key_size=None,
                 unique_id=None,
                 originator=None,
                 bank_name=None,
                 date_of_birth=None,
                 policy_oid=None,
                 common_name=None,
                 signing_certficate=None,
                 x_509_certificate=None,
                 key_usage=None,
                 email_address=None,
                 signing_time=None,
                 phone_number=None,
                 certificate_type=None,
                 additional_properties = {}):
        """Constructor for the Certificate class"""

        # Initialize members of the class
        self.issuer_name = issuer_name
        self.subject_name = subject_name
        self.valid_from_date = APIHelper.RFC3339DateTime(valid_from_date) if valid_from_date else None
        self.valid_to_date = APIHelper.RFC3339DateTime(valid_to_date) if valid_to_date else None
        self.version_number = version_number
        self.serial_number = serial_number
        self.key_algorithm = key_algorithm
        self.key_size = key_size
        self.unique_id = unique_id
        self.originator = originator
        self.bank_name = bank_name
        self.date_of_birth = APIHelper.RFC3339DateTime(date_of_birth) if date_of_birth else None
        self.policy_oid = policy_oid
        self.common_name = common_name
        self.signing_certficate = signing_certficate
        self.x_509_certificate = x_509_certificate
        self.key_usage = key_usage
        self.email_address = email_address
        self.signing_time = APIHelper.RFC3339DateTime(signing_time) if signing_time else None
        self.phone_number = phone_number
        self.certificate_type = certificate_type

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
        issuer_name = dictionary.get('issuerName')
        subject_name = dictionary.get('subjectName')
        valid_from_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("validFromDate")).datetime if dictionary.get("validFromDate") else None
        valid_to_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("validToDate")).datetime if dictionary.get("validToDate") else None
        version_number = dictionary.get('versionNumber')
        serial_number = dictionary.get('serialNumber')
        key_algorithm = dictionary.get('keyAlgorithm')
        key_size = dictionary.get('keySize')
        unique_id = dictionary.get('uniqueId')
        originator = dictionary.get('originator')
        bank_name = dictionary.get('bankName')
        date_of_birth = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateOfBirth")).datetime if dictionary.get("dateOfBirth") else None
        policy_oid = dictionary.get('policyOid')
        common_name = dictionary.get('commonName')
        signing_certficate = dictionary.get('signingCertficate')
        x_509_certificate = idfy_rest_client.models.x_509_certificate.X509Certificate.from_dictionary(dictionary.get('x509Certificate')) if dictionary.get('x509Certificate') else None
        key_usage = dictionary.get('keyUsage')
        email_address = dictionary.get('emailAddress')
        signing_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("signingTime")).datetime if dictionary.get("signingTime") else None
        phone_number = dictionary.get('phoneNumber')
        certificate_type = dictionary.get('certificateType')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(issuer_name,
                   subject_name,
                   valid_from_date,
                   valid_to_date,
                   version_number,
                   serial_number,
                   key_algorithm,
                   key_size,
                   unique_id,
                   originator,
                   bank_name,
                   date_of_birth,
                   policy_oid,
                   common_name,
                   signing_certficate,
                   x_509_certificate,
                   key_usage,
                   email_address,
                   signing_time,
                   phone_number,
                   certificate_type,
                   dictionary)


