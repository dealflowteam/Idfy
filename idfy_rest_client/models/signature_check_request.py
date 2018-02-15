# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_check_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.organization_request

class SignatureCheckRequest(object):

    """Implementation of the 'SignatureCheckRequest' model.

    TODO: type model description here.

    Attributes:
        organizations (list of OrganizationRequest): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "organizations":'Organizations'
    }

    def __init__(self,
                 organizations=None,
                 additional_properties = {}):
        """Constructor for the SignatureCheckRequest class"""

        # Initialize members of the class
        self.organizations = organizations

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
        organizations = None
        if dictionary.get('Organizations') != None:
            organizations = list()
            for structure in dictionary.get('Organizations'):
                organizations.append(idfy_rest_client.models.organization_request.OrganizationRequest.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(organizations,
                   dictionary)


