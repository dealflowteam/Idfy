# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.economy

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Economy(object):

    """Implementation of the 'Economy' model.

    TODO: type model description here.

    Attributes:
        year (int): TODO: type description here.
        turnover (long|int): TODO: type description here.
        operating_profit (long|int): TODO: type description here.
        equity (float): TODO: type description here.
        employees (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "year":'Year',
        "turnover":'Turnover',
        "operating_profit":'OperatingProfit',
        "equity":'Equity',
        "employees":'Employees'
    }

    def __init__(self,
                 year=None,
                 turnover=None,
                 operating_profit=None,
                 equity=None,
                 employees=None,
                 additional_properties = {}):
        """Constructor for the Economy class"""

        # Initialize members of the class
        self.year = year
        self.turnover = turnover
        self.operating_profit = operating_profit
        self.equity = equity
        self.employees = employees

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
        turnover = dictionary.get('Turnover')
        operating_profit = dictionary.get('OperatingProfit')
        equity = dictionary.get('Equity')
        employees = dictionary.get('Employees')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(year,
                   turnover,
                   operating_profit,
                   equity,
                   employees,
                   dictionary)


