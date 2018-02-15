# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_disponibel_inntekt

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonDisponibelInntekt(object):

    """Implementation of the 'Person.DisponibelInntekt' model.

    TODO: type model description here.

    Attributes:
        kode_field (int): TODO: type description here.
        beskrivelse_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kode_field":'kodeField',
        "beskrivelse_field":'beskrivelseField'
    }

    def __init__(self,
                 kode_field=None,
                 beskrivelse_field=None,
                 additional_properties = {}):
        """Constructor for the PersonDisponibelInntekt class"""

        # Initialize members of the class
        self.kode_field = kode_field
        self.beskrivelse_field = beskrivelse_field

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
        kode_field = dictionary.get('kodeField')
        beskrivelse_field = dictionary.get('beskrivelseField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(kode_field,
                   beskrivelse_field,
                   dictionary)


