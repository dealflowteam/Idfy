# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.files_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2

class FilesController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def files_get_signer_attachment(self,
                                    document_id,
                                    attachment_id,
                                    signer_id,
                                    file_format):
        """Does a GET request to /signature/files/documents/{documentId}/attachments/{attachmentId}/signers/{signerId}.

        Retrieves the attachment file for the specified signer.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            attachment_id (uuid|string): TODO: type description here. Example:
                            signer_id (uuid|string): The signers Id
            file_format (FileFormat331): TODO: type description here. Example:
                
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
                                 attachment_id=attachment_id,
                                 signer_id=signer_id,
                                 file_format=file_format)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/files/documents/{documentId}/attachments/{attachmentId}/signers/{signerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'attachmentId': attachment_id,
            'signerId': signer_id
        })
        _query_parameters = {
            'fileFormat': file_format
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
        return APIHelper.json_deserialize(_context.response.raw_body)

    def files_get_attachment(self,
                             document_id,
                             attachment_id,
                             file_format):
        """Does a GET request to /signature/files/documents/{documentId}/attachments/{attachmentId}.

        Retrieves the attachment file.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            attachment_id (uuid|string): TODO: type description here. Example:
                            file_format (FileFormat): TODO: type description here. Example: 

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
                                 attachment_id=attachment_id,
                                 file_format=file_format)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/files/documents/{documentId}/attachments/{attachmentId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'attachmentId': attachment_id
        })
        _query_parameters = {
            'fileFormat': file_format
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
        return APIHelper.json_deserialize(_context.response.raw_body)

    def files_get_signer(self,
                         document_id,
                         signer_id,
                         file_format):
        """Does a GET request to /signature/files/documents/{documentId}/signers/{signerId}.

        Retrieves the signed document file for the specified signer.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            signer_id (uuid|string): The signers Id
            file_format (FileFormat331): TODO: type description here. Example:
                
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
                                 signer_id=signer_id,
                                 file_format=file_format)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/files/documents/{documentId}/signers/{signerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'signerId': signer_id
        })
        _query_parameters = {
            'fileFormat': file_format
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
        return APIHelper.json_deserialize(_context.response.raw_body)

    def files_get(self,
                  document_id,
                  file_format):
        """Does a GET request to /signature/files/documents/{documentId}.

        Retrieves the signed document file.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            file_format (FileFormat): TODO: type description here. Example: 

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
                                 file_format=file_format)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/files/documents/{documentId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id
        })
        _query_parameters = {
            'fileFormat': file_format
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
        return APIHelper.json_deserialize(_context.response.raw_body)
