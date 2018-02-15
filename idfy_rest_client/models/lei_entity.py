# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_entity

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.lei_entity_address
import idfy_rest_client.models.lei_legal_form
import idfy_rest_client.models.lei_registration_authority

class LeiEntity(object):

    """Implementation of the 'LeiEntity' model.

    TODO: type model description here.

    Attributes:
        headquarters_address (LeiEntityAddress): TODO: type description here.
        legal_address (LeiEntityAddress): TODO: type description here.
        legal_jurisdiction (string): TODO: type description here.
        legal_name (string): TODO: type description here.
        entity_status (string): TODO: type description here.
        entity_category (string): TODO: type description here.
        legal_form (LeiLegalForm): TODO: type description here.
        registration_authority (LeiRegistrationAuthority): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "headquarters_address":'HeadquartersAddress',
        "legal_address":'LegalAddress',
        "legal_jurisdiction":'LegalJurisdiction',
        "legal_name":'LegalName',
        "entity_status":'EntityStatus',
        "entity_category":'EntityCategory',
        "legal_form":'LegalForm',
        "registration_authority":'RegistrationAuthority'
    }

    def __init__(self,
                 headquarters_address=None,
                 legal_address=None,
                 legal_jurisdiction=None,
                 legal_name=None,
                 entity_status=None,
                 entity_category=None,
                 legal_form=None,
                 registration_authority=None,
                 additional_properties = {}):
        """Constructor for the LeiEntity class"""

        # Initialize members of the class
        self.headquarters_address = headquarters_address
        self.legal_address = legal_address
        self.legal_jurisdiction = legal_jurisdiction
        self.legal_name = legal_name
        self.entity_status = entity_status
        self.entity_category = entity_category
        self.legal_form = legal_form
        self.registration_authority = registration_authority

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
        headquarters_address = idfy_rest_client.models.lei_entity_address.LeiEntityAddress.from_dictionary(dictionary.get('HeadquartersAddress')) if dictionary.get('HeadquartersAddress') else None
        legal_address = idfy_rest_client.models.lei_entity_address.LeiEntityAddress.from_dictionary(dictionary.get('LegalAddress')) if dictionary.get('LegalAddress') else None
        legal_jurisdiction = dictionary.get('LegalJurisdiction')
        legal_name = dictionary.get('LegalName')
        entity_status = dictionary.get('EntityStatus')
        entity_category = dictionary.get('EntityCategory')
        legal_form = idfy_rest_client.models.lei_legal_form.LeiLegalForm.from_dictionary(dictionary.get('LegalForm')) if dictionary.get('LegalForm') else None
        registration_authority = idfy_rest_client.models.lei_registration_authority.LeiRegistrationAuthority.from_dictionary(dictionary.get('RegistrationAuthority')) if dictionary.get('RegistrationAuthority') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(headquarters_address,
                   legal_address,
                   legal_jurisdiction,
                   legal_name,
                   entity_status,
                   entity_category,
                   legal_form,
                   registration_authority,
                   dictionary)


