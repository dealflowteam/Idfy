# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.oauth_secret

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class OauthSecret(object):

    """Implementation of the 'OauthSecret' model.

    TODO: type model description here.

    Attributes:
        description (string): TODO: type description here.
        value (string): TODO: type description here.
        expiration (datetime): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'Description',
        "value":'Value',
        "expiration":'Expiration',
        "mtype":'Type'
    }

    def __init__(self,
                 description=None,
                 value=None,
                 expiration=None,
                 mtype=None,
                 additional_properties = {}):
        """Constructor for the OauthSecret class"""

        # Initialize members of the class
        self.description = description
        self.value = value
        self.expiration = APIHelper.RFC3339DateTime(expiration) if expiration else None
        self.mtype = mtype

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
        description = dictionary.get('Description')
        value = dictionary.get('Value')
        expiration = APIHelper.RFC3339DateTime.from_value(dictionary.get("Expiration")).datetime if dictionary.get("Expiration") else None
        mtype = dictionary.get('Type')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(description,
                   value,
                   expiration,
                   mtype,
                   dictionary)


