# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.jwt_validation_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.jwt_payload

class JwtValidationResponse(object):

    """Implementation of the 'JwtValidationResponse' model.

    TODO: type model description here.

    Attributes:
        jwt_valid (bool): True if jwt is valid
        expired (bool): True if expired
        jwt_payload (JwtPayload): Payload (valid data if jwt is valid)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "jwt_valid":'jwtValid',
        "expired":'expired',
        "jwt_payload":'jwtPayload'
    }

    def __init__(self,
                 jwt_valid=None,
                 expired=None,
                 jwt_payload=None,
                 additional_properties = {}):
        """Constructor for the JwtValidationResponse class"""

        # Initialize members of the class
        self.jwt_valid = jwt_valid
        self.expired = expired
        self.jwt_payload = jwt_payload

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
        jwt_valid = dictionary.get('jwtValid')
        expired = dictionary.get('expired')
        jwt_payload = idfy_rest_client.models.jwt_payload.JwtPayload.from_dictionary(dictionary.get('jwtPayload')) if dictionary.get('jwtPayload') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(jwt_valid,
                   expired,
                   jwt_payload,
                   dictionary)


