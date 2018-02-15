# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.account_name_item

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class AccountNameItem(object):

    """Implementation of the 'AccountNameItem' model.

    TODO: type model description here.

    Attributes:
        account_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'AccountId',
        "name":'Name',
        "enabled":'Enabled'
    }

    def __init__(self,
                 account_id=None,
                 name=None,
                 enabled=None,
                 additional_properties = {}):
        """Constructor for the AccountNameItem class"""

        # Initialize members of the class
        self.account_id = account_id
        self.name = name
        self.enabled = enabled

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
        name = dictionary.get('Name')
        enabled = dictionary.get('Enabled')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_id,
                   name,
                   enabled,
                   dictionary)


