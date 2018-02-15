# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.signature_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.merchant_sign_transaction import MerchantSignTransaction
from ..models.sign_response import SignResponse

class SignatureController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def signature_get(self,
                      transaction_id):
        """Does a GET request to /merchant/signature/{transactionId}.

        Get a single transaction

        Args:
            transaction_id (uuid|string): TODO: type description here.
                Example: 

        Returns:
            MerchantSignTransaction: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(transaction_id=transaction_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/merchant/signature/{transactionId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'transactionId': transaction_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, MerchantSignTransaction.from_dictionary)

    def signature_sign(self,
                       request):
        """Does a POST request to /merchant/signature.

        Create a merchant signature

        Args:
            request (SignRequest): TODO: type description here. Example: 

        Returns:
            SignResponse: Response from the API. OK

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
        _query_builder += '/merchant/signature'
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
        return APIHelper.json_deserialize(_context.response.raw_body, SignResponse.from_dictionary)

    def signature_list(self,
                       oauth_client_id,
                       from_date=None,
                       to_date=None):
        """Does a GET request to /merchant/signature/list.

        Get a selection of transactions

        Args:
            oauth_client_id (string): TODO: type description here. Example: 
            from_date (long|int, optional): Date in ticks
            to_date (long|int, optional): Date in ticks

        Returns:
            list of MerchantSignTransaction: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(oauth_client_id=oauth_client_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/merchant/signature/list'
        _query_parameters = {
            'oauthClientId': oauth_client_id,
            'fromDate': from_date,
            'toDate': to_date
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
        return APIHelper.json_deserialize(_context.response.raw_body, MerchantSignTransaction.from_dictionary)
