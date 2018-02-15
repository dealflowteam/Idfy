# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.jwt_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.jwt_validation_response import JwtValidationResponse

class JwtController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def jwt_validate(self,
                     request):
        """Does a POST request to /signature/jwt.

        Validate JWT

        Args:
            request (JwtValidationRequest): TODO: type description here.
                Example: 

        Returns:
            JwtValidationResponse: Response from the API. OK

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
        _query_builder += '/signature/jwt'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, JwtValidationResponse.from_dictionary)
