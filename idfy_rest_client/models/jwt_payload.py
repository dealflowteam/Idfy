# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.jwt_payload

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.signature_error
import idfy_rest_client.models.sign_success

class JwtPayload(object):

    """Implementation of the 'JwtPayload' model.

    TODO: type model description here.

    Attributes:
        account_id (uuid|string): Account Id
        document_id (uuid|string): Document Id
        external_id (string): External document Id
        signer_id (uuid|string): Signer Id
        external_signer_id (string): External signer Id
        error (SignatureError): Error object, will be included on error
        sign_success (SignSuccess): Success object, will be included on sign
            success
        expires (datetime): When the jwt expires (ISO 8601)
        aborted (bool): Set to true if user aborted

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'accountId',
        "document_id":'documentId',
        "external_id":'externalId',
        "signer_id":'signerId',
        "external_signer_id":'externalSignerId',
        "error":'error',
        "sign_success":'signSuccess',
        "expires":'expires',
        "aborted":'aborted'
    }

    def __init__(self,
                 account_id=None,
                 document_id=None,
                 external_id=None,
                 signer_id=None,
                 external_signer_id=None,
                 error=None,
                 sign_success=None,
                 expires=None,
                 aborted=None,
                 additional_properties = {}):
        """Constructor for the JwtPayload class"""

        # Initialize members of the class
        self.account_id = account_id
        self.document_id = document_id
        self.external_id = external_id
        self.signer_id = signer_id
        self.external_signer_id = external_signer_id
        self.error = error
        self.sign_success = sign_success
        self.expires = APIHelper.RFC3339DateTime(expires) if expires else None
        self.aborted = aborted

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
        account_id = dictionary.get('accountId')
        document_id = dictionary.get('documentId')
        external_id = dictionary.get('externalId')
        signer_id = dictionary.get('signerId')
        external_signer_id = dictionary.get('externalSignerId')
        error = idfy_rest_client.models.signature_error.SignatureError.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        sign_success = idfy_rest_client.models.sign_success.SignSuccess.from_dictionary(dictionary.get('signSuccess')) if dictionary.get('signSuccess') else None
        expires = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires")).datetime if dictionary.get("expires") else None
        aborted = dictionary.get('aborted')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_id,
                   document_id,
                   external_id,
                   signer_id,
                   external_signer_id,
                   error,
                   sign_success,
                   expires,
                   aborted,
                   dictionary)


