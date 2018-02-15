# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.notifications

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.setup

class Notifications(object):

    """Implementation of the 'Notifications' model.

    TODO: type model description here.

    Attributes:
        setup (Setup): Setup what kind of notifications this signer should
            get. Defaults to off
        merge_fields (dict<object, string>): If you create your own
            notifications texts (See the root object -&gt; Notification), you
            can create your own merge fields with your own keys.   You can
            then specify the text you want to insert in these fields per
            signer in this dictionary. Set the dictionary key to the same
            value as the merge field value in your notification text, and the
            value to the text you want us to merge in.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "setup":'setup',
        "merge_fields":'mergeFields'
    }

    def __init__(self,
                 setup=None,
                 merge_fields=None,
                 additional_properties = {}):
        """Constructor for the Notifications class"""

        # Initialize members of the class
        self.setup = setup
        self.merge_fields = merge_fields

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
        setup = idfy_rest_client.models.setup.Setup.from_dictionary(dictionary.get('setup')) if dictionary.get('setup') else None
        merge_fields = dictionary.get('mergeFields')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(setup,
                   merge_fields,
                   dictionary)


