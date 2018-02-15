# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.lei_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.lei_record import LeiRecord
from ..models.search_result import SearchResult
from ..exceptions.api_exception import APIException

class LeiController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def retrieve_lei_record(self,
                            lei):
        """Does a GET request to /information/lei/{lei}/lookup.

        Retrieve the entity record for a given LEI

        Args:
            lei (string): LEI to retrieve

        Returns:
            LeiRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(lei=lei)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/lei/{lei}/lookup'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'lei': lei
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
        if _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 404:
            raise APIException('Not found', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, LeiRecord.from_dictionary)

    def query_lei_records(self,
                          country_code=None,
                          lei=None,
                          legal_name_contains=None,
                          legal_name_equals=None,
                          registration_authority_entity_id=None,
                          page_size=None,
                          page=None):
        """Does a GET request to /information/lei/search.

        QueryLeiRecords for LEI-registered entities with filters

        Args:
            country_code (string, optional): ISO 3166-1 alpha-2 country code
                for country entity is registered in
            lei (string, optional): LEI of entity
            legal_name_contains (string, optional): Words included in entity's
                legal name
            legal_name_equals (string, optional): Exact phrase included in
                entity's legal name
            registration_authority_entity_id (string, optional): Entity Id
                provided by local business registry authority. For Norway this
                is the 'organisasjonsnummer' or tax identification number of
                the business
            page_size (int, optional): Size of result set per request.
                Defaults to 25
            page (int, optional): Current page number for result set. Defaults
                to 0

        Returns:
            SearchResult: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/lei/search'
        _query_parameters = {
            'countryCode': country_code,
            'lei': lei,
            'legalNameContains': legal_name_contains,
            'legalNameEquals': legal_name_equals,
            'registrationAuthorityEntityId': registration_authority_entity_id,
            'pageSize': page_size,
            'page': page
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
        if _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SearchResult.from_dictionary)
