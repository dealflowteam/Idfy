# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.aml_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.aml_response import AmlResponse
from ..exceptions.api_exception import APIException

class AmlController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def b_2_b_identify_and_screening_request(self,
                                             name,
                                             ssn=None,
                                             birth_date=None,
                                             nationality=None,
                                             language=None,
                                             include_report=None,
                                             mode=None):
        """Does a GET request to /information/aml/b2b.

        Person screening with data enhancement enabled for nationalities where
        data enhancement is provided. For other nationalities the data
        enhancement will be skipped 
        **Required fields**: Name with either birthDate or ssn.

        Args:
            name (string): Complete name of person.  (Order of first and last
                names is not significant.)
            ssn (string, optional): National Identification number. SSN or
                Birthdate are REQUIRED (Se NationalId format)
            birth_date (string, optional): Date of birth. SSN or Birthdate are
                REQUIRED (format: yyyyMMdd)
            nationality (string, optional): Nationality of person (two letters
                ISO 3166 )
            language (string, optional): Language to use in response where
                applicable, optional. (two letters ISO 3166 )
            include_report (bool, optional): Create a PDF report with the data
                timestamp and sealed as future proof for the process.
            mode (Mode, optional): What mode to use. When using identify and
                screening data enhancement is enabled for nationalities where
                data enhancement is provided.

        Returns:
            AmlResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(name=name)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/aml/b2b'
        _query_parameters = {
            'name': name,
            'ssn': ssn,
            'birthDate': birth_date,
            'nationality': nationality,
            'language': language,
            'includeReport': include_report,
            'mode': mode
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
            raise APIException('Not found', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal Server Error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AmlResponse.from_dictionary)

    def b_2_c_identify_and_screening_request(self,
                                             name,
                                             ssn=None,
                                             birth_date=None,
                                             nationality=None,
                                             language=None,
                                             include_report=None,
                                             mode=None):
        """Does a GET request to /information/aml/b2c.

        Person screening with data enhancement enabled for nationalities where
        data enhancement is provided. For other nationalities the data
        enhancement will be skipped 
        **Required fields**: Name with either birthDate or ssn.

        Args:
            name (string): Complete name of person.  (Order of first and last
                names is not significant.)
            ssn (string, optional): National Identification number. SSN or
                Birthdate are REQUIRED (Se NationalId format)
            birth_date (string, optional): Date of birth. SSN or Birthdate are
                REQUIRED (format: yyyyMMdd)
            nationality (string, optional): Nationality of person (two letters
                ISO 3166 )
            language (string, optional): Language to use in response where
                applicable, optional. (two letters ISO 3166 )
            include_report (bool, optional): Create a PDF report with the data
                timestamp and sealed as future proof for the process.
            mode (Mode, optional): What mode to use. When using identify and
                screening data enhancement is enabled for nationalities where
                data enhancement is provided.

        Returns:
            AmlResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(name=name)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/aml/b2c'
        _query_parameters = {
            'name': name,
            'ssn': ssn,
            'birthDate': birth_date,
            'nationality': nationality,
            'language': language,
            'includeReport': include_report,
            'mode': mode
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
            raise APIException('Not found', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal Server Error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AmlResponse.from_dictionary)
