# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_object

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.required_signatures
import idfy_rest_client.models.other_signatures

class SignatureObject(object):

    """Implementation of the 'SignatureObject' model.

    TODO: type model description here.

    Attributes:
        requirements_description (string): TODO: type description here.
        required (RequiredSignatures): TODO: type description here.
        others (OtherSignatures): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "requirements_description":'RequirementsDescription',
        "required":'Required',
        "others":'Others'
    }

    def __init__(self,
                 requirements_description=None,
                 required=None,
                 others=None,
                 additional_properties = {}):
        """Constructor for the SignatureObject class"""

        # Initialize members of the class
        self.requirements_description = requirements_description
        self.required = required
        self.others = others

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
        requirements_description = dictionary.get('RequirementsDescription')
        required = idfy_rest_client.models.required_signatures.RequiredSignatures.from_dictionary(dictionary.get('Required')) if dictionary.get('Required') else None
        others = idfy_rest_client.models.other_signatures.OtherSignatures.from_dictionary(dictionary.get('Others')) if dictionary.get('Others') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(requirements_description,
                   required,
                   others,
                   dictionary)


