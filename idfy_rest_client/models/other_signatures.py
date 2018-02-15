# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.other_signatures

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.signature

class OtherSignatures(object):

    """Implementation of the 'OtherSignatures' model.

    TODO: type model description here.

    Attributes:
        required_number_of_others (int): TODO: type description here.
        list (list of Signature): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "required_number_of_others":'RequiredNumberOfOthers',
        "list":'List'
    }

    def __init__(self,
                 required_number_of_others=None,
                 list=None,
                 additional_properties = {}):
        """Constructor for the OtherSignatures class"""

        # Initialize members of the class
        self.required_number_of_others = required_number_of_others
        self.list = list

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
        required_number_of_others = dictionary.get('RequiredNumberOfOthers')
        list = None
        if dictionary.get('List') != None:
            list = list()
            for structure in dictionary.get('List'):
                list.append(idfy_rest_client.models.signature.Signature.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(required_number_of_others,
                   list,
                   dictionary)


