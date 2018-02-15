# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.norwegian_bank_id_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.parse_sdo_response import ParseSDOResponse
from ..models.validate_sdo_response import ValidateSDOResponse

class NorwegianBankIDController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def no_bank_id_validation_parse_sdo(self,
                                        request):
        """Does a POST request to /validation/no/bankid/parse.

        This service validates and parses the signatures on the SDOdata, to
        validate/parse the SDO we use the validation component from bankID
        norway. 
        This endpoint parses the SDO to readable data and provides you with
        information about the signatures and document.

        Args:
            request (ParseSDORequest): TODO: type description here. Example: 

        Returns:
            ParseSDOResponse: Response from the API. OK

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
        _query_builder += '/validation/no/bankid/parse'
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
        return APIHelper.json_deserialize(_context.response.raw_body, ParseSDOResponse.from_dictionary)

    def no_bank_id_validation_validate_sdo(self,
                                           request):
        """Does a POST request to /validation/no/bankid/validate.

        This service validates the signatures on the SDOdata, to validate the
        SDO we use the validation component from BankID Norway. 
        In this endpoint you can also include the data from the original
        document to validate that they matches the SDO data, the same goes for
        the signatures. (Ssn is only available if you have an account and
        validate-ssn scope)

        Args:
            request (ValidateSDORequest): TODO: type description here.
                Example: 

        Returns:
            ValidateSDOResponse: Response from the API. OK

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
        _query_builder += '/validation/no/bankid/validate'
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
        return APIHelper.json_deserialize(_context.response.raw_body, ValidateSDOResponse.from_dictionary)
