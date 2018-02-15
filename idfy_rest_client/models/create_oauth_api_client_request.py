# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.create_oauth_api_client_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.oauth_secret

class CreateOauthAPIClientRequest(object):

    """Implementation of the 'CreateOauthAPIClientRequest' model.

    TODO: type model description here.

    Attributes:
        account_id (uuid|string): TODO: type description here.
        client_name (string): TODO: type description here.
        client_secrets (list of OauthSecret): TODO: type description here.
        allowed_scopes (list of string): TODO: type description here.
        identity_token_lifetime (int): Lifetime of identity token in seconds
            (defaults to 300 seconds / 5 minutes)
        access_token_lifetime (int): Lifetime of access token in seconds
            (defaults to 3600 seconds / 1 hour)
        absolute_refresh_token_lifetime (int): Maximum lifetime of a refresh
            token in seconds. Defaults to 2592000 seconds / 30 days
        sliding_refresh_token_lifetime (int): Sliding lifetime of a refresh
            token in seconds. Defaults to 1296000 seconds / 15 days
        refresh_token_usage (RefreshTokenUsage): TODO: type description here.
        update_access_token_claims_on_refresh (bool): Gets or sets a value
            indicating whether the access token (and its claims) should be
            updated on a refresh token request.
        refresh_token_expiration (RefreshTokenExpiration): TODO: type
            description here.
        access_token_type (AccessTokenType): TODO: type description here.
        always_send_client_claims (bool): Gets or sets a value indicating
            whether client claims should be always included in the access
            tokens - or only for client credentials flow.
        allowed_cors_origins (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'AccountId',
        "client_name":'ClientName',
        "client_secrets":'ClientSecrets',
        "allowed_scopes":'AllowedScopes',
        "identity_token_lifetime":'IdentityTokenLifetime',
        "access_token_lifetime":'AccessTokenLifetime',
        "absolute_refresh_token_lifetime":'AbsoluteRefreshTokenLifetime',
        "sliding_refresh_token_lifetime":'SlidingRefreshTokenLifetime',
        "refresh_token_usage":'RefreshTokenUsage',
        "update_access_token_claims_on_refresh":'UpdateAccessTokenClaimsOnRefresh',
        "refresh_token_expiration":'RefreshTokenExpiration',
        "access_token_type":'AccessTokenType',
        "always_send_client_claims":'AlwaysSendClientClaims',
        "allowed_cors_origins":'AllowedCorsOrigins'
    }

    def __init__(self,
                 account_id=None,
                 client_name=None,
                 client_secrets=None,
                 allowed_scopes=None,
                 identity_token_lifetime=None,
                 access_token_lifetime=None,
                 absolute_refresh_token_lifetime=None,
                 sliding_refresh_token_lifetime=None,
                 refresh_token_usage=None,
                 update_access_token_claims_on_refresh=None,
                 refresh_token_expiration=None,
                 access_token_type=None,
                 always_send_client_claims=None,
                 allowed_cors_origins=None,
                 additional_properties = {}):
        """Constructor for the CreateOauthAPIClientRequest class"""

        # Initialize members of the class
        self.account_id = account_id
        self.client_name = client_name
        self.client_secrets = client_secrets
        self.allowed_scopes = allowed_scopes
        self.identity_token_lifetime = identity_token_lifetime
        self.access_token_lifetime = access_token_lifetime
        self.absolute_refresh_token_lifetime = absolute_refresh_token_lifetime
        self.sliding_refresh_token_lifetime = sliding_refresh_token_lifetime
        self.refresh_token_usage = refresh_token_usage
        self.update_access_token_claims_on_refresh = update_access_token_claims_on_refresh
        self.refresh_token_expiration = refresh_token_expiration
        self.access_token_type = access_token_type
        self.always_send_client_claims = always_send_client_claims
        self.allowed_cors_origins = allowed_cors_origins

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
        account_id = dictionary.get('AccountId')
        client_name = dictionary.get('ClientName')
        client_secrets = None
        if dictionary.get('ClientSecrets') != None:
            client_secrets = list()
            for structure in dictionary.get('ClientSecrets'):
                client_secrets.append(idfy_rest_client.models.oauth_secret.OauthSecret.from_dictionary(structure))
        allowed_scopes = dictionary.get('AllowedScopes')
        identity_token_lifetime = dictionary.get('IdentityTokenLifetime')
        access_token_lifetime = dictionary.get('AccessTokenLifetime')
        absolute_refresh_token_lifetime = dictionary.get('AbsoluteRefreshTokenLifetime')
        sliding_refresh_token_lifetime = dictionary.get('SlidingRefreshTokenLifetime')
        refresh_token_usage = dictionary.get('RefreshTokenUsage')
        update_access_token_claims_on_refresh = dictionary.get('UpdateAccessTokenClaimsOnRefresh')
        refresh_token_expiration = dictionary.get('RefreshTokenExpiration')
        access_token_type = dictionary.get('AccessTokenType')
        always_send_client_claims = dictionary.get('AlwaysSendClientClaims')
        allowed_cors_origins = dictionary.get('AllowedCorsOrigins')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_id,
                   client_name,
                   client_secrets,
                   allowed_scopes,
                   identity_token_lifetime,
                   access_token_lifetime,
                   absolute_refresh_token_lifetime,
                   sliding_refresh_token_lifetime,
                   refresh_token_usage,
                   update_access_token_claims_on_refresh,
                   refresh_token_expiration,
                   access_token_type,
                   always_send_client_claims,
                   allowed_cors_origins,
                   dictionary)


