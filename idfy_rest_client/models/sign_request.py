# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.sign_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class SignRequest(object):

    """Implementation of the 'SignRequest' model.

    TODO: type model description here.

    Attributes:
        data_to_sign (string): Base 64 encoded data
        data_format (DataFormat): Format of data (i.e xml)
        external_reference (string): The service reference for the signing.
            Will be used for auditlog, and invoicing
        xslt (string): Base 64 encoded xslt (optional)
        signing_format (SigningFormat): Optional, if not set the default
            setting for the account will be used

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_to_sign":'dataToSign',
        "data_format":'dataFormat',
        "external_reference":'externalReference',
        "xslt":'xslt',
        "signing_format":'signingFormat'
    }

    def __init__(self,
                 data_to_sign=None,
                 data_format=None,
                 external_reference=None,
                 xslt=None,
                 signing_format=None,
                 additional_properties = {}):
        """Constructor for the SignRequest class"""

        # Initialize members of the class
        self.data_to_sign = data_to_sign
        self.data_format = data_format
        self.external_reference = external_reference
        self.xslt = xslt
        self.signing_format = signing_format

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
        data_to_sign = dictionary.get('dataToSign')
        data_format = dictionary.get('dataFormat')
        external_reference = dictionary.get('externalReference')
        xslt = dictionary.get('xslt')
        signing_format = dictionary.get('signingFormat')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(data_to_sign,
                   data_format,
                   external_reference,
                   xslt,
                   signing_format,
                   dictionary)


