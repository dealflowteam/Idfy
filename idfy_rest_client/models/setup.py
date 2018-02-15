# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.setup

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Setup(object):

    """Implementation of the 'Setup' model.

    TODO: type model description here.

    Attributes:
        request (Request): TODO: type description here.
        reminder (Reminder): TODO: type description here.
        signature_receipt (SignatureReceipt): TODO: type description here.
        final_receipt (FinalReceipt): TODO: type description here.
        canceled (Canceled): TODO: type description here.
        expired (Expired): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request":'request',
        "reminder":'reminder',
        "signature_receipt":'signatureReceipt',
        "final_receipt":'finalReceipt',
        "canceled":'canceled',
        "expired":'expired'
    }

    def __init__(self,
                 request=None,
                 reminder=None,
                 signature_receipt=None,
                 final_receipt=None,
                 canceled=None,
                 expired=None,
                 additional_properties = {}):
        """Constructor for the Setup class"""

        # Initialize members of the class
        self.request = request
        self.reminder = reminder
        self.signature_receipt = signature_receipt
        self.final_receipt = final_receipt
        self.canceled = canceled
        self.expired = expired

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
        request = dictionary.get('request')
        reminder = dictionary.get('reminder')
        signature_receipt = dictionary.get('signatureReceipt')
        final_receipt = dictionary.get('finalReceipt')
        canceled = dictionary.get('canceled')
        expired = dictionary.get('expired')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(request,
                   reminder,
                   signature_receipt,
                   final_receipt,
                   canceled,
                   expired,
                   dictionary)


