# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.dialogs

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.dialog_before
import idfy_rest_client.models.dialog

class Dialogs(object):

    """Implementation of the 'Dialogs' model.

    TODO: type model description here.

    Attributes:
        before (DialogBefore): Will be presented before the document is
            signed
        after (Dialog): Will be presented after the document is signed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before":'before',
        "after":'after'
    }

    def __init__(self,
                 before=None,
                 after=None,
                 additional_properties = {}):
        """Constructor for the Dialogs class"""

        # Initialize members of the class
        self.before = before
        self.after = after

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
        before = idfy_rest_client.models.dialog_before.DialogBefore.from_dictionary(dictionary.get('before')) if dictionary.get('before') else None
        after = idfy_rest_client.models.dialog.Dialog.from_dictionary(dictionary.get('after')) if dictionary.get('after') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(before,
                   after,
                   dictionary)


