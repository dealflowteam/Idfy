# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signer_info

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.mobile
import idfy_rest_client.models.organization_info

class SignerInfo(object):

    """Implementation of the 'SignerInfo' model.

    TODO: type model description here.

    Attributes:
        first_name (string): The signers first name
        last_name (string): The signers last name
        email (string): The signers email adress, define this if you are using
            notifications
        mobile (Mobile): The signers mobile, define this if you are using
            notifications
        organization_info (OrganizationInfo): The signers organization info

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name":'firstName',
        "last_name":'lastName',
        "email":'email',
        "mobile":'mobile',
        "organization_info":'organizationInfo'
    }

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 email=None,
                 mobile=None,
                 organization_info=None,
                 additional_properties = {}):
        """Constructor for the SignerInfo class"""

        # Initialize members of the class
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.organization_info = organization_info

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
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        email = dictionary.get('email')
        mobile = idfy_rest_client.models.mobile.Mobile.from_dictionary(dictionary.get('mobile')) if dictionary.get('mobile') else None
        organization_info = idfy_rest_client.models.organization_info.OrganizationInfo.from_dictionary(dictionary.get('organizationInfo')) if dictionary.get('organizationInfo') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   email,
                   mobile,
                   organization_info,
                   dictionary)


