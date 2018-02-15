# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.mobile_info_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2

class MobileInfoController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def mobile_info(self,
                    response_mode):
        """Does a POST request to /information/mobileinfo/authorize.

        With this enpoints a user can fill out a form with one click. Per now
        the user have to be a telenor customer to retrieve information from
        this endpoint.
                   The url received here can be used in an iframe or a
                   popupwindow, we will then deliever the user information
                   with webmessageing.
                   <br /><br />
                   Flow:<br />
                   1) Get url from this endpoint<br />
                   2) Open a popup window or an iframe with this url as src<br
                   />
                   3) User authenticates and gives you permission to retrieve
                   user information<br />
                   4) User is redirected to the callback endpoint, we connect
                   to the serviceprovider API and retrieves the information
                   about the user<br />
                   5) We use webmessaging so you can collect the information

        Args:
            response_mode (ResponseMode): TODO: type description here.
                Example: 

        Returns:
            string: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(response_mode=response_mode)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/mobileinfo/authorize'
        _query_parameters = {
            'serviceProvider': 'telenor',
            'responseMode': response_mode
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.post(_query_url)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
