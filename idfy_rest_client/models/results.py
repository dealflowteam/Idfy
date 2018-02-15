# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.results

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Results(object):

    """Implementation of the 'Results' model.

    TODO: type model description here.

    Attributes:
        matchit_personal_info (string): TODO: type description here.
        matchit_company_info (string): TODO: type description here.
        difi_company_info (string): TODO: type description here.
        personal_credit_check (string): TODO: type description here.
        business_credit_check (string): TODO: type description here.
        official_personal_info (string): TODO: type description here.
        aml_b_2_c_identify_and_screening (string): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "matchit_personal_info":'matchitPersonalInfo',
        "matchit_company_info":'matchitCompanyInfo',
        "difi_company_info":'difiCompanyInfo',
        "personal_credit_check":'personalCreditCheck',
        "business_credit_check":'businessCreditCheck',
        "official_personal_info":'officialPersonalInfo',
        "aml_b_2_c_identify_and_screening":'amlB2cIdentifyAndScreening'
    }

    def __init__(self,
                 matchit_personal_info=None,
                 matchit_company_info=None,
                 difi_company_info=None,
                 personal_credit_check=None,
                 business_credit_check=None,
                 official_personal_info=None,
                 aml_b_2_c_identify_and_screening=None,
                 additional_properties = {}):
        """Constructor for the Results class"""

        # Initialize members of the class
        self.matchit_personal_info = matchit_personal_info
        self.matchit_company_info = matchit_company_info
        self.difi_company_info = difi_company_info
        self.personal_credit_check = personal_credit_check
        self.business_credit_check = business_credit_check
        self.official_personal_info = official_personal_info
        self.aml_b_2_c_identify_and_screening = aml_b_2_c_identify_and_screening

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
        matchit_personal_info = dictionary.get('matchitPersonalInfo')
        matchit_company_info = dictionary.get('matchitCompanyInfo')
        difi_company_info = dictionary.get('difiCompanyInfo')
        personal_credit_check = dictionary.get('personalCreditCheck')
        business_credit_check = dictionary.get('businessCreditCheck')
        official_personal_info = dictionary.get('officialPersonalInfo')
        aml_b_2_c_identify_and_screening = dictionary.get('amlB2cIdentifyAndScreening')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(matchit_personal_info,
                   matchit_company_info,
                   difi_company_info,
                   personal_credit_check,
                   business_credit_check,
                   official_personal_info,
                   aml_b_2_c_identify_and_screening,
                   dictionary)


