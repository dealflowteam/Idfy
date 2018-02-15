# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.oauth_client_list_item_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class OauthClientListItemResponse(object):

    """Implementation of the 'OauthClientListItemResponse' model.

    TODO: type model description here.

    Attributes:
        client_id (string): TODO: type description here.
        enabled (bool): TODO: type description here.
        client_name (string): TODO: type description here.
        account_id (uuid|string): TODO: type description here.
        created (datetime): TODO: type description here.
        last_changed (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_id":'ClientId',
        "enabled":'Enabled',
        "client_name":'ClientName',
        "account_id":'AccountId',
        "created":'Created',
        "last_changed":'LastChanged'
    }

    def __init__(self,
                 client_id=None,
                 enabled=None,
                 client_name=None,
                 account_id=None,
                 created=None,
                 last_changed=None,
                 additional_properties = {}):
        """Constructor for the OauthClientListItemResponse class"""

        # Initialize members of the class
        self.client_id = client_id
        self.enabled = enabled
        self.client_name = client_name
        self.account_id = account_id
        self.created = APIHelper.RFC3339DateTime(created) if created else None
        self.last_changed = APIHelper.RFC3339DateTime(last_changed) if last_changed else None

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
        client_id = dictionary.get('ClientId')
        enabled = dictionary.get('Enabled')
        client_name = dictionary.get('ClientName')
        account_id = dictionary.get('AccountId')
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("Created")).datetime if dictionary.get("Created") else None
        last_changed = APIHelper.RFC3339DateTime.from_value(dictionary.get("LastChanged")).datetime if dictionary.get("LastChanged") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(client_id,
                   enabled,
                   client_name,
                   account_id,
                   created,
                   last_changed,
                   dictionary)


