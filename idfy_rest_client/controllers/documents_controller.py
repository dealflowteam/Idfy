# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.documents_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.document_summary import DocumentSummary
from ..models.status_201 import Status201
from ..models.update_document_request import UpdateDocumentRequest
from ..models.create_document_response import CreateDocumentResponse
from ..models.collection_with_paging_document_summary import CollectionWithPagingDocumentSummary

class DocumentsController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def documents_get_summary(self,
                              document_id):
        """Does a GET request to /signature/documents/{documentId}/summary.

        Get information about a document

        Args:
            document_id (uuid|string): TODO: type description here. Example: 

        Returns:
            DocumentSummary: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/summary'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, DocumentSummary.from_dictionary)

    def documents_status(self,
                         document_id):
        """Does a GET request to /signature/documents/{documentId}/status.

        Get the status of a document

        Args:
            document_id (uuid|string): TODO: type description here. Example: 

        Returns:
            Status201: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/status'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Status201.from_dictionary)

    def documents_cancel(self,
                         document_id,
                         reason):
        """Does a POST request to /signature/documents/{documentId}/cancel.

        Cancel document

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            reason (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id,
                                 reason=reason)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/cancel'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id
        })
        _query_parameters = {
            'reason': reason
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def documents_update(self,
                         document_id,
                         request):
        """Does a PATCH request to /signature/documents/{documentId}.

        Update document

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            request (UpdateDocumentRequestWrapper): TODO: type description
                here. Example: 

        Returns:
            UpdateDocumentRequest: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id,
                                 request=request)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, UpdateDocumentRequest.from_dictionary)

    def documents_get(self,
                      document_id):
        """Does a GET request to /signature/documents/{documentId}.

        Retrieves details of a single document.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 

        Returns:
            CreateDocumentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CreateDocumentResponse.from_dictionary)

    def documents_create(self,
                         request):
        """Does a POST request to /signature/documents.

        Creates a new document. In the response you will receive a document ID
        to retrieve info about the document at a later time. 
        You also receive a URL and unique identifier per signer.

        Args:
            request (CreateDocumentRequestWrapper): TODO: type description
                here. Example: 

        Returns:
            CreateDocumentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(request=request)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CreateDocumentResponse.from_dictionary)

    def documents_get_collection(self,
                                 external_id=None,
                                 signer_id=None,
                                 external_signer_id=None,
                                 from_date=None,
                                 to_date=None,
                                 last_updated=None,
                                 signed_date=None,
                                 name_of_signer=None,
                                 title=None,
                                 status=None,
                                 tags=None,
                                 offset=None,
                                 limit=None):
        """Does a GET request to /signature/documents/summary.

        Queries your documents using the provided parameters.

        Args:
            external_id (string, optional): Documents external id
            signer_id (uuid|string, optional): Signer Id
            external_signer_id (string, optional): External signer Id
            from_date (datetime, optional): Documents created from date
                (ticks)
            to_date (datetime, optional): Documents created to date (ticks)
            last_updated (datetime, optional): Documents updated after this
                date (ticks)
            signed_date (datetime, optional): Documents signed after this date
                (ticks)
            name_of_signer (string, optional): Name of signer
            title (string, optional): TODO: type description here. Example: 
            status (Status329, optional): Document status
            tags (string, optional): Document tags
            offset (int, optional): Used for paging (will be automatically set
                in response links)
            limit (int, optional): Set how many results you want per page
                (max/default 100)

        Returns:
            CollectionWithPagingDocumentSummary: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/summary'
        _query_parameters = {
            'externalId': external_id,
            'signerId': signer_id,
            'externalSignerId': external_signer_id,
            'fromDate': APIHelper.RFC3339DateTime(from_date),
            'toDate': APIHelper.RFC3339DateTime(to_date),
            'lastUpdated': APIHelper.RFC3339DateTime(last_updated),
            'signedDate': APIHelper.RFC3339DateTime(signed_date),
            'nameOfSigner': name_of_signer,
            'title': title,
            'status': status,
            'tags': tags,
            'offset': offset,
            'limit': limit
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CollectionWithPagingDocumentSummary.from_dictionary)
