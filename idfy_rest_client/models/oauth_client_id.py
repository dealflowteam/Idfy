# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.oauth_client_id

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class OauthClientId(object):

    """Implementation of the 'OauthClientId' model.

    TODO: type model description here.

    Attributes:
        client_id (string): TODO: type description here.
        account_id (uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_id":'ClientId',
        "account_id":'AccountId'
    }

    def __init__(self,
                 client_id=None,
                 account_id=None,
                 additional_properties = {}):
        """Constructor for the OauthClientId class"""

        # Initialize members of the class
        self.client_id = client_id
        self.account_id = account_id

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
        account_id = dictionary.get('AccountId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(client_id,
                   account_id,
                   dictionary)


