# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.organization_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.check_signature

class OrganizationRequest(object):

    """Implementation of the 'OrganizationRequest' model.

    TODO: type model description here.

    Attributes:
        org_number (string): TODO: type description here.
        prokura (bool): TODO: type description here.
        signature (bool): TODO: type description here.
        signatures (list of CheckSignature): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "org_number":'OrgNumber',
        "prokura":'Prokura',
        "signature":'Signature',
        "signatures":'Signatures'
    }

    def __init__(self,
                 org_number=None,
                 prokura=None,
                 signature=None,
                 signatures=None,
                 additional_properties = {}):
        """Constructor for the OrganizationRequest class"""

        # Initialize members of the class
        self.org_number = org_number
        self.prokura = prokura
        self.signature = signature
        self.signatures = signatures

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
        org_number = dictionary.get('OrgNumber')
        prokura = dictionary.get('Prokura')
        signature = dictionary.get('Signature')
        signatures = None
        if dictionary.get('Signatures') != None:
            signatures = list()
            for structure in dictionary.get('Signatures'):
                signatures.append(idfy_rest_client.models.check_signature.CheckSignature.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(org_number,
                   prokura,
                   signature,
                   signatures,
                   dictionary)


