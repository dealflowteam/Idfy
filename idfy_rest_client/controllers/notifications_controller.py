# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.notifications_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.notification_log_item import NotificationLogItem

class NotificationsController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def notifications_list(self,
                           document_id):
        """Does a GET request to /signature/documents/{documentId}/notifications.

        Returns a list of all notifications that has been sent / attempted
        sent for a document

        Args:
            document_id (uuid|string): TODO: type description here. Example: 

        Returns:
            list of NotificationLogItem: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(document_id=document_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/signature/documents/{documentId}/notifications'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'documentId': document_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, NotificationLogItem.from_dictionary)
