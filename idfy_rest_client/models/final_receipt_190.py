# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.final_receipt_190

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.email
import idfy_rest_client.models.sms

class FinalReceipt190(object):

    """Implementation of the 'FinalReceipt190' model.

    Here you can setup email/sms notifications as a receipt for a signed
    document (when all the required signatures is registered).

    Attributes:
        include_signed_file (bool): You can include the signed document as an
            attachment in the receipt if you wish (We don't recommend to do
            this with sensitive documents).
        email (list of Email): Define your own email texts (Our default texts
            can be used by leaving this blank)
        sms (list of SMS): Define your own sms texts (Our default texts can be
            used by leaving this blank)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "include_signed_file":'includeSignedFile',
        "email":'email',
        "sms":'sms'
    }

    def __init__(self,
                 include_signed_file=None,
                 email=None,
                 sms=None,
                 additional_properties = {}):
        """Constructor for the FinalReceipt190 class"""

        # Initialize members of the class
        self.include_signed_file = include_signed_file
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
        include_signed_file = dictionary.get('includeSignedFile')
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
        return cls(include_signed_file,
                   email,
                   sms,
                   dictionary)


