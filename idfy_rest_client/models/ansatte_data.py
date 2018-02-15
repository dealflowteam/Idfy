# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.ansatte_data

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class AnsatteData(object):

    """Implementation of the 'AnsatteData' model.

    TODO: type model description here.

    Attributes:
        ansatte_ar_field (int): TODO: type description here.
        ansatte_antall_field (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ansatte_ar_field":'ansatteArField',
        "ansatte_antall_field":'ansatteAntallField'
    }

    def __init__(self,
                 ansatte_ar_field=None,
                 ansatte_antall_field=None,
                 additional_properties = {}):
        """Constructor for the AnsatteData class"""

        # Initialize members of the class
        self.ansatte_ar_field = ansatte_ar_field
        self.ansatte_antall_field = ansatte_antall_field

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
        ansatte_ar_field = dictionary.get('ansatteArField')
        ansatte_antall_field = dictionary.get('ansatteAntallField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(ansatte_ar_field,
                   ansatte_antall_field,
                   dictionary)


