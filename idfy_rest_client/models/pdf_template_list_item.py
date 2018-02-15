# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.pdf_template_list_item

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class PdfTemplateListItem(object):

    """Implementation of the 'PdfTemplateListItem' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        name (string): The name of the Pdf template
        last_edited (datetime): Timestamp when the template is last edited

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'Id',
        "name":'Name',
        "last_edited":'LastEdited'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 last_edited=None,
                 additional_properties = {}):
        """Constructor for the PdfTemplateListItem class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.last_edited = APIHelper.RFC3339DateTime(last_edited) if last_edited else None

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
        id = dictionary.get('Id')
        name = dictionary.get('Name')
        last_edited = APIHelper.RFC3339DateTime.from_value(dictionary.get("LastEdited")).datetime if dictionary.get("LastEdited") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   last_edited,
                   dictionary)


