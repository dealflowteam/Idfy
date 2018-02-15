# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.notification

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.signature_sign_request
import idfy_rest_client.models.reminder_188
import idfy_rest_client.models.signature_receipt_189
import idfy_rest_client.models.final_receipt_190
import idfy_rest_client.models.base_notification

class Notification(object):

    """Implementation of the 'Notification' model.

    Setup your own notification texts, and specify specail settings. Info: you
    also has to setup notifications on the signers you want to notify.

    Attributes:
        sign_request (SignatureSignRequest): Here you can setup email/sms
            notifications notifying the signer that they have a new document
            to sign.
        reminder (Reminder188): Here you can setup email/sms notifications
            reminding the signers that they have unsigned documents.
        signature_receipt (SignatureReceipt189): Here you can setup email/sms
            notifications as a receipt for a retrieved signature
        final_receipt (FinalReceipt190): Here you can setup email/sms
            notifications as a receipt for a signed document (when all the
            required signatures is registered).
        canceled_receipt (BaseNotification): Here you can setup email/sms
            notifications as a receipt when a document is canceled and can no
            longer be signed.
        expired_receipt (BaseNotification): Here you can setup email/sms
            notifications as a receipt when a document is expired and can no
            longer be signed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sign_request":'signRequest',
        "reminder":'reminder',
        "signature_receipt":'signatureReceipt',
        "final_receipt":'finalReceipt',
        "canceled_receipt":'canceledReceipt',
        "expired_receipt":'expiredReceipt'
    }

    def __init__(self,
                 sign_request=None,
                 reminder=None,
                 signature_receipt=None,
                 final_receipt=None,
                 canceled_receipt=None,
                 expired_receipt=None,
                 additional_properties = {}):
        """Constructor for the Notification class"""

        # Initialize members of the class
        self.sign_request = sign_request
        self.reminder = reminder
        self.signature_receipt = signature_receipt
        self.final_receipt = final_receipt
        self.canceled_receipt = canceled_receipt
        self.expired_receipt = expired_receipt

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
        sign_request = idfy_rest_client.models.signature_sign_request.SignatureSignRequest.from_dictionary(dictionary.get('signRequest')) if dictionary.get('signRequest') else None
        reminder = idfy_rest_client.models.reminder_188.Reminder188.from_dictionary(dictionary.get('reminder')) if dictionary.get('reminder') else None
        signature_receipt = idfy_rest_client.models.signature_receipt_189.SignatureReceipt189.from_dictionary(dictionary.get('signatureReceipt')) if dictionary.get('signatureReceipt') else None
        final_receipt = idfy_rest_client.models.final_receipt_190.FinalReceipt190.from_dictionary(dictionary.get('finalReceipt')) if dictionary.get('finalReceipt') else None
        canceled_receipt = idfy_rest_client.models.base_notification.BaseNotification.from_dictionary(dictionary.get('canceledReceipt')) if dictionary.get('canceledReceipt') else None
        expired_receipt = idfy_rest_client.models.base_notification.BaseNotification.from_dictionary(dictionary.get('expiredReceipt')) if dictionary.get('expiredReceipt') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(sign_request,
                   reminder,
                   signature_receipt,
                   final_receipt,
                   canceled_receipt,
                   expired_receipt,
                   dictionary)


