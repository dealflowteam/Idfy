# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.merchant_sign_transaction

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class MerchantSignTransaction(object):

    """Implementation of the 'MerchantSignTransaction' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): Transaction Id
        account_id (uuid|string): Your account Id
        audit_log_reference (uuid|string): Audit log Id
        external_reference (string): External Reference
        oauth_client_id (string): The oauth client used in this transaction
        ip_address (string): Ip address
        xslt (string): Xslt sha256 hash
        data_to_sign (string): Data to sign sha256 hash
        result (string): Signed data sha256 hash
        certificate (string): Certificate
        time_stamp (datetime): Log save time

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "account_id":'accountId',
        "audit_log_reference":'auditLogReference',
        "external_reference":'externalReference',
        "oauth_client_id":'oauthClientId',
        "ip_address":'ipAddress',
        "xslt":'xslt',
        "data_to_sign":'dataToSign',
        "result":'result',
        "certificate":'certificate',
        "time_stamp":'timeStamp'
    }

    def __init__(self,
                 id=None,
                 account_id=None,
                 audit_log_reference=None,
                 external_reference=None,
                 oauth_client_id=None,
                 ip_address=None,
                 xslt=None,
                 data_to_sign=None,
                 result=None,
                 certificate=None,
                 time_stamp=None,
                 additional_properties = {}):
        """Constructor for the MerchantSignTransaction class"""

        # Initialize members of the class
        self.id = id
        self.account_id = account_id
        self.audit_log_reference = audit_log_reference
        self.external_reference = external_reference
        self.oauth_client_id = oauth_client_id
        self.ip_address = ip_address
        self.xslt = xslt
        self.data_to_sign = data_to_sign
        self.result = result
        self.certificate = certificate
        self.time_stamp = APIHelper.RFC3339DateTime(time_stamp) if time_stamp else None

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
        id = dictionary.get('id')
        account_id = dictionary.get('accountId')
        audit_log_reference = dictionary.get('auditLogReference')
        external_reference = dictionary.get('externalReference')
        oauth_client_id = dictionary.get('oauthClientId')
        ip_address = dictionary.get('ipAddress')
        xslt = dictionary.get('xslt')
        data_to_sign = dictionary.get('dataToSign')
        result = dictionary.get('result')
        certificate = dictionary.get('certificate')
        time_stamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timeStamp")).datetime if dictionary.get("timeStamp") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   account_id,
                   audit_log_reference,
                   external_reference,
                   oauth_client_id,
                   ip_address,
                   xslt,
                   data_to_sign,
                   result,
                   certificate,
                   time_stamp,
                   dictionary)


