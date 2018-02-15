# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.webhook_create_dto

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.webhook_create_config

class WebhookCreateDto(object):

    """Implementation of the 'WebhookCreateDto' model.

    TODO: type model description here.

    Attributes:
        name (string): Display name of the webhook.
        active (bool): Determines whether the webhook is active or not.
        events (list of string): A list of events that the webhook triggers
            for.
        config (WebhookCreateConfig): TODO: type description here.
        tags (list of string): An optional list of event tags that the webhook
            triggers for.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "active":'active',
        "events":'events',
        "config":'config',
        "tags":'tags'
    }

    def __init__(self,
                 name=None,
                 active=None,
                 events=None,
                 config=None,
                 tags=None,
                 additional_properties = {}):
        """Constructor for the WebhookCreateDto class"""

        # Initialize members of the class
        self.name = name
        self.active = active
        self.events = events
        self.config = config
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
        name = dictionary.get('name')
        active = dictionary.get('active')
        events = dictionary.get('events')
        config = idfy_rest_client.models.webhook_create_config.WebhookCreateConfig.from_dictionary(dictionary.get('config')) if dictionary.get('config') else None
        tags = dictionary.get('tags')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   active,
                   events,
                   config,
                   tags,
                   dictionary)


