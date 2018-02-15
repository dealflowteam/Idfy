# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.special_properties

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class SpecialProperties(object):

    """Implementation of the 'SpecialProperties' model.

    TODO: type model description here.

    Attributes:
        bisnode_username (string): TODO: type description here.
        bisnode_password (string): TODO: type description here.
        include_pdf_reports (string): TODO: type description here.
        official_username (string): TODO: type description here.
        official_password (string): TODO: type description here.
        official_reason (string): TODO: type description here.
        official_system (string): TODO: type description here.
        aml_nationality (string): TODO: type description here.
        aml_language (string): TODO: type description here.
        aml_mode (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bisnode_username":'bisnodeUsername',
        "bisnode_password":'bisnodePassword',
        "include_pdf_reports":'includePdfReports',
        "official_username":'officialUsername',
        "official_password":'officialPassword',
        "official_reason":'officialReason',
        "official_system":'officialSystem',
        "aml_nationality":'amlNationality',
        "aml_language":'amlLanguage',
        "aml_mode":'amlMode'
    }

    def __init__(self,
                 bisnode_username=None,
                 bisnode_password=None,
                 include_pdf_reports=None,
                 official_username=None,
                 official_password=None,
                 official_reason=None,
                 official_system=None,
                 aml_nationality=None,
                 aml_language=None,
                 aml_mode=None,
                 additional_properties = {}):
        """Constructor for the SpecialProperties class"""

        # Initialize members of the class
        self.bisnode_username = bisnode_username
        self.bisnode_password = bisnode_password
        self.include_pdf_reports = include_pdf_reports
        self.official_username = official_username
        self.official_password = official_password
        self.official_reason = official_reason
        self.official_system = official_system
        self.aml_nationality = aml_nationality
        self.aml_language = aml_language
        self.aml_mode = aml_mode

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
        bisnode_username = dictionary.get('bisnodeUsername')
        bisnode_password = dictionary.get('bisnodePassword')
        include_pdf_reports = dictionary.get('includePdfReports')
        official_username = dictionary.get('officialUsername')
        official_password = dictionary.get('officialPassword')
        official_reason = dictionary.get('officialReason')
        official_system = dictionary.get('officialSystem')
        aml_nationality = dictionary.get('amlNationality')
        aml_language = dictionary.get('amlLanguage')
        aml_mode = dictionary.get('amlMode')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(bisnode_username,
                   bisnode_password,
                   include_pdf_reports,
                   official_username,
                   official_password,
                   official_reason,
                   official_system,
                   aml_nationality,
                   aml_language,
                   aml_mode,
                   dictionary)


