# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.events_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.event_type_info import EventTypeInfo
from ..models.event_dto import EventDto

class EventsController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def events_get_event_types(self):
        """Does a GET request to /notification/events/types.

        Returns a list of all available event types.

        Returns:
            EventTypeInfo: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/events/types'
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
        return APIHelper.json_deserialize(_context.response.raw_body, EventTypeInfo.from_dictionary)

    def events_clear(self):
        """Does a POST request to /notification/events/clear.

        Clear all events for your account

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/events/clear'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.post(_query_url)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def events_peek(self,
                    event_type=None,
                    tags=None):
        """Does a GET request to /notification/events/peek.

        Peek top 100 unhandled events regardless if they are locked or not.
        Dont use this endpoint to handle events.

        Args:
            event_type (EventType, optional): Filter by event type
            tags (string, optional): Filter the events with your own tags that
                you added to the document when you created it (Separate tags
                with ,)

        Returns:
            list of EventDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/events/peek'
        _query_parameters = {
            'eventType': event_type,
            'tags': tags
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
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, EventDto.from_dictionary)

    def events_handle(self,
                      event_id):
        """Does a POST request to /notification/events/{eventId}.

        Mark the status of an event as handled to make sure you dont retrieve
        this event again

        Args:
            event_id (uuid|string): TODO: type description here. Example: 

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(event_id=event_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/events/{eventId}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'eventId': event_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.post(_query_url)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def events_handle_many(self,
                           event_ids):
        """Does a POST request to /notification/events.

        Mark the status of a batch of events as handled to make sure you dont
        retrieve these events again

        Args:
            event_ids (list of uuid|string): TODO: type description here.
                Example: 

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(event_ids=event_ids)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/events'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(event_ids))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def events_get(self,
                   event_type=None,
                   tags=None):
        """Does a GET request to /notification/events.

        Retrieve up to 100 unhandled events for your account. After you
        retrieve this list the
                     events will be "locked" for 10 minutes to give you time
                     to handle them. Please handle the events using one of the
                     endpoints in this API to avoid retrieving the same events
                     multiple times.

        Args:
            event_type (EventType, optional): Filter by event type
            tags (string, optional): Filter the events with your own tags that
                you added to the document when you created it (Separate tags
                with ,)

        Returns:
            list of EventDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/notification/events'
        _query_parameters = {
            'eventType': event_type,
            'tags': tags
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
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, EventDto.from_dictionary)
