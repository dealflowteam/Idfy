# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.create_document_request_wrapper

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.data_to_sign
import idfy_rest_client.models.contact_details
import idfy_rest_client.models.signer_wrapper
import idfy_rest_client.models.advanced
import idfy_rest_client.models.notification

class CreateDocumentRequestWrapper(object):

    """Implementation of the 'CreateDocumentRequestWrapper' model.

    TODO: type model description here.

    Attributes:
        title (string): Signjob title
        description (string): Signjob description
        external_id (string): Your reference to this signjob
        data_to_sign (DataToSign): Data that should be signed
        contact_details (ContactDetails): The companys contact information
        signers (list of SignerWrapper): TODO: type description here.
        advanced (Advanced): For advanced users
        notification (Notification): Manage notifications

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title":'title',
        "description":'description',
        "external_id":'externalId',
        "data_to_sign":'dataToSign',
        "contact_details":'contactDetails',
        "signers":'signers',
        "advanced":'advanced',
        "notification":'notification'
    }

    def __init__(self,
                 title=None,
                 description=None,
                 external_id=None,
                 data_to_sign=None,
                 contact_details=None,
                 signers=None,
                 advanced=None,
                 notification=None,
                 additional_properties = {}):
        """Constructor for the CreateDocumentRequestWrapper class"""

        # Initialize members of the class
        self.title = title
        self.description = description
        self.external_id = external_id
        self.data_to_sign = data_to_sign
        self.contact_details = contact_details
        self.signers = signers
        self.advanced = advanced
        self.notification = notification

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
        title = dictionary.get('title')
        description = dictionary.get('description')
        external_id = dictionary.get('externalId')
        data_to_sign = idfy_rest_client.models.data_to_sign.DataToSign.from_dictionary(dictionary.get('dataToSign')) if dictionary.get('dataToSign') else None
        contact_details = idfy_rest_client.models.contact_details.ContactDetails.from_dictionary(dictionary.get('contactDetails')) if dictionary.get('contactDetails') else None
        signers = None
        if dictionary.get('signers') != None:
            signers = list()
            for structure in dictionary.get('signers'):
                signers.append(idfy_rest_client.models.signer_wrapper.SignerWrapper.from_dictionary(structure))
        advanced = idfy_rest_client.models.advanced.Advanced.from_dictionary(dictionary.get('advanced')) if dictionary.get('advanced') else None
        notification = idfy_rest_client.models.notification.Notification.from_dictionary(dictionary.get('notification')) if dictionary.get('notification') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(title,
                   description,
                   external_id,
                   data_to_sign,
                   contact_details,
                   signers,
                   advanced,
                   notification,
                   dictionary)


