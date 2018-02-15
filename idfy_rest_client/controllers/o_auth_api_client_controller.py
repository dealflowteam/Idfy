# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.o_auth_api_client_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.oauth_api_client_response import OauthAPIClientResponse
from ..models.oauth_client_list_item_response import OauthClientListItemResponse
from ..exceptions.api_exception import APIException

class OAuthAPIClientController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def create_oauth_client(self,
                            api_client):
        """Does a POST request to /admin/oauthclient.

        Create a new oauth api client for the requested account. Requires on
        of the following scopes: [dealer,  oauth-token, root]

        Args:
            api_client (CreateOauthAPIClientRequest): TODO: type description
                here. Example: 

        Returns:
            OauthAPIClientResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(api_client=api_client)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/oauthclient'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(api_client))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OauthAPIClientResponse.from_dictionary)

    def update_oauth_client(self,
                            api_client):
        """Does a PUT request to /admin/oauthclient.

        Updates the requested oauth client on the requested account. Requires
        on of the following scopes: [dealer,  oauth-token, root]

        Args:
            api_client (UpdateOauthAPIClientRequest): TODO: type description
                here. Example: 

        Returns:
            OauthAPIClientResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(api_client=api_client)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/oauthclient'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(api_client))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OauthAPIClientResponse.from_dictionary)

    def disable_oauth_client(self,
                             request):
        """Does a PUT request to /admin/oauthclient/disable.

        Deactivates the requested oauth client. Requires on of the following
        scopes: [dealer,  oauth-token, root]

        Args:
            request (OauthClientId): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Ok

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
        _query_builder += '/admin/oauthclient/disable'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def enable_oauth_client(self,
                            request):
        """Does a PUT request to /admin/oauthclient/enable.

        Activates the requested oauth client. Requires on of the following
        scopes: [dealer,  oauth-token, root]

        Args:
            request (OauthClientId): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Ok

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
        _query_builder += '/admin/oauthclient/enable'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def list_oauth_clients(self):
        """Does a GET request to /admin/oauthclient/list.

        Returns a list of all oauth clients registered on requested account.
        Requires on of the following scopes: [dealer,  oauth-token, root]

        Returns:
            list of OauthClientListItemResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/oauthclient/list'
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
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OauthClientListItemResponse.from_dictionary)

    def delete_oauth_client(self,
                            client_id):
        """Does a DELETE request to /admin/oauthclient/{clientId}.

        Delete oauth API client.  Requires on of the following scopes:
        [dealer,  oauth-token, root]

        Args:
            client_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(client_id=client_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/oauthclient/{clientId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'clientId': client_id
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

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def retrieve_oauth_client(self,
                              client_id):
        """Does a GET request to /admin/oauthclient/{clientId}.

        Returns the requested oauth client with settings. Requires on of the
        following scopes: [dealer,  oauth-token, root]

        Args:
            client_id (string): TODO: type description here. Example: 

        Returns:
            OauthAPIClientResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(client_id=client_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/oauthclient/{clientId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'clientId': client_id
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

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OauthAPIClientResponse.from_dictionary)
