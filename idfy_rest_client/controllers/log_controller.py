# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.log_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.identification_log_item import IdentificationLogItem
from ..models.list_result_identification_log_item import ListResultIdentificationLogItem
from ..exceptions.api_exception import APIException

class LogController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def retrieve_a_log_entry(self,
                             request_id):
        """Does a GET request to /identification/log/requestId/{requestId}.

        Gets an historic identification session (older than 14 days)

        Args:
            request_id (string): A request object

        Returns:
            IdentificationLogItem: Response from the API. OK

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
        _query_builder += '/identification/log/requestId/{requestId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'requestId': request_id
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
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IdentificationLogItem.from_dictionary)

    def list_log_entries(self,
                         year,
                         month=None,
                         day=None,
                         status=None,
                         identity_provider_type=None,
                         external_id=None,
                         name=None,
                         skip=None,
                         page_size=None):
        """Does a GET request to /identification/log/filter/{year}.

        Gets an  list of historic identification sessions (older than 14 days)
        by the filter below fetched the last 1000 with a link to next page

        Args:
            year (int): The year to fetch the sessions from
            month (int, optional): Optional: Filter on month
            day (int, optional): Optional: Filter on day
            status (Status, optional): Optional: Filter on status
            identity_provider_type (IdentityProviderType, optional): Optional:
                Filter on identity provider
            external_id (string, optional): The merchants reference to the
                identification process
            name (string, optional): Optional: Filter on the name of the user
            skip (int, optional): Number of pages to skip
            page_size (int, optional): Number of results in each page (max
                1000)

        Returns:
            ListResultIdentificationLogItem: Response from the API. OK

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
        _query_builder += '/identification/log/filter/{year}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'year': year
        })
        _query_parameters = {
            'month': month,
            'day': day,
            'status': status,
            'identityProviderType': identity_provider_type,
            'externalId': external_id,
            'name': name,
            'skip': skip,
            'pageSize': page_size
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
        return APIHelper.json_deserialize(_context.response.raw_body, ListResultIdentificationLogItem.from_dictionary)
