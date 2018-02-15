# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.create_bank_id_mobile_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class CreateBankIDMobileRequest(object):

    """Implementation of the 'CreateBankIDMobileRequest' model.

    Creates a BankID mobile identification process

    Attributes:
        mobile_number (string): Mobile number for the user that is to be
            identified
        date_of_birth (string): Date of birth for the user that is to be
            identified
        get_social_security_number (bool): Should the socialsecuritynumber be
            fetched from the identityprovider? Beware that there is an extra
            cost of doing this every time and one need permission to do it.
        external_reference (string): The merchants reference to the
            identification process
        addonservices (dict<object, string>): List of addon data that can be
            orderd. The result will be in MetaData list of the reponse

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mobile_number":'MobileNumber',
        "date_of_birth":'DateOfBirth',
        "get_social_security_number":'GetSocialSecurityNumber',
        "external_reference":'ExternalReference',
        "addonservices":'Addonservices'
    }

    def __init__(self,
                 mobile_number=None,
                 date_of_birth=None,
                 get_social_security_number=None,
                 external_reference=None,
                 addonservices=None,
                 additional_properties = {}):
        """Constructor for the CreateBankIDMobileRequest class"""

        # Initialize members of the class
        self.mobile_number = mobile_number
        self.date_of_birth = date_of_birth
        self.get_social_security_number = get_social_security_number
        self.external_reference = external_reference
        self.addonservices = addonservices

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
        mobile_number = dictionary.get('MobileNumber')
        date_of_birth = dictionary.get('DateOfBirth')
        get_social_security_number = dictionary.get('GetSocialSecurityNumber')
        external_reference = dictionary.get('ExternalReference')
        addonservices = dictionary.get('Addonservices')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mobile_number,
                   date_of_birth,
                   get_social_security_number,
                   external_reference,
                   addonservices,
                   dictionary)


