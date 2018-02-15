# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.styling

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Styling(object):

    """Implementation of the 'Styling' model.

    TODO: type model description here.

    Attributes:
        account_id (uuid|string): TODO: type description here.
        base_64_encoded_css_data (string): TODO: type description here.
        file_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'AccountId',
        "base_64_encoded_css_data":'Base64EncodedCssData',
        "file_name":'FileName'
    }

    def __init__(self,
                 account_id=None,
                 base_64_encoded_css_data=None,
                 file_name=None,
                 additional_properties = {}):
        """Constructor for the Styling class"""

        # Initialize members of the class
        self.account_id = account_id
        self.base_64_encoded_css_data = base_64_encoded_css_data
        self.file_name = file_name

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
        base_64_encoded_css_data = dictionary.get('Base64EncodedCssData')
        file_name = dictionary.get('FileName')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_id,
                   base_64_encoded_css_data,
                   file_name,
                   dictionary)


