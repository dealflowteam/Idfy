# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_sign_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.email
import idfy_rest_client.models.sms

class SignatureSignRequest(object):

    """Implementation of the 'signatureSignRequest' model.

    Here you can setup email/sms notifications notifying the signer that they
    have a new document to sign.

    Attributes:
        include_original_file (bool): Set this to true if you want to include
            the unsigned main document as an attachment to this email message
        email (list of Email): Define your own email texts (Our default texts
            can be used by leaving this blank)
        sms (list of SMS): Define your own sms texts (Our default texts can be
            used by leaving this blank)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "include_original_file":'includeOriginalFile',
        "email":'email',
        "sms":'sms'
    }

    def __init__(self,
                 include_original_file=None,
                 email=None,
                 sms=None,
                 additional_properties = {}):
        """Constructor for the SignatureSignRequest class"""

        # Initialize members of the class
        self.include_original_file = include_original_file
        self.email = email
        self.sms = sms

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
        include_original_file = dictionary.get('includeOriginalFile')
        email = None
        if dictionary.get('email') != None:
            email = list()
            for structure in dictionary.get('email'):
                email.append(idfy_rest_client.models.email.Email.from_dictionary(structure))
        sms = None
        if dictionary.get('sms') != None:
            sms = list()
            for structure in dictionary.get('sms'):
                sms.append(idfy_rest_client.models.sms.SMS.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(include_original_file,
                   email,
                   sms,
                   dictionary)


