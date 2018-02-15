# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.norwgian_bank_id_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.create_bank_id_mobile_response import CreateBankIDMobileResponse
from ..exceptions.api_exception import APIException

class NorwgianBankIDController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def create_mobile_session(self,
                              model):
        """Does a POST request to /identification/no/bankid/mobile.

        Create a new BankID mobile session to start the identification
        process. Returns requestID and a merchant ref.
        If the user do not have BankID mobile of have inputed inncorrect
        values the InvalidMobileNumberOrDateOfBirth will be returned as true
        If there is an error the error code will be returned also.

        Args:
            model (CreateBankIDMobileRequest): A request object

        Returns:
            CreateBankIDMobileResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(model=model)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/identification/no/bankid/mobile'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(model))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request (One or more of the request properties are missing or are on a wrong format)', _context)
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CreateBankIDMobileResponse.from_dictionary)
