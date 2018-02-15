# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.security

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Security(object):

    """Implementation of the 'Security' model.

    TODO: type model description here.

    Attributes:
        one_time_use (bool): (Coming soon) The link can only be used one time
        ip_white_list (list of string): (Coming soon) Define a list of IP's
            that are allowed to see / sign the document

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "one_time_use":'oneTimeUse',
        "ip_white_list":'ipWhiteList'
    }

    def __init__(self,
                 one_time_use=None,
                 ip_white_list=None,
                 additional_properties = {}):
        """Constructor for the Security class"""

        # Initialize members of the class
        self.one_time_use = one_time_use
        self.ip_white_list = ip_white_list

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
        one_time_use = dictionary.get('oneTimeUse')
        ip_white_list = dictionary.get('ipWhiteList')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(one_time_use,
                   ip_white_list,
                   dictionary)


