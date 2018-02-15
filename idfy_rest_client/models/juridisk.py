# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.juridisk

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Juridisk(object):

    """Implementation of the 'Juridisk' model.

    TODO: type model description here.

    Attributes:
        prokura_field (string): TODO: type description here.
        signatur_field (string): TODO: type description here.
        eier_struktur_field (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prokura_field":'prokuraField',
        "signatur_field":'signaturField',
        "eier_struktur_field":'eierStrukturField'
    }

    def __init__(self,
                 prokura_field=None,
                 signatur_field=None,
                 eier_struktur_field=None,
                 additional_properties = {}):
        """Constructor for the Juridisk class"""

        # Initialize members of the class
        self.prokura_field = prokura_field
        self.signatur_field = signatur_field
        self.eier_struktur_field = eier_struktur_field

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
        prokura_field = dictionary.get('prokuraField')
        signatur_field = dictionary.get('signaturField')
        eier_struktur_field = dictionary.get('eierStrukturField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(prokura_field,
                   signatur_field,
                   eier_struktur_field,
                   dictionary)


