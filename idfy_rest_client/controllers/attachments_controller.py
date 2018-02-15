# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.attachments_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.attachment_response import AttachmentResponse
from ..models.attachment_list_item import AttachmentListItem

class AttachmentsController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def attachments_update(self,
                           document_id,
                           attachment_id,
                           request):
        """Does a PATCH request to /signature/documents/{documentId}/attachments/{attachmentId}.

        Updates the specified attachment (Will only take affect if no one has
        signed the document yet)

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            attachment_id (uuid|string): TODO: type description here. Example:
                            request (UpdateAttachmentRequestWrapper): TODO: type description
                here. Example: 

        Returns:
            AttachmentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id,
                                 attachment_id=attachment_id,
                                 request=request)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/attachments/{attachmentId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'attachmentId': attachment_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, AttachmentResponse.from_dictionary)

    def attachments_delete(self,
                           document_id,
                           attachment_id):
        """Does a DELETE request to /signature/documents/{documentId}/attachments/{attachmentId}.

        Deletes the specified attachment (Will only take affect if no one has
        signed the document yet)

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            attachment_id (uuid|string): TODO: type description here. Example:
                
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
                                 attachment_id=attachment_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/attachments/{attachmentId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'attachmentId': attachment_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def attachments_get(self,
                        document_id,
                        attachment_id):
        """Does a GET request to /signature/documents/{documentId}/attachments/{attachmentId}.

        Retrieves the details of a single attachment.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            attachment_id (uuid|string): TODO: type description here. Example:
                
        Returns:
            AttachmentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id,
                                 attachment_id=attachment_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/attachments/{attachmentId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'attachmentId': attachment_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, AttachmentResponse.from_dictionary)

    def attachments_create(self,
                           document_id,
                           request):
        """Does a POST request to /signature/documents/{documentId}/attachments.

        Adds an attachments to the specified document. You can choose between
        different ways to make the user accept the attachment.
                     <span style="color:red;">The attachment will be deleted
                     when the signature job is completed or has
                     expired</span>

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            request (AttachmentRequestWrapper): TODO: type description here.
                Example: 

        Returns:
            AttachmentResponse: Response from the API. 

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
        _query_builder += '/signature/documents/{documentId}/attachments'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AttachmentResponse.from_dictionary)

    def attachments_list(self,
                         document_id):
        """Does a GET request to /signature/documents/{documentId}/attachments.

        Returns a list of all attachments for the specified document.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 

        Returns:
            list of AttachmentListItem: Response from the API. OK

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
        _query_builder += '/signature/documents/{documentId}/attachments'
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
        return APIHelper.json_deserialize(_context.response.raw_body, AttachmentListItem.from_dictionary)
