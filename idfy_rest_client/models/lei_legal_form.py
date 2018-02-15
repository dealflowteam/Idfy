# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_legal_form

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class LeiLegalForm(object):

    """Implementation of the 'LeiLegalForm' model.

    TODO: type model description here.

    Attributes:
        other_legal_form (string): TODO: type description here.
        entity_legal_form_code (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "other_legal_form":'OtherLegalForm',
        "entity_legal_form_code":'EntityLegalFormCode'
    }

    def __init__(self,
                 other_legal_form=None,
                 entity_legal_form_code=None,
                 additional_properties = {}):
        """Constructor for the LeiLegalForm class"""

        # Initialize members of the class
        self.other_legal_form = other_legal_form
        self.entity_legal_form_code = entity_legal_form_code

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
        other_legal_form = dictionary.get('OtherLegalForm')
        entity_legal_form_code = dictionary.get('EntityLegalFormCode')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(other_legal_form,
                   entity_legal_form_code,
                   dictionary)


