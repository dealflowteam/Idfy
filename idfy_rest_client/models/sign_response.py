# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.sign_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.merchant_error

class SignResponse(object):

    """Implementation of the 'SignResponse' model.

    TODO: type model description here.

    Attributes:
        signed_data (string): base 64 encoded signed data
        audit_log_reference (uuid|string): Reference Id to audit log
        signing_format (SigningFormat): Signing format
        error (MerchantError): Error message
        sign_certificate_base_64_string (string): Signed with certificate
        transaction_id (uuid|string): Id to look up the transaction at a later
            time

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signed_data":'signedData',
        "audit_log_reference":'auditLogReference',
        "signing_format":'signingFormat',
        "error":'error',
        "sign_certificate_base_64_string":'signCertificateBase64String',
        "transaction_id":'transactionId'
    }

    def __init__(self,
                 signed_data=None,
                 audit_log_reference=None,
                 signing_format=None,
                 error=None,
                 sign_certificate_base_64_string=None,
                 transaction_id=None,
                 additional_properties = {}):
        """Constructor for the SignResponse class"""

        # Initialize members of the class
        self.signed_data = signed_data
        self.audit_log_reference = audit_log_reference
        self.signing_format = signing_format
        self.error = error
        self.sign_certificate_base_64_string = sign_certificate_base_64_string
        self.transaction_id = transaction_id

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
        signed_data = dictionary.get('signedData')
        audit_log_reference = dictionary.get('auditLogReference')
        signing_format = dictionary.get('signingFormat')
        error = idfy_rest_client.models.merchant_error.MerchantError.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        sign_certificate_base_64_string = dictionary.get('signCertificateBase64String')
        transaction_id = dictionary.get('transactionId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(signed_data,
                   audit_log_reference,
                   signing_format,
                   error,
                   sign_certificate_base_64_string,
                   transaction_id,
                   dictionary)


