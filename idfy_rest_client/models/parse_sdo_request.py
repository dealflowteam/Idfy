# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.parse_sdo_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class ParseSDORequest(object):

    """Implementation of the 'ParseSDORequest' model.

    TODO: type model description here.

    Attributes:
        sdo_data (string): Base 64 encoded SDO (Signed document)
        external_reference (string): The service reference for the signing.
            Will be used for auditlog, and invoicing
        fetch_ssn (bool): Fetch social security number (Requires valid scope)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sdo_data":'sdoData',
        "external_reference":'externalReference',
        "fetch_ssn":'fetchSSN'
    }

    def __init__(self,
                 sdo_data=None,
                 external_reference=None,
                 fetch_ssn=None,
                 additional_properties = {}):
        """Constructor for the ParseSDORequest class"""

        # Initialize members of the class
        self.sdo_data = sdo_data
        self.external_reference = external_reference
        self.fetch_ssn = fetch_ssn

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
        fetch_ssn = dictionary.get('fetchSSN')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(sdo_data,
                   external_reference,
                   fetch_ssn,
                   dictionary)


