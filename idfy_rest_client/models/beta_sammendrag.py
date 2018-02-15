# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.beta_sammendrag

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class BetaSammendrag(object):

    """Implementation of the 'BetaSammendrag' model.

    TODO: type model description here.

    Attributes:
        antall_inkasso_field (int): TODO: type description here.
        ajour_dato_inkasso_field (datetime): TODO: type description here.
        antall_panter_losore_field (int): TODO: type description here.
        ajour_dato_losore_field (datetime): TODO: type description here.
        antall_panter_eiendom_field (int): TODO: type description here.
        ajour_dato_eiendom_field (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "antall_inkasso_field":'antallInkassoField',
        "ajour_dato_inkasso_field":'ajourDatoInkassoField',
        "antall_panter_losore_field":'antallPanterLosoreField',
        "ajour_dato_losore_field":'ajourDatoLosoreField',
        "antall_panter_eiendom_field":'antallPanterEiendomField',
        "ajour_dato_eiendom_field":'ajourDatoEiendomField'
    }

    def __init__(self,
                 antall_inkasso_field=None,
                 ajour_dato_inkasso_field=None,
                 antall_panter_losore_field=None,
                 ajour_dato_losore_field=None,
                 antall_panter_eiendom_field=None,
                 ajour_dato_eiendom_field=None,
                 additional_properties = {}):
        """Constructor for the BetaSammendrag class"""

        # Initialize members of the class
        self.antall_inkasso_field = antall_inkasso_field
        self.ajour_dato_inkasso_field = APIHelper.RFC3339DateTime(ajour_dato_inkasso_field) if ajour_dato_inkasso_field else None
        self.antall_panter_losore_field = antall_panter_losore_field
        self.ajour_dato_losore_field = APIHelper.RFC3339DateTime(ajour_dato_losore_field) if ajour_dato_losore_field else None
        self.antall_panter_eiendom_field = antall_panter_eiendom_field
        self.ajour_dato_eiendom_field = APIHelper.RFC3339DateTime(ajour_dato_eiendom_field) if ajour_dato_eiendom_field else None

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
        antall_inkasso_field = dictionary.get('antallInkassoField')
        ajour_dato_inkasso_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("ajourDatoInkassoField")).datetime if dictionary.get("ajourDatoInkassoField") else None
        antall_panter_losore_field = dictionary.get('antallPanterLosoreField')
        ajour_dato_losore_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("ajourDatoLosoreField")).datetime if dictionary.get("ajourDatoLosoreField") else None
        antall_panter_eiendom_field = dictionary.get('antallPanterEiendomField')
        ajour_dato_eiendom_field = APIHelper.RFC3339DateTime.from_value(dictionary.get("ajourDatoEiendomField")).datetime if dictionary.get("ajourDatoEiendomField") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(antall_inkasso_field,
                   ajour_dato_inkasso_field,
                   antall_panter_losore_field,
                   ajour_dato_losore_field,
                   antall_panter_eiendom_field,
                   ajour_dato_eiendom_field,
                   dictionary)


