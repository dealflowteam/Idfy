# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.signers_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.signer_response import SignerResponse
from ..models.update_signer_request import UpdateSignerRequest

class SignersController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def signers_add(self,
                    document_id,
                    signer):
        """Does a POST request to /signature/documents/{documentId}/signers.

        Create signer

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            signer (SignerWrapper): TODO: type description here. Example: 

        Returns:
            SignerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id,
                                 signer=signer)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/signers'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(signer))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SignerResponse.from_dictionary)

    def signers_list(self,
                     document_id):
        """Does a GET request to /signature/documents/{documentId}/signers.

        List signers

        Args:
            document_id (uuid|string): TODO: type description here. Example: 

        Returns:
            list of SignerResponse: Response from the API. OK

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
        _query_builder += '/signature/documents/{documentId}/signers'
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
        return APIHelper.json_deserialize(_context.response.raw_body, SignerResponse.from_dictionary)

    def signers_update(self,
                       document_id,
                       signer_id,
                       request):
        """Does a PATCH request to /signature/documents/{documentId}/signers/{signerId}.

        Update signer

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            signer_id (uuid|string): TODO: type description here. Example: 
            request (UpdateSignerRequestWrapper): TODO: type description here.
                Example: 

        Returns:
            UpdateSignerRequest: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id,
                                 signer_id=signer_id,
                                 request=request)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/signers/{signerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'signerId': signer_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, UpdateSignerRequest.from_dictionary)

    def signers_delete(self,
                       document_id,
                       signer_id):
        """Does a DELETE request to /signature/documents/{documentId}/signers/{signerId}.

        Delete signer

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            signer_id (uuid|string): TODO: type description here. Example: 

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
                                 signer_id=signer_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/signers/{signerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'signerId': signer_id
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

    def signers_get(self,
                    document_id,
                    signer_id):
        """Does a GET request to /signature/documents/{documentId}/signers/{signerId}.

        Retrieves the details of a single signer.

        Args:
            document_id (uuid|string): TODO: type description here. Example: 
            signer_id (uuid|string): TODO: type description here. Example: 

        Returns:
            SignerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id,
                                 signer_id=signer_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/signers/{signerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id,
            'signerId': signer_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, SignerResponse.from_dictionary)
