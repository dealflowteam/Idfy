# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_economy

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonEconomy(object):

    """Implementation of the 'Person.Economy' model.

    TODO: type model description here.

    Attributes:
        year (int): TODO: type description here.
        net_income (float): TODO: type description here.
        income_change (float): TODO: type description here.
        fortune (float): TODO: type description here.
        assessed_tax (float): TODO: type description here.
        tax_class (string): TODO: type description here.
        municipal (string): TODO: type description here.
        municipal_number (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "year":'Year',
        "net_income":'NetIncome',
        "income_change":'IncomeChange',
        "fortune":'Fortune',
        "assessed_tax":'AssessedTax',
        "tax_class":'TaxClass',
        "municipal":'Municipal',
        "municipal_number":'MunicipalNumber'
    }

    def __init__(self,
                 year=None,
                 net_income=None,
                 income_change=None,
                 fortune=None,
                 assessed_tax=None,
                 tax_class=None,
                 municipal=None,
                 municipal_number=None,
                 additional_properties = {}):
        """Constructor for the PersonEconomy class"""

        # Initialize members of the class
        self.year = year
        self.net_income = net_income
        self.income_change = income_change
        self.fortune = fortune
        self.assessed_tax = assessed_tax
        self.tax_class = tax_class
        self.municipal = municipal
        self.municipal_number = municipal_number

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
        year = dictionary.get('Year')
        net_income = dictionary.get('NetIncome')
        income_change = dictionary.get('IncomeChange')
        fortune = dictionary.get('Fortune')
        assessed_tax = dictionary.get('AssessedTax')
        tax_class = dictionary.get('TaxClass')
        municipal = dictionary.get('Municipal')
        municipal_number = dictionary.get('MunicipalNumber')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(year,
                   net_income,
                   income_change,
                   fortune,
                   assessed_tax,
                   tax_class,
                   municipal,
                   municipal_number,
                   dictionary)


