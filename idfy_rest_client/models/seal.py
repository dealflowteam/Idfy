# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.seal

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.certificate

class Seal(object):

    """Implementation of the 'Seal' model.

    TODO: type model description here.

    Attributes:
        sealed_by (string): TODO: type description here.
        sealed_timestamp (datetime): TODO: type description here.
        certificate (Certificate): TODO: type description here.
        seal_valid (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sealed_by":'sealedBy',
        "sealed_timestamp":'sealedTimestamp',
        "certificate":'certificate',
        "seal_valid":'sealValid'
    }

    def __init__(self,
                 sealed_by=None,
                 sealed_timestamp=None,
                 certificate=None,
                 seal_valid=None,
                 additional_properties = {}):
        """Constructor for the Seal class"""

        # Initialize members of the class
        self.sealed_by = sealed_by
        self.sealed_timestamp = APIHelper.RFC3339DateTime(sealed_timestamp) if sealed_timestamp else None
        self.certificate = certificate
        self.seal_valid = seal_valid

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
        sealed_by = dictionary.get('sealedBy')
        sealed_timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("sealedTimestamp")).datetime if dictionary.get("sealedTimestamp") else None
        certificate = idfy_rest_client.models.certificate.Certificate.from_dictionary(dictionary.get('certificate')) if dictionary.get('certificate') else None
        seal_valid = dictionary.get('sealValid')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(sealed_by,
                   sealed_timestamp,
                   certificate,
                   seal_valid,
                   dictionary)


