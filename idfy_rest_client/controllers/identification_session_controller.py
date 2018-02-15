# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.identification_session_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.identification_complete_response import IdentificationCompleteResponse
from ..models.create_identification_response import CreateIdentificationResponse
from ..models.identification_response import IdentificationResponse
from ..exceptions.api_exception import APIException

class IdentificationSessionController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def invalidate_session(self,
                           value):
        """Does a PUT request to /identification/session/invalidate.

        Invalidate the identification session to avoid using the same request
        twice. (remark: if the session is in error the session will not be
        invalidated)

        Args:
            value (InvalidateIdentificationRequest): A request object

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(value=value)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/identification/session/invalidate'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(value))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def is_session_done(self,
                        request_id):
        """Does a GET request to /identification/session/status.

        Checks the status of the identification session, returns OK if
        complete

        Args:
            request_id (string): The requestId returned in the creation of the
                request

        Returns:
            IdentificationCompleteResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(request_id=request_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/identification/session/status'
        _query_parameters = {
            'requestId': request_id
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

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IdentificationCompleteResponse.from_dictionary)

    def create_session(self,
                       request):
        """Does a POST request to /identification/session.

        Creates a new identification session

        Args:
            request (CreateIdentificationRequest): A request object

        Returns:
            CreateIdentificationResponse: Response from the API. OK

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
        _query_builder += '/identification/session'
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

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request (One or more of the request properties are missing or are on a wrong format)', _context)
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CreateIdentificationResponse.from_dictionary)

    def retrieve_session_response(self,
                                  request_id,
                                  meta_data=None):
        """Does a GET request to /identification/session.

        Gets the response of the identifaction session (status, name, unique
        identifier from e-Id, ssn (if allowed) and other metadata about the
        user)
        REMARK: Only authenticate users when the identitication status is
        equal to SUCCESS.

        Args:
            request_id (string): The requestId returned in the creation of the
                session
            meta_data (bool, optional): Should metadata be included in the
                response, only set to true if need (addons and user
                ceritifcate)

        Returns:
            IdentificationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(request_id=request_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/identification/session'
        _query_parameters = {
            'requestId': request_id,
            'metaData': meta_data
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

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IdentificationResponse.from_dictionary)
