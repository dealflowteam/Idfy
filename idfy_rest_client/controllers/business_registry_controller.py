# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.business_registry_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2

class BusinessRegistryController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def list_registration_authorities(self):
        """Does a GET request to /information/businessregistry.

        Retrieves a list of business registration authorities globally

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
        _query_builder += '/information/businessregistry'
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

    def retrieve_registration_authority(self,
                                        authority_code):
        """Does a GET request to /information/businessregistry/{authorityCode}.

        Retrieves detailed information about a specific registration
        authority

        Args:
            authority_code (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(authority_code=authority_code)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/businessregistry/{authorityCode}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'authorityCode': authority_code
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
        return APIHelper.json_deserialize(_context.response.raw_body)
