# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.document_summary

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.status_201
import idfy_rest_client.models.extended_document_signature

class DocumentSummary(object):

    """Implementation of the 'DocumentSummary' model.

    A summary containing core information about a document

    Attributes:
        document_id (uuid|string): Document id
        account_id (uuid|string): Account id
        title (string): Document title
        description (string): Document description
        last_updated (datetime): When was the document last updated (ISO8601)
        deadline (datetime): The sign deadline for the document (ISO8601)
        signed_date (datetime): When was all the signatures processed
            (ISO8601)
        status (Status201): Document status
        external_id (string): External document Id (your Id)
        document_signatures (list of ExtendedDocumentSignature): All the
            signatures received on this document
        required_signatures (int): The number of required signatures on the
            document
        current_signatures (int): How many signatures is completed right now
        tags (list of string): Document tags
        attachments (list of uuid|string): A list of attachment Id's
        signers (list of uuid|string): A list of all the signers on the
            document
        created (datetime): When the document was created (ISO 8601)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_id":'documentId',
        "account_id":'accountId',
        "title":'title',
        "description":'description',
        "last_updated":'lastUpdated',
        "deadline":'deadline',
        "signed_date":'signedDate',
        "status":'status',
        "external_id":'externalId',
        "document_signatures":'documentSignatures',
        "required_signatures":'requiredSignatures',
        "current_signatures":'currentSignatures',
        "tags":'tags',
        "attachments":'attachments',
        "signers":'signers',
        "created":'created'
    }

    def __init__(self,
                 document_id=None,
                 account_id=None,
                 title=None,
                 description=None,
                 last_updated=None,
                 deadline=None,
                 signed_date=None,
                 status=None,
                 external_id=None,
                 document_signatures=None,
                 required_signatures=None,
                 current_signatures=None,
                 tags=None,
                 attachments=None,
                 signers=None,
                 created=None,
                 additional_properties = {}):
        """Constructor for the DocumentSummary class"""

        # Initialize members of the class
        self.document_id = document_id
        self.account_id = account_id
        self.title = title
        self.description = description
        self.last_updated = APIHelper.RFC3339DateTime(last_updated) if last_updated else None
        self.deadline = APIHelper.RFC3339DateTime(deadline) if deadline else None
        self.signed_date = APIHelper.RFC3339DateTime(signed_date) if signed_date else None
        self.status = status
        self.external_id = external_id
        self.document_signatures = document_signatures
        self.required_signatures = required_signatures
        self.current_signatures = current_signatures
        self.tags = tags
        self.attachments = attachments
        self.signers = signers
        self.created = APIHelper.RFC3339DateTime(created) if created else None

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
        document_id = dictionary.get('documentId')
        account_id = dictionary.get('accountId')
        title = dictionary.get('title')
        description = dictionary.get('description')
        last_updated = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastUpdated")).datetime if dictionary.get("lastUpdated") else None
        deadline = APIHelper.RFC3339DateTime.from_value(dictionary.get("deadline")).datetime if dictionary.get("deadline") else None
        signed_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("signedDate")).datetime if dictionary.get("signedDate") else None
        status = idfy_rest_client.models.status_201.Status201.from_dictionary(dictionary.get('status')) if dictionary.get('status') else None
        external_id = dictionary.get('externalId')
        document_signatures = None
        if dictionary.get('documentSignatures') != None:
            document_signatures = list()
            for structure in dictionary.get('documentSignatures'):
                document_signatures.append(idfy_rest_client.models.extended_document_signature.ExtendedDocumentSignature.from_dictionary(structure))
        required_signatures = dictionary.get('requiredSignatures')
        current_signatures = dictionary.get('currentSignatures')
        tags = dictionary.get('tags')
        attachments = dictionary.get('attachments')
        signers = dictionary.get('signers')
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("created")).datetime if dictionary.get("created") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(document_id,
                   account_id,
                   title,
                   description,
                   last_updated,
                   deadline,
                   signed_date,
                   status,
                   external_id,
                   document_signatures,
                   required_signatures,
                   current_signatures,
                   tags,
                   attachments,
                   signers,
                   created,
                   dictionary)


