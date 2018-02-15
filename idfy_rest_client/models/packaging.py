# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.packaging

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.pades_settings

class Packaging(object):

    """Implementation of the 'Packaging' model.

    TODO: type model description here.

    Attributes:
        signature_package_formats (list of SignaturePackageFormat): The
            format(s) that you will be able to fetch the signed document
            afterwards. Read more about SignaturePackage format in the
            documentation. (The native package format is included
            automatically (i.e. bankid sdo)
        pades_settings (PadesSettings): If you are using pades as a signature
            package format you can define settings here

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signature_package_formats":'signaturePackageFormats',
        "pades_settings":'padesSettings'
    }

    def __init__(self,
                 signature_package_formats=None,
                 pades_settings=None,
                 additional_properties = {}):
        """Constructor for the Packaging class"""

        # Initialize members of the class
        self.signature_package_formats = signature_package_formats
        self.pades_settings = pades_settings

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
        signature_package_formats = dictionary.get('signaturePackageFormats')
        pades_settings = idfy_rest_client.models.pades_settings.PadesSettings.from_dictionary(dictionary.get('padesSettings')) if dictionary.get('padesSettings') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(signature_package_formats,
                   pades_settings,
                   dictionary)


