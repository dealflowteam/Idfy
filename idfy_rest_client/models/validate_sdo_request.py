# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.validate_sdo_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.signers

class ValidateSDORequest(object):

    """Implementation of the 'ValidateSDORequest' model.

    TODO: type model description here.

    Attributes:
        sdo_data (string): Base 64 encoded SDO (Signed document)
        external_reference (string): The service reference for the signing.
            Will be used for auditlog, and invoicing
        data_to_validate (string): Check that the original data matches the
            sdo data (optional, base64 encoded)
        signers_to_validate (list of Signers): Add signers to validate
            (optional)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sdo_data":'sdoData',
        "external_reference":'externalReference',
        "data_to_validate":'dataToValidate',
        "signers_to_validate":'signersToValidate'
    }

    def __init__(self,
                 sdo_data=None,
                 external_reference=None,
                 data_to_validate=None,
                 signers_to_validate=None,
                 additional_properties = {}):
        """Constructor for the ValidateSDORequest class"""

        # Initialize members of the class
        self.sdo_data = sdo_data
        self.external_reference = external_reference
        self.data_to_validate = data_to_validate
        self.signers_to_validate = signers_to_validate

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
        sdo_data = dictionary.get('sdoData')
        external_reference = dictionary.get('externalReference')
        data_to_validate = dictionary.get('dataToValidate')
        signers_to_validate = None
        if dictionary.get('signersToValidate') != None:
            signers_to_validate = list()
            for structure in dictionary.get('signersToValidate'):
                signers_to_validate.append(idfy_rest_client.models.signers.Signers.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(sdo_data,
                   external_reference,
                   data_to_validate,
                   signers_to_validate,
                   dictionary)


