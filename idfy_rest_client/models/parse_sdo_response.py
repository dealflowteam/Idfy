# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.parse_sdo_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.seal
import idfy_rest_client.models.sdo_signers
import idfy_rest_client.models.validation_error

class ParseSDOResponse(object):

    """Implementation of the 'ParseSDOResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (string): TODO: type description here.
        audit_id (uuid|string): Reference to audit log
        signers_valid (bool): Is the signatures valid
        seal (Seal): Is the sealing of the SDO valid
        signers (list of SDOSigners): Signers list
        summary (string): Summary
        validation_error (ValidationError): Error messages
        signed_data (string): Original data from document (base64 string)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id":'requestId',
        "audit_id":'auditId',
        "signers_valid":'signersValid',
        "seal":'seal',
        "signers":'signers',
        "summary":'summary',
        "validation_error":'validationError',
        "signed_data":'signedData'
    }

    def __init__(self,
                 request_id=None,
                 audit_id=None,
                 signers_valid=None,
                 seal=None,
                 signers=None,
                 summary=None,
                 validation_error=None,
                 signed_data=None,
                 additional_properties = {}):
        """Constructor for the ParseSDOResponse class"""

        # Initialize members of the class
        self.request_id = request_id
        self.audit_id = audit_id
        self.signers_valid = signers_valid
        self.seal = seal
        self.signers = signers
        self.summary = summary
        self.validation_error = validation_error
        self.signed_data = signed_data

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
        request_id = dictionary.get('requestId')
        audit_id = dictionary.get('auditId')
        signers_valid = dictionary.get('signersValid')
        seal = idfy_rest_client.models.seal.Seal.from_dictionary(dictionary.get('seal')) if dictionary.get('seal') else None
        signers = None
        if dictionary.get('signers') != None:
            signers = list()
            for structure in dictionary.get('signers'):
                signers.append(idfy_rest_client.models.sdo_signers.SDOSigners.from_dictionary(structure))
        summary = dictionary.get('summary')
        validation_error = idfy_rest_client.models.validation_error.ValidationError.from_dictionary(dictionary.get('validationError')) if dictionary.get('validationError') else None
        signed_data = dictionary.get('signedData')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(request_id,
                   audit_id,
                   signers_valid,
                   seal,
                   signers,
                   summary,
                   validation_error,
                   signed_data,
                   dictionary)


