# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.invoice_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.transaction import Transaction
from ..exceptions.api_exception import APIException

class InvoiceController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def list_account_transactions(self,
                                  year,
                                  month=None,
                                  get_as_csv=None):
        """Does a GET request to /admin/invoice.

        Returns a list of transactions for the requested account. Requires on
        of the following scopes: [dealer, account-read, root]

        Args:
            year (int): Define a year
            month (int, optional): Define a month (0 - 12), not required
            get_as_csv (bool, optional): If this is set to true a csv file is
                returned insted of transactionlist

        Returns:
            list of Transaction: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(year=year)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/invoice'
        _query_parameters = {
            'year': year,
            'month': month,
            'getAsCsv': get_as_csv
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
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Transaction.from_dictionary)
