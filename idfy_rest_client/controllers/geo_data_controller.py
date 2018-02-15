# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.geo_data_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2

class GeoDataController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def list_country_subdivisions(self,
                                  country_code,
                                  lang=None):
        """Does a GET request to /information/geodata/countries/{countryCode}/subdivisions.

        Retrieves a list over top level administrative subdivisions for a
        country with name and ISO 3166-2 region code

        Args:
            country_code (string): ISO 3166-1 country code to look up
            lang (string, optional): Language for result. Defaults to English

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(country_code=country_code)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/geodata/countries/{countryCode}/subdivisions'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'countryCode': country_code
        })
        _query_parameters = {
            'lang': lang
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

    def retrieve_country_info(self,
                              country_code,
                              lang=None):
        """Does a GET request to /information/geodata/countries/{countryCode}.

        Retrieves basic geographical information about a country

        Args:
            country_code (string): ISO 3166-1 country code to look up
            lang (string, optional): Language for result. Defaults to English

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(country_code=country_code)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/geodata/countries/{countryCode}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'countryCode': country_code
        })
        _query_parameters = {
            'lang': lang
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

    def list_countries(self,
                       lang=None):
        """Does a GET request to /information/geodata/countries.

        Lists all countries in the world with English name and ISO 3166-1
        country code

        Args:
            lang (string, optional): Language for result. Defaults to English

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/geodata/countries'
        _query_parameters = {
            'lang': lang
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
