# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.extra_info_document_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.special_properties

class ExtraInfoDocumentRequest(object):

    """Implementation of the 'ExtraInfoDocumentRequest' model.

    TODO: type model description here.

    Attributes:
        addon (list of Addon171): Add a list of the addons you want to order,
            some of them requires specialproperties (read more in our
            documentation). (Extra costs will occur for addons (except difi
            company info))
        special_properties (SpecialProperties): Add a dictionay of special
            properties, see our documentation for more info

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "addon":'addon',
        "special_properties":'specialProperties'
    }

    def __init__(self,
                 addon=None,
                 special_properties=None,
                 additional_properties = {}):
        """Constructor for the ExtraInfoDocumentRequest class"""

        # Initialize members of the class
        self.addon = addon
        self.special_properties = special_properties

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
        addon = dictionary.get('addon')
        special_properties = idfy_rest_client.models.special_properties.SpecialProperties.from_dictionary(dictionary.get('specialProperties')) if dictionary.get('specialProperties') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(addon,
                   special_properties,
                   dictionary)


