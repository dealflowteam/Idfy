# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.update_open_id_client_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class UpdateOpenIdClientRequest(object):

    """Implementation of the 'UpdateOpenIdClientRequest' model.

    TODO: type model description here.

    Attributes:
        account_id (uuid|string): TODO: type description here.
        client_id (string): TODO: type description here.
        client_name (string): TODO: type description here.
        redirect_uris (list of string): TODO: type description here.
        enabled (bool): TODO: type description here.
        client_uri (string): TODO: type description here.
        require_consent (bool): TODO: type description here.
        allow_remember_consent (bool): TODO: type description here.
        flow (Flow): TODO: type description here.
        allow_client_credentials_only (bool): TODO: type description here.
        post_logout_redirect_uris (list of string): TODO: type description
            here.
        logout_uri (string): Specifies logout URI at client for HTTP based
            logout.
        require_sign_out_prompt (bool): Specifies if the client will always
            show a confirmation page for sign-out. Defaults to false.
        allowed_scopes (list of string): TODO: type description here.
        identity_provider_restrictions (list of IdentityProviderRestriction):
            Setup which id providers that should be allowed to use
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
        include_jwt_id (bool): Gets or sets a value indicating whether JWT
            access tokens should include an identifier
        always_send_client_claims (bool): Gets or sets a value indicating
            whether client claims should be always included in the access
            tokens - or only for client credentials flow.
        allowed_cors_origins (list of string): TODO: type description here.
        allow_access_tokens_via_browser (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'AccountId',
        "client_id":'ClientId',
        "client_name":'ClientName',
        "redirect_uris":'RedirectUris',
        "enabled":'Enabled',
        "client_uri":'ClientUri',
        "require_consent":'RequireConsent',
        "allow_remember_consent":'AllowRememberConsent',
        "flow":'Flow',
        "allow_client_credentials_only":'AllowClientCredentialsOnly',
        "post_logout_redirect_uris":'PostLogoutRedirectUris',
        "logout_uri":'LogoutUri',
        "require_sign_out_prompt":'RequireSignOutPrompt',
        "allowed_scopes":'AllowedScopes',
        "identity_provider_restrictions":'IdentityProviderRestrictions',
        "identity_token_lifetime":'IdentityTokenLifetime',
        "access_token_lifetime":'AccessTokenLifetime',
        "absolute_refresh_token_lifetime":'AbsoluteRefreshTokenLifetime',
        "sliding_refresh_token_lifetime":'SlidingRefreshTokenLifetime',
        "refresh_token_usage":'RefreshTokenUsage',
        "update_access_token_claims_on_refresh":'UpdateAccessTokenClaimsOnRefresh',
        "refresh_token_expiration":'RefreshTokenExpiration',
        "access_token_type":'AccessTokenType',
        "include_jwt_id":'IncludeJwtId',
        "always_send_client_claims":'AlwaysSendClientClaims',
        "allowed_cors_origins":'AllowedCorsOrigins',
        "allow_access_tokens_via_browser":'AllowAccessTokensViaBrowser'
    }

    def __init__(self,
                 account_id=None,
                 client_id=None,
                 client_name=None,
                 redirect_uris=None,
                 enabled=None,
                 client_uri=None,
                 require_consent=None,
                 allow_remember_consent=None,
                 flow=None,
                 allow_client_credentials_only=None,
                 post_logout_redirect_uris=None,
                 logout_uri=None,
                 require_sign_out_prompt=None,
                 allowed_scopes=None,
                 identity_provider_restrictions=None,
                 identity_token_lifetime=None,
                 access_token_lifetime=None,
                 absolute_refresh_token_lifetime=None,
                 sliding_refresh_token_lifetime=None,
                 refresh_token_usage=None,
                 update_access_token_claims_on_refresh=None,
                 refresh_token_expiration=None,
                 access_token_type=None,
                 include_jwt_id=None,
                 always_send_client_claims=None,
                 allowed_cors_origins=None,
                 allow_access_tokens_via_browser=None,
                 additional_properties = {}):
        """Constructor for the UpdateOpenIdClientRequest class"""

        # Initialize members of the class
        self.account_id = account_id
        self.client_id = client_id
        self.client_name = client_name
        self.redirect_uris = redirect_uris
        self.enabled = enabled
        self.client_uri = client_uri
        self.require_consent = require_consent
        self.allow_remember_consent = allow_remember_consent
        self.flow = flow
        self.allow_client_credentials_only = allow_client_credentials_only
        self.post_logout_redirect_uris = post_logout_redirect_uris
        self.logout_uri = logout_uri
        self.require_sign_out_prompt = require_sign_out_prompt
        self.allowed_scopes = allowed_scopes
        self.identity_provider_restrictions = identity_provider_restrictions
        self.identity_token_lifetime = identity_token_lifetime
        self.access_token_lifetime = access_token_lifetime
        self.absolute_refresh_token_lifetime = absolute_refresh_token_lifetime
        self.sliding_refresh_token_lifetime = sliding_refresh_token_lifetime
        self.refresh_token_usage = refresh_token_usage
        self.update_access_token_claims_on_refresh = update_access_token_claims_on_refresh
        self.refresh_token_expiration = refresh_token_expiration
        self.access_token_type = access_token_type
        self.include_jwt_id = include_jwt_id
        self.always_send_client_claims = always_send_client_claims
        self.allowed_cors_origins = allowed_cors_origins
        self.allow_access_tokens_via_browser = allow_access_tokens_via_browser

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
        client_id = dictionary.get('ClientId')
        client_name = dictionary.get('ClientName')
        redirect_uris = dictionary.get('RedirectUris')
        enabled = dictionary.get('Enabled')
        client_uri = dictionary.get('ClientUri')
        require_consent = dictionary.get('RequireConsent')
        allow_remember_consent = dictionary.get('AllowRememberConsent')
        flow = dictionary.get('Flow')
        allow_client_credentials_only = dictionary.get('AllowClientCredentialsOnly')
        post_logout_redirect_uris = dictionary.get('PostLogoutRedirectUris')
        logout_uri = dictionary.get('LogoutUri')
        require_sign_out_prompt = dictionary.get('RequireSignOutPrompt')
        allowed_scopes = dictionary.get('AllowedScopes')
        identity_provider_restrictions = dictionary.get('IdentityProviderRestrictions')
        identity_token_lifetime = dictionary.get('IdentityTokenLifetime')
        access_token_lifetime = dictionary.get('AccessTokenLifetime')
        absolute_refresh_token_lifetime = dictionary.get('AbsoluteRefreshTokenLifetime')
        sliding_refresh_token_lifetime = dictionary.get('SlidingRefreshTokenLifetime')
        refresh_token_usage = dictionary.get('RefreshTokenUsage')
        update_access_token_claims_on_refresh = dictionary.get('UpdateAccessTokenClaimsOnRefresh')
        refresh_token_expiration = dictionary.get('RefreshTokenExpiration')
        access_token_type = dictionary.get('AccessTokenType')
        include_jwt_id = dictionary.get('IncludeJwtId')
        always_send_client_claims = dictionary.get('AlwaysSendClientClaims')
        allowed_cors_origins = dictionary.get('AllowedCorsOrigins')
        allow_access_tokens_via_browser = dictionary.get('AllowAccessTokensViaBrowser')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_id,
                   client_id,
                   client_name,
                   redirect_uris,
                   enabled,
                   client_uri,
                   require_consent,
                   allow_remember_consent,
                   flow,
                   allow_client_credentials_only,
                   post_logout_redirect_uris,
                   logout_uri,
                   require_sign_out_prompt,
                   allowed_scopes,
                   identity_provider_restrictions,
                   identity_token_lifetime,
                   access_token_lifetime,
                   absolute_refresh_token_lifetime,
                   sliding_refresh_token_lifetime,
                   refresh_token_usage,
                   update_access_token_claims_on_refresh,
                   refresh_token_expiration,
                   access_token_type,
                   include_jwt_id,
                   always_send_client_claims,
                   allowed_cors_origins,
                   allow_access_tokens_via_browser,
                   dictionary)


