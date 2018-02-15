# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.extra_info_signer_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.results
import idfy_rest_client.models.special_properties

class ExtraInfoSignerResponse(object):

    """Implementation of the 'ExtraInfoSignerResponse' model.

    TODO: type model description here.

    Attributes:
        results (Results): Results as a dictionary with json result. See our
            documentation for model examples.
        addon (list of Addon): Add a list of the addons you want to order,
            some of them requires specialproperties (read more in our
            documentation). (Extra costs will occur for addons (except difi
            company info))
        special_properties (SpecialProperties): Add a dictionay of special
            properties, see our documentation for more info

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "results":'results',
        "addon":'addon',
        "special_properties":'specialProperties'
    }

    def __init__(self,
                 results=None,
                 addon=None,
                 special_properties=None,
                 additional_properties = {}):
        """Constructor for the ExtraInfoSignerResponse class"""

        # Initialize members of the class
        self.results = results
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
        results = idfy_rest_client.models.results.Results.from_dictionary(dictionary.get('results')) if dictionary.get('results') else None
        addon = dictionary.get('addon')
        special_properties = idfy_rest_client.models.special_properties.SpecialProperties.from_dictionary(dictionary.get('specialProperties')) if dictionary.get('specialProperties') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(results,
                   addon,
                   special_properties,
                   dictionary)


