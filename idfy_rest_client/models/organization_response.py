# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.organization_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class OrganizationResponse(object):

    """Implementation of the 'OrganizationResponse' model.

    TODO: type model description here.

    Attributes:
        mva_number (int): TODO: type description here.
        prokura (string): TODO: type description here.
        signature (string): TODO: type description here.
        report (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mva_number":'MvaNumber',
        "prokura":'Prokura',
        "signature":'Signature',
        "report":'Report'
    }

    def __init__(self,
                 mva_number=None,
                 prokura=None,
                 signature=None,
                 report=None,
                 additional_properties = {}):
        """Constructor for the OrganizationResponse class"""

        # Initialize members of the class
        self.mva_number = mva_number
        self.prokura = prokura
        self.signature = signature
        self.report = report

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
        mva_number = dictionary.get('MvaNumber')
        prokura = dictionary.get('Prokura')
        signature = dictionary.get('Signature')
        report = dictionary.get('Report')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mva_number,
                   prokura,
                   signature,
                   report,
                   dictionary)


