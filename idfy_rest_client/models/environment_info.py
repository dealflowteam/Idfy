# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.environment_info

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class EnvironmentInfo(object):

    """Implementation of the 'EnvironmentInfo' model.

    Information aboute users enviroment

    Attributes:
        user_agent (string): The users user-agent (browser/device)
        ip_address (string): The IP-address of the user

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_agent":'UserAgent',
        "ip_address":'IPAddress'
    }

    def __init__(self,
                 user_agent=None,
                 ip_address=None,
                 additional_properties = {}):
        """Constructor for the EnvironmentInfo class"""

        # Initialize members of the class
        self.user_agent = user_agent
        self.ip_address = ip_address

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
        user_agent = dictionary.get('UserAgent')
        ip_address = dictionary.get('IPAddress')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(user_agent,
                   ip_address,
                   dictionary)


