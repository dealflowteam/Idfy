# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.person_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.person_person_information import PersonPersonInformation
from ..models.person_credit_check_person_response import PersonCreditCheckPersonResponse
from ..models.person_official_person_registry_response import PersonOfficialPersonRegistryResponse
from ..exceptions.api_exception import APIException

class PersonController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def list_person_info_through_matchit_by_query(self,
                                                  query_string):
        """Does a GET request to /information/person/info/matchit/query.

        Returns (unofficial) person information, this method returns the 5
        best matches from the query parameters served (freetext). The
        information is delievered by Matchit.

        Args:
            query_string (string): TODO: type description here. Example: 

        Returns:
            list of PersonPersonInformation: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(query_string=query_string)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/person/info/matchit/query'
        _query_parameters = {
            'queryString': query_string
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
        return APIHelper.json_deserialize(_context.response.raw_body, PersonPersonInformation.from_dictionary)

    def retrieve_person_info_through_matchit(self,
                                             name=None,
                                             social_sec=None,
                                             date_of_birth=None,
                                             phonenumber=None,
                                             address=None):
        """Does a GET request to /information/person/info/matchit.

        Returns (unofficial) person information, this method returns the best
        match from the query parameters served. The information is delievered
        by Matchit. 
        Valid query parameter combinations: name + dateOfBirth, name +
        socialSec, name + address, phonenumber

        Args:
            name (string, optional): TODO: type description here. Example: 
            social_sec (string, optional): TODO: type description here.
                Example: 
            date_of_birth (string, optional): TODO: type description here.
                Example: 
            phonenumber (string, optional): TODO: type description here.
                Example: 
            address (string, optional): TODO: type description here. Example:
                
        Returns:
            PersonPersonInformation: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/person/info/matchit'
        _query_parameters = {
            'name': name,
            'socialSec': social_sec,
            'dateOfBirth': date_of_birth,
            'phonenumber': phonenumber,
            'address': address
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
        return APIHelper.json_deserialize(_context.response.raw_body, PersonPersonInformation.from_dictionary)

    def run_credit_check(self,
                         social_security_number,
                         user_id=None,
                         password=None,
                         phonenumber=None,
                         email=None,
                         include_report=None):
        """Does a GET request to /information/person/creditcheck.

        Credit check of a single person. The use of this will produce a
        duplicate letter to the person that is checked.
                     A pdf report will be awailable to download the first 48
                     hours.

        Args:
            social_security_number (long|int): TODO: type description here.
                Example: 
            user_id (string, optional): Override bisnode user Id
            password (string, optional): Override bisnode password
            phonenumber (int, optional): Specify this to use electronic
                duplicate letters
            email (string, optional): Specify this to use electronic duplicate
                letters
            include_report (bool, optional): Specify if you want a pdf report
                (defaults to false)

        Returns:
            PersonCreditCheckPersonResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(social_security_number=social_security_number)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/person/creditcheck'
        _query_parameters = {
            'socialSecurityNumber': social_security_number,
            'userId': user_id,
            'password': password,
            'phonenumber': phonenumber,
            'email': email,
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
        return APIHelper.json_deserialize(_context.response.raw_body, PersonCreditCheckPersonResponse.from_dictionary)

    def retrieve_person_info_through_infotorget(self,
                                                username,
                                                password,
                                                reason,
                                                system,
                                                social_security_number=None,
                                                firstname=None,
                                                lastname=None,
                                                dateofbirth=None,
                                                address=None,
                                                postalcode=None):
        """Does a GET request to /information/person/info/infotorget.

        Run a query using social security number as parameter. The use of this
        requires username and password for Infortorget with the required
        permissions.
        Valid query parameter combinations: 
        socialSecurityNumber, 
        socialSecurityNumber + firstName + lastName, 
        dateOfBirth + firstName + lastName, 
        firstName + lastName + address + postalCode

        Args:
            username (string): Infotorget username
            password (string): Infotorget password
            reason (string): Reason for request
            system (string): Your system name (Cannot contain any special
                characters or numbers)
            social_security_number (string, optional): TODO: type description
                here. Example: 
            firstname (string, optional): TODO: type description here.
                Example: 
            lastname (string, optional): TODO: type description here. Example:
                            dateofbirth (int, optional): TODO: type description here. Example:
                            address (string, optional): TODO: type description here. Example:
                            postalcode (string, optional): TODO: type description here.
                Example: 

        Returns:
            PersonOfficialPersonRegistryResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(username=username,
                                 password=password,
                                 reason=reason,
                                 system=system)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/person/info/infotorget'
        _query_parameters = {
            'username': username,
            'password': password,
            'reason': reason,
            'system': system,
            'socialSecurityNumber': social_security_number,
            'firstname': firstname,
            'lastname': lastname,
            'dateofbirth': dateofbirth,
            'address': address,
            'postalcode': postalcode
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
        return APIHelper.json_deserialize(_context.response.raw_body, PersonOfficialPersonRegistryResponse.from_dictionary)
