# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.language_sets_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.language_set_dto import LanguageSetDTO

class LanguageSetsController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def create_language_set(self,
                            new_language_set=None):
        """Does a POST request to /text/language-sets.

        Creates a new language set.

        Args:
            new_language_set (LanguageSetCreateDTO, optional): TODO: type
                description here. Example: 

        Returns:
            LanguageSetDTO: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/text/language-sets'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(new_language_set))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, LanguageSetDTO.from_dictionary)

    def list_language_sets(self):
        """Does a GET request to /text/language-sets.

        Returns a list of all your language sets.

        Returns:
            list of LanguageSetDTO: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/text/language-sets'
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
        return APIHelper.json_deserialize(_context.response.raw_body, LanguageSetDTO.from_dictionary)

    def update_language_set(self,
                            id,
                            language_set_update=None):
        """Does a PATCH request to /text/language-sets/{id}.

        Updates the specified language set with the parameters passed.

        Args:
            id (int): TODO: type description here. Example: 
            language_set_update (LanguageSetUpdateDTO, optional): TODO: type
                description here. Example: 

        Returns:
            LanguageSetDTO: Response from the API. Success

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
        _query_builder += '/text/language-sets/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(language_set_update))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, LanguageSetDTO.from_dictionary)

    def delete_language_set(self,
                            id):
        """Does a DELETE request to /text/language-sets/{id}.

        Deletes the specified language set.

        Args:
            id (int): TODO: type description here. Example: 

        Returns:
            void: Response from the API. Success

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
        _query_builder += '/text/language-sets/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def retrieve_language_set(self,
                              id):
        """Does a GET request to /text/language-sets/{id}.

        Retrieves the details of a single language set.

        Args:
            id (int): TODO: type description here. Example: 

        Returns:
            LanguageSetDTO: Response from the API. Success

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
        _query_builder += '/text/language-sets/{id}'
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
        return APIHelper.json_deserialize(_context.response.raw_body, LanguageSetDTO.from_dictionary)
