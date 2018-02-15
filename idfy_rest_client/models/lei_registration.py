# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_registration

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.managing_lou

class LeiRegistration(object):

    """Implementation of the 'LeiRegistration' model.

    TODO: type model description here.

    Attributes:
        initial_registration_date (datetime): TODO: type description here.
        registration_status (string): TODO: type description here.
        validation_sources (string): TODO: type description here.
        last_update_date (datetime): TODO: type description here.
        next_renewal_date (datetime): TODO: type description here.
        managing_lou (ManagingLou): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "initial_registration_date":'InitialRegistrationDate',
        "registration_status":'RegistrationStatus',
        "validation_sources":'ValidationSources',
        "last_update_date":'LastUpdateDate',
        "next_renewal_date":'NextRenewalDate',
        "managing_lou":'ManagingLou'
    }

    def __init__(self,
                 initial_registration_date=None,
                 registration_status=None,
                 validation_sources=None,
                 last_update_date=None,
                 next_renewal_date=None,
                 managing_lou=None,
                 additional_properties = {}):
        """Constructor for the LeiRegistration class"""

        # Initialize members of the class
        self.initial_registration_date = APIHelper.RFC3339DateTime(initial_registration_date) if initial_registration_date else None
        self.registration_status = registration_status
        self.validation_sources = validation_sources
        self.last_update_date = APIHelper.RFC3339DateTime(last_update_date) if last_update_date else None
        self.next_renewal_date = APIHelper.RFC3339DateTime(next_renewal_date) if next_renewal_date else None
        self.managing_lou = managing_lou

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
        initial_registration_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("InitialRegistrationDate")).datetime if dictionary.get("InitialRegistrationDate") else None
        registration_status = dictionary.get('RegistrationStatus')
        validation_sources = dictionary.get('ValidationSources')
        last_update_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("LastUpdateDate")).datetime if dictionary.get("LastUpdateDate") else None
        next_renewal_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("NextRenewalDate")).datetime if dictionary.get("NextRenewalDate") else None
        managing_lou = idfy_rest_client.models.managing_lou.ManagingLou.from_dictionary(dictionary.get('ManagingLou')) if dictionary.get('ManagingLou') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(initial_registration_date,
                   registration_status,
                   validation_sources,
                   last_update_date,
                   next_renewal_date,
                   managing_lou,
                   dictionary)


