# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.languages_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.language_dto import LanguageDTO

class LanguagesController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def list_all_languages(self):
        """Does a GET request to /text/languages.

        Returns a list of all supported languages.

        Returns:
            LanguageDTO: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/text/languages'
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
        return APIHelper.json_deserialize(_context.response.raw_body, LanguageDTO.from_dictionary)

    def retrieve_language(self,
                          id):
        """Does a GET request to /text/languages/{id}.

        Retrieve language

        Args:
            id (int): TODO: type description here. Example: 

        Returns:
            LanguageDTO: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/text/languages/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
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
        return APIHelper.json_deserialize(_context.response.raw_body, LanguageDTO.from_dictionary)
