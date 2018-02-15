# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.validate_sdo_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.seal
import idfy_rest_client.models.validated_signers
import idfy_rest_client.models.validation_error

class ValidateSDOResponse(object):

    """Implementation of the 'ValidateSDOResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (string): TODO: type description here.
        valid (bool): Is the SDO valid
        seal (Seal): Is the Seal of the SDO valid
        signers (list of ValidatedSigners): TODO: type description here.
        summary (string): TODO: type description here.
        validation_error (ValidationError): TODO: type description here.
        audit_id (uuid|string): The AuditId vil only be set for users with an
            account on the API.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id":'requestId',
        "valid":'valid',
        "seal":'seal',
        "signers":'signers',
        "summary":'summary',
        "validation_error":'validationError',
        "audit_id":'auditId'
    }

    def __init__(self,
                 request_id=None,
                 valid=None,
                 seal=None,
                 signers=None,
                 summary=None,
                 validation_error=None,
                 audit_id=None,
                 additional_properties = {}):
        """Constructor for the ValidateSDOResponse class"""

        # Initialize members of the class
        self.request_id = request_id
        self.valid = valid
        self.seal = seal
        self.signers = signers
        self.summary = summary
        self.validation_error = validation_error
        self.audit_id = audit_id

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
        valid = dictionary.get('valid')
        seal = idfy_rest_client.models.seal.Seal.from_dictionary(dictionary.get('seal')) if dictionary.get('seal') else None
        signers = None
        if dictionary.get('signers') != None:
            signers = list()
            for structure in dictionary.get('signers'):
                signers.append(idfy_rest_client.models.validated_signers.ValidatedSigners.from_dictionary(structure))
        summary = dictionary.get('summary')
        validation_error = idfy_rest_client.models.validation_error.ValidationError.from_dictionary(dictionary.get('validationError')) if dictionary.get('validationError') else None
        audit_id = dictionary.get('auditId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(request_id,
                   valid,
                   seal,
                   signers,
                   summary,
                   validation_error,
                   audit_id,
                   dictionary)


