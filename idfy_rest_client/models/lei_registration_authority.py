# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_registration_authority

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class LeiRegistrationAuthority(object):

    """Implementation of the 'LeiRegistrationAuthority' model.

    TODO: type model description here.

    Attributes:
        registration_authority_id (string): TODO: type description here.
        registration_authority_entity_id (string): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "registration_authority_id":'RegistrationAuthorityId',
        "registration_authority_entity_id":'RegistrationAuthorityEntityId'
    }

    def __init__(self,
                 registration_authority_id=None,
                 registration_authority_entity_id=None,
                 additional_properties = {}):
        """Constructor for the LeiRegistrationAuthority class"""

        # Initialize members of the class
        self.registration_authority_id = registration_authority_id
        self.registration_authority_entity_id = registration_authority_entity_id

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
        registration_authority_id = dictionary.get('RegistrationAuthorityId')
        registration_authority_entity_id = dictionary.get('RegistrationAuthorityEntityId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(registration_authority_id,
                   registration_authority_entity_id,
                   dictionary)


