# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.webhooks_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.webhook_delivery_dto import WebhookDeliveryDto
from ..models.webhook_dto import WebhookDto

class WebhooksController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def webhooks_get_webhook_deliveries(self,
                                        id):
        """Does a GET request to /notification/webhooks/{id}/deliveries.

        Returns the 10 most recent delivery attempts for a single webhook.

        Args:
            id (int): TODO: type description here. Example: 

        Returns:
            WebhookDeliveryDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/webhooks/{id}/deliveries'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
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
        return APIHelper.json_deserialize(_context.response.raw_body, WebhookDeliveryDto.from_dictionary)

    def webhooks_ping_webhook(self,
                              id):
        """Does a POST request to /notification/webhooks/{id}/ping.

        Triggers a ping event to be sent to the webhook.

        Args:
            id (int): TODO: type description here. Example: 

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/webhooks/{id}/ping'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.post(_query_url)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def webhooks_create_webhook(self,
                                new_webhook):
        """Does a POST request to /notification/webhooks.

        Creates a new webhook

        Args:
            new_webhook (WebhookCreateDto): TODO: type description here.
                Example: 

        Returns:
            WebhookDto: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(new_webhook=new_webhook)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/webhooks'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(new_webhook))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, WebhookDto.from_dictionary)

    def webhooks_list_webhooks(self):
        """Does a GET request to /notification/webhooks.

        Returns a list of all your webhooks.

        Returns:
            list of WebhookDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/webhooks'
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
        return APIHelper.json_deserialize(_context.response.raw_body, WebhookDto.from_dictionary)

    def webhooks_update_webhook(self,
                                id,
                                updated_webhook):
        """Does a PATCH request to /notification/webhooks/{id}.

        Updates the specifiedlast webhook with the parameters passed.
        Any parameters not provided will be left unchanged.

        Args:
            id (int): TODO: type description here. Example: 
            updated_webhook (WebhookUpdateDto): TODO: type description here.
                Example: 

        Returns:
            WebhookDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id,
                                 updated_webhook=updated_webhook)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/webhooks/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(updated_webhook))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, WebhookDto.from_dictionary)

    def webhooks_delete_webhook(self,
                                id):
        """Does a DELETE request to /notification/webhooks/{id}.

        Deletes the specified webhook.

        Args:
            id (int): TODO: type description here. Example: 

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/webhooks/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def webhooks_get_single_webhook(self,
                                    id):
        """Does a GET request to /notification/webhooks/{id}.

        Retrieves the details of a single webhook.

        Args:
            id (int): TODO: type description here. Example: 

        Returns:
            WebhookDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/webhooks/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
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
        return APIHelper.json_deserialize(_context.response.raw_body, WebhookDto.from_dictionary)
