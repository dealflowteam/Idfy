# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.business_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.company_information_response import CompanyInformationResponse
from ..models.difi_response import DifiResponse
from ..models.credit_check_company_response import CreditCheckCompanyResponse
from ..exceptions.api_exception import APIException

class BusinessController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def retrieve_information_from_matchit(self,
                                          companyname=None,
                                          orgnumber=None):
        """Does a GET request to /information/business/info/matchit.

        Query company information from Matchit, Matchit uses existing
        information to build up their database. Supports query by name and/or
        orgnumber

        Args:
            companyname (string, optional): query param
            orgnumber (string, optional): query param

        Returns:
            CompanyInformationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/business/info/matchit'
        _query_parameters = {
            'companyname': companyname,
            'orgnumber': orgnumber
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
        return APIHelper.json_deserialize(_context.response.raw_body, CompanyInformationResponse.from_dictionary)

    def retrieve_information_from_difi(self,
                                       orgnumber=None,
                                       companyname=None):
        """Does a GET request to /information/business/info/difi.

        Query company information from difi datahotell (official data from
        bronnoysund), supports query by name and/or orgnumber

        Args:
            orgnumber (string, optional): TODO: type description here.
                Example: 
            companyname (string, optional): TODO: type description here.
                Example: 

        Returns:
            DifiResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/business/info/difi'
        _query_parameters = {
            'orgnumber': orgnumber,
            'companyname': companyname
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
        elif _context.response.status_code == 404:
            raise APIException('Not found', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal Server Error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, DifiResponse.from_dictionary)

    def perform_credit_check(self,
                             orgnumber,
                             user_id=None,
                             password=None,
                             country_code=None,
                             include_report=None):
        """Does a GET request to /information/business/creditcheck.

        Run a credit check on a specified company, this check will not produce
        any duplicate letters.
                     A pdf report will be awailable to download the first 48
                     hours.

        Args:
            orgnumber (int): TODO: type description here. Example: 
            user_id (string, optional): Override bisnode user Id
            password (string, optional): Override bisnode password
            country_code (string, optional): Default = "NO"
            include_report (bool, optional): Specify if you want a pdf report
                (defaults to false)

        Returns:
            CreditCheckCompanyResponse: Response from the API. OK

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
        _query_builder += '/information/business/creditcheck'
        _query_parameters = {
            'orgnumber': orgnumber,
            'userId': user_id,
            'password': password,
            'countryCode': country_code,
            'includeReport': include_report
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
        elif _context.response.status_code == 500:
            raise APIException('Internal server error (Miscellaneous)', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CreditCheckCompanyResponse.from_dictionary)
