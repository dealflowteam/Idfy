# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.authentication

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Authentication(object):

    """Implementation of the 'Authentication' model.

    TODO: type model description here.

    Attributes:
        auth_before_sign (bool): If this is set to true, you have to include
            the social security number or SignatureMethod unique id for the
            signer
        social_security_number (string): The signers social security number
        signature_method_unique_id (string): Define this if you have the
            signers unique signaturemethod id (i.e. the norwegian bankid pid).
            Only the person supposed to sign the document will then be allowed
            to sign it.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auth_before_sign":'authBeforeSign',
        "social_security_number":'socialSecurityNumber',
        "signature_method_unique_id":'signatureMethodUniqueId'
    }

    def __init__(self,
                 auth_before_sign=None,
                 social_security_number=None,
                 signature_method_unique_id=None,
                 additional_properties = {}):
        """Constructor for the Authentication class"""

        # Initialize members of the class
        self.auth_before_sign = auth_before_sign
        self.social_security_number = social_security_number
        self.signature_method_unique_id = signature_method_unique_id

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
        auth_before_sign = dictionary.get('authBeforeSign')
        social_security_number = dictionary.get('socialSecurityNumber')
        signature_method_unique_id = dictionary.get('signatureMethodUniqueId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(auth_before_sign,
                   social_security_number,
                   signature_method_unique_id,
                   dictionary)


