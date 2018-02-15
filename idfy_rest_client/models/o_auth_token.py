# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.o_auth_token

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class OAuthToken(object):

    """Implementation of the 'OAuthToken' model.

    OAuth 2 Authorization endpoint response

    Attributes:
        access_token (string): Access token
        token_type (string): Type of access token
        expires_in (long|int): Time in seconds before the access token
            expires
        scope (string): List of scopes granted This is a space-delimited list
            of strings.
        expiry (long|int): Time of token expiry as unix timestamp (UTC)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_token":'access_token',
        "token_type":'token_type',
        "expires_in":'expires_in',
        "scope":'scope',
        "expiry":'expiry'
    }

    def __init__(self,
                 access_token=None,
                 token_type=None,
                 expires_in=None,
                 scope=None,
                 expiry=None,
                 additional_properties = {}):
        """Constructor for the OAuthToken class"""

        # Initialize members of the class
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.scope = scope
        self.expiry = expiry

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
        access_token = dictionary.get('access_token')
        token_type = dictionary.get('token_type')
        expires_in = dictionary.get('expires_in')
        scope = dictionary.get('scope')
        expiry = dictionary.get('expiry')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(access_token,
                   token_type,
                   expires_in,
                   scope,
                   expiry,
                   dictionary)


