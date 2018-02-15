# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.scoring

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.arsaks_data

class Scoring(object):

    """Implementation of the 'Scoring' model.

    TODO: type model description here.

    Attributes:
        beslutning_field (string): TODO: type description here.
        arsaks_data_field (list of ArsaksData): TODO: type description here.
        score_field (int): TODO: type description here.
        grense_avslag_field (int): TODO: type description here.
        grense_godkjent_field (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "beslutning_field":'beslutningField',
        "arsaks_data_field":'arsaksDataField',
        "score_field":'scoreField',
        "grense_avslag_field":'grenseAvslagField',
        "grense_godkjent_field":'grenseGodkjentField'
    }

    def __init__(self,
                 beslutning_field=None,
                 arsaks_data_field=None,
                 score_field=None,
                 grense_avslag_field=None,
                 grense_godkjent_field=None,
                 additional_properties = {}):
        """Constructor for the Scoring class"""

        # Initialize members of the class
        self.beslutning_field = beslutning_field
        self.arsaks_data_field = arsaks_data_field
        self.score_field = score_field
        self.grense_avslag_field = grense_avslag_field
        self.grense_godkjent_field = grense_godkjent_field

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
        beslutning_field = dictionary.get('beslutningField')
        arsaks_data_field = None
        if dictionary.get('arsaksDataField') != None:
            arsaks_data_field = list()
            for structure in dictionary.get('arsaksDataField'):
                arsaks_data_field.append(idfy_rest_client.models.arsaks_data.ArsaksData.from_dictionary(structure))
        score_field = dictionary.get('scoreField')
        grense_avslag_field = dictionary.get('grenseAvslagField')
        grense_godkjent_field = dictionary.get('grenseGodkjentField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(beslutning_field,
                   arsaks_data_field,
                   score_field,
                   grense_avslag_field,
                   grense_godkjent_field,
                   dictionary)


