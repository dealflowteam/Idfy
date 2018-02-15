# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_record

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.lei_entity
import idfy_rest_client.models.lei_registration
import idfy_rest_client.models.lei_extension

class LeiRecord(object):

    """Implementation of the 'LeiRecord' model.

    TODO: type model description here.

    Attributes:
        lei (string): TODO: type description here.
        entity (LeiEntity): TODO: type description here.
        registration (LeiRegistration): TODO: type description here.
        extension (LeiExtension): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lei":'Lei',
        "entity":'Entity',
        "registration":'Registration',
        "extension":'Extension'
    }

    def __init__(self,
                 lei=None,
                 entity=None,
                 registration=None,
                 extension=None,
                 additional_properties = {}):
        """Constructor for the LeiRecord class"""

        # Initialize members of the class
        self.lei = lei
        self.entity = entity
        self.registration = registration
        self.extension = extension

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
        lei = dictionary.get('Lei')
        entity = idfy_rest_client.models.lei_entity.LeiEntity.from_dictionary(dictionary.get('Entity')) if dictionary.get('Entity') else None
        registration = idfy_rest_client.models.lei_registration.LeiRegistration.from_dictionary(dictionary.get('Registration')) if dictionary.get('Registration') else None
        extension = idfy_rest_client.models.lei_extension.LeiExtension.from_dictionary(dictionary.get('Extension')) if dictionary.get('Extension') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(lei,
                   entity,
                   registration,
                   extension,
                   dictionary)


