# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.webhook_delivery_dto

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class WebhookDeliveryDto(object):

    """Implementation of the 'WebhookDeliveryDto' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): The webhooks unique identifier.
        webhook_id (int): TODO: type description here.
        event_id (uuid|string): TODO: type description here.
        timestamp (datetime): TODO: type description here.
        url (string): TODO: type description here.
        elapsed_ms (long|int): TODO: type description here.
        request_headers (object): TODO: type description here.
        request_body (object): TODO: type description here.
        response_headers (object): TODO: type description here.
        response_body (object): TODO: type description here.
        response_status_code (int): TODO: type description here.
        response_message (string): TODO: type description here.
        error_message (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "webhook_id":'webhookId',
        "event_id":'eventId',
        "timestamp":'timestamp',
        "url":'url',
        "elapsed_ms":'elapsedMs',
        "request_headers":'requestHeaders',
        "request_body":'requestBody',
        "response_headers":'responseHeaders',
        "response_body":'responseBody',
        "response_status_code":'responseStatusCode',
        "response_message":'responseMessage',
        "error_message":'errorMessage'
    }

    def __init__(self,
                 id=None,
                 webhook_id=None,
                 event_id=None,
                 timestamp=None,
                 url=None,
                 elapsed_ms=None,
                 request_headers=None,
                 request_body=None,
                 response_headers=None,
                 response_body=None,
                 response_status_code=None,
                 response_message=None,
                 error_message=None,
                 additional_properties = {}):
        """Constructor for the WebhookDeliveryDto class"""

        # Initialize members of the class
        self.id = id
        self.webhook_id = webhook_id
        self.event_id = event_id
        self.timestamp = APIHelper.RFC3339DateTime(timestamp) if timestamp else None
        self.url = url
        self.elapsed_ms = elapsed_ms
        self.request_headers = request_headers
        self.request_body = request_body
        self.response_headers = response_headers
        self.response_body = response_body
        self.response_status_code = response_status_code
        self.response_message = response_message
        self.error_message = error_message

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        webhook_id = dictionary.get('webhookId')
        event_id = dictionary.get('eventId')
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None
        url = dictionary.get('url')
        elapsed_ms = dictionary.get('elapsedMs')
        request_headers = dictionary.get('requestHeaders')
        request_body = dictionary.get('requestBody')
        response_headers = dictionary.get('responseHeaders')
        response_body = dictionary.get('responseBody')
        response_status_code = dictionary.get('responseStatusCode')
        response_message = dictionary.get('responseMessage')
        error_message = dictionary.get('errorMessage')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   webhook_id,
                   event_id,
                   timestamp,
                   url,
                   elapsed_ms,
                   request_headers,
                   request_body,
                   response_headers,
                   response_body,
                   response_status_code,
                   response_message,
                   error_message,
                   dictionary)


