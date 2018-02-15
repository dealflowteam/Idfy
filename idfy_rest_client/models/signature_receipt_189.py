# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_receipt_189

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.email
import idfy_rest_client.models.sms

class SignatureReceipt189(object):

    """Implementation of the 'SignatureReceipt189' model.

    Here you can setup email/sms notifications as a receipt for a retrieved
    signature

    Attributes:
        email (list of Email): Define your own email texts (Our default texts
            can be used by leaving this blank)
        sms (list of SMS): Define your own sms texts (Our default texts can be
            used by leaving this blank)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email":'email',
        "sms":'sms'
    }

    def __init__(self,
                 email=None,
                 sms=None,
                 additional_properties = {}):
        """Constructor for the SignatureReceipt189 class"""

        # Initialize members of the class
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
        return cls(email,
                   sms,
                   dictionary)


