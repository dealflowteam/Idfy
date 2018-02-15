# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.webhook_dto

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.webhook_config
import idfy_rest_client.models.webhook_response

class WebhookDto(object):

    """Implementation of the 'WebhookDto' model.

    TODO: type model description here.

    Attributes:
        id (int): The webhooks unique identifier.
        name (string): Display name of the webhook.
        active (bool): Determines if the webhook is active.
        events (list of string): A list of events that the webhook triggers
            for.
        config (WebhookConfig): TODO: type description here.
        created_at (datetime): Time at which the webhook was created.
        updated_at (datetime): Time at which the webhook was last updated.
        last_response (WebhookResponse): TODO: type description here.
        tags (list of string): A list of event tags that the webhook triggers
            for.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "active":'active',
        "events":'events',
        "config":'config',
        "created_at":'createdAt',
        "updated_at":'updatedAt',
        "last_response":'lastResponse',
        "tags":'tags'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 active=None,
                 events=None,
                 config=None,
                 created_at=None,
                 updated_at=None,
                 last_response=None,
                 tags=None,
                 additional_properties = {}):
        """Constructor for the WebhookDto class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.active = active
        self.events = events
        self.config = config
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.last_response = last_response
        self.tags = tags

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
        name = dictionary.get('name')
        active = dictionary.get('active')
        events = dictionary.get('events')
        config = idfy_rest_client.models.webhook_config.WebhookConfig.from_dictionary(dictionary.get('config')) if dictionary.get('config') else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdAt")).datetime if dictionary.get("createdAt") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updatedAt")).datetime if dictionary.get("updatedAt") else None
        last_response = idfy_rest_client.models.webhook_response.WebhookResponse.from_dictionary(dictionary.get('lastResponse')) if dictionary.get('lastResponse') else None
        tags = dictionary.get('tags')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   active,
                   events,
                   config,
                   created_at,
                   updated_at,
                   last_response,
                   tags,
                   dictionary)


