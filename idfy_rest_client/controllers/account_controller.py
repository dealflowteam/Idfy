# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.account_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.account_name_item import AccountNameItem
from ..models.account import Account
from ..models.account_list_item import AccountListItem
from ..exceptions.api_exception import APIException

class AccountController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def list_account_names(self):
        """Does a GET request to /admin/account/list/names.

        List names of accounts you have access to

        Returns:
            list of AccountNameItem: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account/list/names'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AccountNameItem.from_dictionary)

    def disable_account(self):
        """Does a POST request to /admin/account/disable.

        Set the account as incative / disabled. Requires one of the following
        scopes: [root, account-write, dealer]

        Returns:
            mixed: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account/disable'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
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

    def update_account_styling(self,
                               styling):
        """Does a POST request to /admin/account/styling.

        Upload / Update custom account css. Returns a url with your uploaded
        css. Requires one of the following scopes: [root, account-write,
        dealer]

        Args:
            styling (Styling): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(styling=styling)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account/styling'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(styling))
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

    def update_account_logo(self,
                            account_logo):
        """Does a POST request to /admin/account/logo.

        Upload / Update and resize account logo. Returns a url with your
        uploaded / resized logo. Requires one of the following scopes: [root,
        account-write, dealer]

        Args:
            account_logo (AccountLogo): TODO: type description here. Example:
                
        Returns:
            string: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(account_logo=account_logo)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account/logo'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(account_logo))
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
        return _context.response.raw_body

    def create_account(self,
                       account_details):
        """Does a POST request to /admin/account.

        Requires one of the following scopes: [dealer]

        Args:
            account_details (CreateAccountRequest): TODO: type description
                here. Example: 

        Returns:
            Account: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(account_details=account_details)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(account_details))
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
        return APIHelper.json_deserialize(_context.response.raw_body, Account.from_dictionary)

    def update_account(self,
                       account_details):
        """Does a PUT request to /admin/account.

        Requires one of the following scopes: [root, account-write, dealer]

        Args:
            account_details (UpdateAccountRequest): TODO: type description
                here. Example: 

        Returns:
            Account: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(account_details=account_details)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(account_details))
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
        return APIHelper.json_deserialize(_context.response.raw_body, Account.from_dictionary)

    def retrieve_account(self):
        """Does a GET request to /admin/account.

        Requires one of the following scopes: [root, account-read, dealer]

        Returns:
            Account: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account'
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
        return APIHelper.json_deserialize(_context.response.raw_body, Account.from_dictionary)

    def list_accounts(self,
                      filter_name=None,
                      filter_org_no=None,
                      filter_uni_customer_no=None,
                      filter_created_before=None,
                      filter_created_after=None,
                      filter_last_modified_before=None,
                      filter_last_modified_after=None,
                      filter_dealer_name=None,
                      filter_dealer_reference=None,
                      filter_enabled=None):
        """Does a GET request to /admin/account/list.

        List accounts you have access to

        Args:
            filter_name (string, optional): TODO: type description here.
                Example: 
            filter_org_no (string, optional): TODO: type description here.
                Example: 
            filter_uni_customer_no (string, optional): TODO: type description
                here. Example: 
            filter_created_before (datetime, optional): TODO: type description
                here. Example: 
            filter_created_after (datetime, optional): TODO: type description
                here. Example: 
            filter_last_modified_before (datetime, optional): TODO: type
                description here. Example: 
            filter_last_modified_after (datetime, optional): TODO: type
                description here. Example: 
            filter_dealer_name (string, optional): TODO: type description
                here. Example: 
            filter_dealer_reference (string, optional): TODO: type description
                here. Example: 
            filter_enabled (bool, optional): TODO: type description here.
                Example: 

        Returns:
            list of AccountListItem: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/account/list'
        _query_parameters = {
            'filter.name': filter_name,
            'filter.orgNo': filter_org_no,
            'filter.uniCustomerNo': filter_uni_customer_no,
            'filter.createdBefore': APIHelper.RFC3339DateTime(filter_created_before),
            'filter.createdAfter': APIHelper.RFC3339DateTime(filter_created_after),
            'filter.lastModifiedBefore': APIHelper.RFC3339DateTime(filter_last_modified_before),
            'filter.lastModifiedAfter': APIHelper.RFC3339DateTime(filter_last_modified_after),
            'filter.dealerName': filter_dealer_name,
            'filter.dealerReference': filter_dealer_reference,
            'filter.enabled': filter_enabled
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
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AccountListItem.from_dictionary)
