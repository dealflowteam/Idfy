# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.signature_roles_check_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.signature_rights import SignatureRights
from ..models.signature_status_response import SignatureStatusResponse
from ..exceptions.api_exception import APIException

class SignatureRolesCheckController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def get_rights(self,
                   orgnumber,
                   countrycode=None):
        """Does a GET request to /information/signroles/rights.

        Check which person(s) that has the right to sign documents in an
        organization. You will receive lists with names and date of birth for
        the persons allowed for signing / prokura.

        Args:
            orgnumber (string): TODO: type description here. Example: 
            countrycode (string, optional): Default value is "NO"

        Returns:
            SignatureRights: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(orgnumber=orgnumber)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/signroles/rights'
        _query_parameters = {
            'orgnumber': orgnumber,
            'countrycode': countrycode
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
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 404:
            raise APIException('Organization data not found', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SignatureRights.from_dictionary)

    def check_signatures_prokura(self,
                                 data,
                                 includereport=None,
                                 countrycode=None):
        """Does a POST request to /information/signroles/signature/check.

        Check if received signatures and/or prokura are valid. This call
        allows you to do this check for multiple organizations
        simulataneously.
        A valid date of birth in this format [ddMMyy] is required. The persons
        last name plus minimum one other part of the signees name (first,
        (middle) and last name has to be separated by whitespace, comma or ;).
                A report that explains the validity of the signatures can be
        included.

        Args:
            data (SignatureCheckRequest): An array including all the
                organizations you want to check
            includereport (bool, optional): Returns a pdf report explaining
                the validity of the checked signatures, default value is true
            countrycode (string, optional): Default value is "NO"

        Returns:
            SignatureStatusResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(data=data)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/signroles/signature/check'
        _query_parameters = {
            'includereport': includereport,
            'countrycode': countrycode
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(data))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 401:
            raise APIException('Not authorized', _context)
        elif _context.response.status_code == 404:
            raise APIException('Organization data not found', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SignatureStatusResponse.from_dictionary)
