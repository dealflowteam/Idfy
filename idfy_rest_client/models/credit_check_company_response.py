# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.credit_check_company_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.economy
import idfy_rest_client.models.hent_foretak_response

class CreditCheckCompanyResponse(object):

    """Implementation of the 'CreditCheckCompanyResponse' model.

    TODO: type model description here.

    Attributes:
        org_number (int): TODO: type description here.
        org_name (string): TODO: type description here.
        address (string): TODO: type description here.
        postal_code (string): TODO: type description here.
        city (string): TODO: type description here.
        incorporation_date (datetime): TODO: type description here.
        chair_man (string): TODO: type description here.
        ceo (string): TODO: type description here.
        economy (Economy): TODO: type description here.
        bisnode_rating_code (string): TODO: type description here.
        bisnode_rating_description (string): TODO: type description here.
        credit_limit (float): TODO: type description here.
        payment_defaults (string): TODO: type description here.
        request_id (string): TODO: type description here.
        report (string): TODO: type description here.
        detailed_information (HentForetakResponse): TODO: type description
            here.
        number_of_payment_defaults (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "org_number":'OrgNumber',
        "org_name":'OrgName',
        "address":'Address',
        "postal_code":'PostalCode',
        "city":'City',
        "incorporation_date":'IncorporationDate',
        "chair_man":'ChairMan',
        "ceo":'CEO',
        "economy":'Economy',
        "bisnode_rating_code":'BisnodeRatingCode',
        "bisnode_rating_description":'BisnodeRatingDescription',
        "credit_limit":'CreditLimit',
        "payment_defaults":'PaymentDefaults',
        "request_id":'RequestId',
        "report":'Report',
        "detailed_information":'DetailedInformation',
        "number_of_payment_defaults":'NumberOfPaymentDefaults'
    }

    def __init__(self,
                 org_number=None,
                 org_name=None,
                 address=None,
                 postal_code=None,
                 city=None,
                 incorporation_date=None,
                 chair_man=None,
                 ceo=None,
                 economy=None,
                 bisnode_rating_code=None,
                 bisnode_rating_description=None,
                 credit_limit=None,
                 payment_defaults=None,
                 request_id=None,
                 report=None,
                 detailed_information=None,
                 number_of_payment_defaults=None,
                 additional_properties = {}):
        """Constructor for the CreditCheckCompanyResponse class"""

        # Initialize members of the class
        self.org_number = org_number
        self.org_name = org_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.incorporation_date = APIHelper.RFC3339DateTime(incorporation_date) if incorporation_date else None
        self.chair_man = chair_man
        self.ceo = ceo
        self.economy = economy
        self.bisnode_rating_code = bisnode_rating_code
        self.bisnode_rating_description = bisnode_rating_description
        self.credit_limit = credit_limit
        self.payment_defaults = payment_defaults
        self.request_id = request_id
        self.report = report
        self.detailed_information = detailed_information
        self.number_of_payment_defaults = number_of_payment_defaults

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
        org_number = dictionary.get('OrgNumber')
        org_name = dictionary.get('OrgName')
        address = dictionary.get('Address')
        postal_code = dictionary.get('PostalCode')
        city = dictionary.get('City')
        incorporation_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("IncorporationDate")).datetime if dictionary.get("IncorporationDate") else None
        chair_man = dictionary.get('ChairMan')
        ceo = dictionary.get('CEO')
        economy = idfy_rest_client.models.economy.Economy.from_dictionary(dictionary.get('Economy')) if dictionary.get('Economy') else None
        bisnode_rating_code = dictionary.get('BisnodeRatingCode')
        bisnode_rating_description = dictionary.get('BisnodeRatingDescription')
        credit_limit = dictionary.get('CreditLimit')
        payment_defaults = dictionary.get('PaymentDefaults')
        request_id = dictionary.get('RequestId')
        report = dictionary.get('Report')
        detailed_information = idfy_rest_client.models.hent_foretak_response.HentForetakResponse.from_dictionary(dictionary.get('DetailedInformation')) if dictionary.get('DetailedInformation') else None
        number_of_payment_defaults = dictionary.get('NumberOfPaymentDefaults')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(org_number,
                   org_name,
                   address,
                   postal_code,
                   city,
                   incorporation_date,
                   chair_man,
                   ceo,
                   economy,
                   bisnode_rating_code,
                   bisnode_rating_description,
                   credit_limit,
                   payment_defaults,
                   request_id,
                   report,
                   detailed_information,
                   number_of_payment_defaults,
                   dictionary)


