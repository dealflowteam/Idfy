# -*- coding: utf-8 -*-

"""
   idfy_rest_client.configuration

   This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from .api_helper import APIHelper

class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # An enum for SDK environments
    class Environment(object):
        PRODUCTION = 0

    # An enum for API servers
    class Server(object):
        DEFAULT = 0
        ACCESS_TOKEN_SERVER = 1

    # The environment in which the SDK is running
    environment = Environment.PRODUCTION

    # OAuth 2 Client ID
    o_auth_client_id = 't50406ae2701149be8d72063a4ac005d0'

    # OAuth 2 Client Secret
    o_auth_client_secret = 'b3bf4003f34acc146a8270cb991fa2afc3be4a72df2aae0b5db3067120ec23a6'

    # Object for storing information about the OAuth token
    o_auth_token = None

    # Callback to be called when OAuth token is acquired or refreshed
    o_auth_callback = None

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'https://api.idfy.io',
            Server.ACCESS_TOKEN_SERVER: 'https://api.idfy.io/oauth/connect/token',
        },
    }

    @classmethod
    def get_base_uri(cls, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the server.

        Args:
            server (Configuration.Server): The server enum for which the base URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
        }
        return APIHelper.append_url_with_template_parameters(cls.environments[cls.environment][server], parameters)
