# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_credit_check_person_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.person_economy
import idfy_rest_client.models.person_hent_person_response

class PersonCreditCheckPersonResponse(object):

    """Implementation of the 'Person.CreditCheckPersonResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (string): TODO: type description here.
        report (string): TODO: type description here.
        name (string): TODO: type description here.
        address (string): TODO: type description here.
        city (string): TODO: type description here.
        postal_code (string): TODO: type description here.
        score (int): TODO: type description here.
        score_decision (string): TODO: type description here.
        date_of_birth (string): TODO: type description here.
        age (int): TODO: type description here.
        gender (string): TODO: type description here.
        number_of_payment_defaults (int): TODO: type description here.
        payment_defaults_amount (float): TODO: type description here.
        income_and_fortune (list of PersonEconomy): TODO: type description
            here.
        detailed_information (PersonHentPersonResponse): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id":'RequestId',
        "report":'Report',
        "name":'Name',
        "address":'Address',
        "city":'City',
        "postal_code":'PostalCode',
        "score":'Score',
        "score_decision":'ScoreDecision',
        "date_of_birth":'DateOfBirth',
        "age":'Age',
        "gender":'Gender',
        "number_of_payment_defaults":'NumberOfPaymentDefaults',
        "payment_defaults_amount":'PaymentDefaultsAmount',
        "income_and_fortune":'IncomeAndFortune',
        "detailed_information":'DetailedInformation'
    }

    def __init__(self,
                 request_id=None,
                 report=None,
                 name=None,
                 address=None,
                 city=None,
                 postal_code=None,
                 score=None,
                 score_decision=None,
                 date_of_birth=None,
                 age=None,
                 gender=None,
                 number_of_payment_defaults=None,
                 payment_defaults_amount=None,
                 income_and_fortune=None,
                 detailed_information=None,
                 additional_properties = {}):
        """Constructor for the PersonCreditCheckPersonResponse class"""

        # Initialize members of the class
        self.request_id = request_id
        self.report = report
        self.name = name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.score = score
        self.score_decision = score_decision
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.number_of_payment_defaults = number_of_payment_defaults
        self.payment_defaults_amount = payment_defaults_amount
        self.income_and_fortune = income_and_fortune
        self.detailed_information = detailed_information

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
        request_id = dictionary.get('RequestId')
        report = dictionary.get('Report')
        name = dictionary.get('Name')
        address = dictionary.get('Address')
        city = dictionary.get('City')
        postal_code = dictionary.get('PostalCode')
        score = dictionary.get('Score')
        score_decision = dictionary.get('ScoreDecision')
        date_of_birth = dictionary.get('DateOfBirth')
        age = dictionary.get('Age')
        gender = dictionary.get('Gender')
        number_of_payment_defaults = dictionary.get('NumberOfPaymentDefaults')
        payment_defaults_amount = dictionary.get('PaymentDefaultsAmount')
        income_and_fortune = None
        if dictionary.get('IncomeAndFortune') != None:
            income_and_fortune = list()
            for structure in dictionary.get('IncomeAndFortune'):
                income_and_fortune.append(idfy_rest_client.models.person_economy.PersonEconomy.from_dictionary(structure))
        detailed_information = idfy_rest_client.models.person_hent_person_response.PersonHentPersonResponse.from_dictionary(dictionary.get('DetailedInformation')) if dictionary.get('DetailedInformation') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(request_id,
                   report,
                   name,
                   address,
                   city,
                   postal_code,
                   score,
                   score_decision,
                   date_of_birth,
                   age,
                   gender,
                   number_of_payment_defaults,
                   payment_defaults_amount,
                   income_and_fortune,
                   detailed_information,
                   dictionary)


