# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.identification_log_item

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class IdentificationLogItem(object):

    """Implementation of the 'IdentificationLogItem' model.

    An identification historic item

    Attributes:
        id (string): The sessionID for the identitication
        name (string): The fullname of the user as reported back from the
            IdentityProvider if the identification was a success
        status (string): The status of the identification process. If not
            success the identification process is not completed.
        client_ip (string): The IP-address of the user
        user_agent (string): The users user-agent (browser/device)
        identity_provider_type (string): The identityprovider type (Norwegian
            BanKID, SwedishBankID, Nemid, etc)
        language (string): The language  used for the identification process
        externalid (string): The merchants reference to the identification
            process, this will also be used to identify an identification in a
            detailed invoice.
        errorcode (string): The error code for the error
        timestamp (datetime): The timestamp for the creation of the
            identification process
        i_frame (bool): Was an iFrame used
        social_security_number (bool): Was social securitynumber fetched

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'Id',
        "name":'Name',
        "status":'Status',
        "client_ip":'ClientIp',
        "user_agent":'UserAgent',
        "identity_provider_type":'IdentityProviderType',
        "language":'Language',
        "externalid":'Externalid',
        "errorcode":'Errorcode',
        "timestamp":'Timestamp',
        "i_frame":'iFrame',
        "social_security_number":'SocialSecurityNumber'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 status=None,
                 client_ip=None,
                 user_agent=None,
                 identity_provider_type=None,
                 language=None,
                 externalid=None,
                 errorcode=None,
                 timestamp=None,
                 i_frame=None,
                 social_security_number=None,
                 additional_properties = {}):
        """Constructor for the IdentificationLogItem class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.status = status
        self.client_ip = client_ip
        self.user_agent = user_agent
        self.identity_provider_type = identity_provider_type
        self.language = language
        self.externalid = externalid
        self.errorcode = errorcode
        self.timestamp = APIHelper.RFC3339DateTime(timestamp) if timestamp else None
        self.i_frame = i_frame
        self.social_security_number = social_security_number

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
        id = dictionary.get('Id')
        name = dictionary.get('Name')
        status = dictionary.get('Status')
        client_ip = dictionary.get('ClientIp')
        user_agent = dictionary.get('UserAgent')
        identity_provider_type = dictionary.get('IdentityProviderType')
        language = dictionary.get('Language')
        externalid = dictionary.get('Externalid')
        errorcode = dictionary.get('Errorcode')
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("Timestamp")).datetime if dictionary.get("Timestamp") else None
        i_frame = dictionary.get('iFrame')
        social_security_number = dictionary.get('SocialSecurityNumber')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   status,
                   client_ip,
                   user_agent,
                   identity_provider_type,
                   language,
                   externalid,
                   errorcode,
                   timestamp,
                   i_frame,
                   social_security_number,
                   dictionary)


