# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.create_document_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.data_to_sign
import idfy_rest_client.models.contact_details
import idfy_rest_client.models.signer_response
import idfy_rest_client.models.status_201
import idfy_rest_client.models.advanced_response
import idfy_rest_client.models.notification

class CreateDocumentResponse(object):

    """Implementation of the 'CreateDocumentResponse' model.

    TODO: type model description here.

    Attributes:
        title (string): Signjob title
        description (string): Signjob description
        external_id (string): Your reference to this signjob
        data_to_sign (DataToSign): Data that should be signed
        contact_details (ContactDetails): The companys contact information
        document_id (uuid|string): A unique document Id
        signers (list of SignerResponse): List of all the signers
        meta_data (dict<object, string>): A dicitonary with extra information
            from additional services. See developer documentation for more
            information
        status (Status201): Overall document status
        advanced (AdvancedResponse): For advanced users
        notification (Notification): Manage notifications

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title":'title',
        "description":'description',
        "external_id":'externalId',
        "data_to_sign":'dataToSign',
        "contact_details":'contactDetails',
        "document_id":'documentId',
        "signers":'signers',
        "meta_data":'metaData',
        "status":'status',
        "advanced":'advanced',
        "notification":'notification'
    }

    def __init__(self,
                 title=None,
                 description=None,
                 external_id=None,
                 data_to_sign=None,
                 contact_details=None,
                 document_id=None,
                 signers=None,
                 meta_data=None,
                 status=None,
                 advanced=None,
                 notification=None,
                 additional_properties = {}):
        """Constructor for the CreateDocumentResponse class"""

        # Initialize members of the class
        self.title = title
        self.description = description
        self.external_id = external_id
        self.data_to_sign = data_to_sign
        self.contact_details = contact_details
        self.document_id = document_id
        self.signers = signers
        self.meta_data = meta_data
        self.status = status
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
        document_id = dictionary.get('documentId')
        signers = None
        if dictionary.get('signers') != None:
            signers = list()
            for structure in dictionary.get('signers'):
                signers.append(idfy_rest_client.models.signer_response.SignerResponse.from_dictionary(structure))
        meta_data = dictionary.get('metaData')
        status = idfy_rest_client.models.status_201.Status201.from_dictionary(dictionary.get('status')) if dictionary.get('status') else None
        advanced = idfy_rest_client.models.advanced_response.AdvancedResponse.from_dictionary(dictionary.get('advanced')) if dictionary.get('advanced') else None
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
                   document_id,
                   signers,
                   meta_data,
                   status,
                   advanced,
                   notification,
                   dictionary)


