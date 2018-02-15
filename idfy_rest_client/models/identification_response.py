# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.identification_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.error
import idfy_rest_client.models.environment_info

class IdentificationResponse(object):

    """Implementation of the 'IdentificationResponse' model.

    The reponse for the identity process. Contains users name, id number etc

    Attributes:
        name (string): The fullname of the user as reported back from the
            IdentityProvider
        first_name (string): The first name of the user
        middle_name (string): The middle name of the user (not always
            available)
        last_name (string): The last name of the user
        date_of_birth (string): The users date of birth (not always
            available)
        status (Status): The status of the identification process. If not
            success the identification process is not completed.
        social_security_number (string): The social security number for the
            user (if allowed and if the GetSocialSecurityNumber is set to true
            in the request)
        identity_provider_unique_id (string): The uniqueID from the e-ID, this
            ID is unique for the user and is the same every time the user logs
            on. This is not a sensitiv ID and you could store this to identify
            the user in you database.  Remark: The Swedish BankID do not have
            an unique ID.
        identity_provider (IdentityProvider): The identityprovider type
            (Norwegian BanKID, SwedishBankID, Nemid, etc)
        error (Error): Information about error if the identification process
            failed. (Only set if an error occured, if not is null)
        environment_info (EnvironmentInfo): Information about the users
            environment as seen by IdentiSign, can be used to compare with own
            data.
        meta_data (dict<object, string>): A dicitonary with extra information
            from each identityprovider, and extra services. See developer
            documentation for more information
        request_id (string): The RequestId

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'Name',
        "first_name":'FirstName',
        "middle_name":'MiddleName',
        "last_name":'LastName',
        "date_of_birth":'DateOfBirth',
        "status":'Status',
        "social_security_number":'SocialSecurityNumber',
        "identity_provider_unique_id":'IdentityProviderUniqueId',
        "identity_provider":'IdentityProvider',
        "error":'Error',
        "environment_info":'EnvironmentInfo',
        "meta_data":'MetaData',
        "request_id":'RequestId'
    }

    def __init__(self,
                 name=None,
                 first_name=None,
                 middle_name=None,
                 last_name=None,
                 date_of_birth=None,
                 status=None,
                 social_security_number=None,
                 identity_provider_unique_id=None,
                 identity_provider=None,
                 error=None,
                 environment_info=None,
                 meta_data=None,
                 request_id=None,
                 additional_properties = {}):
        """Constructor for the IdentificationResponse class"""

        # Initialize members of the class
        self.name = name
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.status = status
        self.social_security_number = social_security_number
        self.identity_provider_unique_id = identity_provider_unique_id
        self.identity_provider = identity_provider
        self.error = error
        self.environment_info = environment_info
        self.meta_data = meta_data
        self.request_id = request_id

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
        name = dictionary.get('Name')
        first_name = dictionary.get('FirstName')
        middle_name = dictionary.get('MiddleName')
        last_name = dictionary.get('LastName')
        date_of_birth = dictionary.get('DateOfBirth')
        status = dictionary.get('Status')
        social_security_number = dictionary.get('SocialSecurityNumber')
        identity_provider_unique_id = dictionary.get('IdentityProviderUniqueId')
        identity_provider = dictionary.get('IdentityProvider')
        error = idfy_rest_client.models.error.Error.from_dictionary(dictionary.get('Error')) if dictionary.get('Error') else None
        environment_info = idfy_rest_client.models.environment_info.EnvironmentInfo.from_dictionary(dictionary.get('EnvironmentInfo')) if dictionary.get('EnvironmentInfo') else None
        meta_data = dictionary.get('MetaData')
        request_id = dictionary.get('RequestId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   first_name,
                   middle_name,
                   last_name,
                   date_of_birth,
                   status,
                   social_security_number,
                   identity_provider_unique_id,
                   identity_provider,
                   error,
                   environment_info,
                   meta_data,
                   request_id,
                   dictionary)


