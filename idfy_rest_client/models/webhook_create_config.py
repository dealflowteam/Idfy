# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.webhook_create_config

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class WebhookCreateConfig(object):

    """Implementation of the 'WebhookCreateConfig' model.

    TODO: type model description here.

    Attributes:
        url (string): The URL to which the payloads will be delivered.
        secret (string): Optional secret used to compute a HMAC hex digest of
            the payload,   which is passed with the HTTP request as an
            ``X-Idfy-Signature`` header.
        delivery_logging (DeliveryLogging): Determines whether to log webhook
            delivery attempts. Defaults to `never`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url',
        "secret":'secret',
        "delivery_logging":'deliveryLogging'
    }

    def __init__(self,
                 url=None,
                 secret=None,
                 delivery_logging=None,
                 additional_properties = {}):
        """Constructor for the WebhookCreateConfig class"""

        # Initialize members of the class
        self.url = url
        self.secret = secret
        self.delivery_logging = delivery_logging

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
        url = dictionary.get('url')
        secret = dictionary.get('secret')
        delivery_logging = dictionary.get('deliveryLogging')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(url,
                   secret,
                   delivery_logging,
                   dictionary)


