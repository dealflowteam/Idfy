# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.report_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..exceptions.api_exception import APIException

class ReportController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def retrive_signature_roles_report(self,
                                       report_id):
        """Does a GET request to /information/report/signroles/{reportId}.

        The pdf report will be awailable to download the first 48 hours.

        Args:
            report_id (string): The reportId returned from the Get

        Returns:
            void: Response from the API. PDF file

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(report_id=report_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/information/report/signroles/{reportId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'reportId': report_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
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
