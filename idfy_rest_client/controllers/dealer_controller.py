# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.dealer_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.account_list_item import AccountListItem
from ..models.dealer import Dealer
from ..exceptions.api_exception import APIException

class DealerController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def update_dealer_logo(self,
                           dealer_id,
                           dealer_logo):
        """Does a POST request to /admin/dealer/logo/{dealerId}.

        Set dealer Logo. Requires the following scope: [dealer]

        Args:
            dealer_id (uuid|string): Your Idfy dealer ID
            dealer_logo (DealerLogo): TODO: type description here. Example: 

        Returns:
            string: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(dealer_id=dealer_id,
                                 dealer_logo=dealer_logo)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/dealer/logo/{dealerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'dealerId': dealer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(dealer_logo))
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
        return _context.response.raw_body

    def list_accounts_for_dealer(self,
                                 dealer_id):
        """Does a GET request to /admin/dealer/{dealerId}/accounts.

        Requires the following scope: [dealer-read]

        Args:
            dealer_id (uuid|string): Your Idfy dealer ID

        Returns:
            list of AccountListItem: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(dealer_id=dealer_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/dealer/{dealerId}/accounts'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'dealerId': dealer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
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
        return APIHelper.json_deserialize(_context.response.raw_body, AccountListItem.from_dictionary)

    def update_dealer(self,
                      dealer_id,
                      dealer):
        """Does a POST request to /admin/dealer/{dealerId}.

        Update dealer credentials. Requires the following scope: [dealer]

        Args:
            dealer_id (uuid|string): Your Idfy dealer ID
            dealer (Dealer): TODO: type description here. Example: 

        Returns:
            Dealer: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(dealer_id=dealer_id,
                                 dealer=dealer)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/dealer/{dealerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'dealerId': dealer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(dealer))
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
        return APIHelper.json_deserialize(_context.response.raw_body, Dealer.from_dictionary)

    def retrieve_dealer(self,
                        dealer_id):
        """Does a GET request to /admin/dealer/{dealerId}.

        Requires the following scope: [dealer]

        Args:
            dealer_id (uuid|string): Your Idfy dealer ID

        Returns:
            Dealer: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(dealer_id=dealer_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/dealer/{dealerId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'dealerId': dealer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
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
        return APIHelper.json_deserialize(_context.response.raw_body, Dealer.from_dictionary)
