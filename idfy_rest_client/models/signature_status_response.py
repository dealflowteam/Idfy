# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_status_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.organization_response

class SignatureStatusResponse(object):

    """Implementation of the 'SignatureStatusResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (string): TODO: type description here.
        organizations (list of OrganizationResponse): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id":'RequestId',
        "organizations":'Organizations'
    }

    def __init__(self,
                 request_id=None,
                 organizations=None,
                 additional_properties = {}):
        """Constructor for the SignatureStatusResponse class"""

        # Initialize members of the class
        self.request_id = request_id
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
        request_id = dictionary.get('RequestId')
        organizations = None
        if dictionary.get('Organizations') != None:
            organizations = list()
            for structure in dictionary.get('Organizations'):
                organizations.append(idfy_rest_client.models.organization_response.OrganizationResponse.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(request_id,
                   organizations,
                   dictionary)


