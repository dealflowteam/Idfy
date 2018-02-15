# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.transaction

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class Transaction(object):

    """Implementation of the 'Transaction' model.

    TODO: type model description here.

    Attributes:
        id (string): Transaction ID
        date (datetime): The date for the transaction
        product_id (string): Product ID (SIGN, IDENTIFICATION etc)
        description (string): Transaction description
        count (int): Number of transactions for the selected date
        customer_number (int): Your customer number in our invocing system
        external_reference (string): Your reference to the transaction (by
            ExternalRef in the API call)
        department_id (string): The Departments ID if specified

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'ID',
        "date":'Date',
        "product_id":'ProductID',
        "description":'Description',
        "count":'Count',
        "customer_number":'CustomerNumber',
        "external_reference":'ExternalReference',
        "department_id":'DepartmentId'
    }

    def __init__(self,
                 id=None,
                 date=None,
                 product_id=None,
                 description=None,
                 count=None,
                 customer_number=None,
                 external_reference=None,
                 department_id=None,
                 additional_properties = {}):
        """Constructor for the Transaction class"""

        # Initialize members of the class
        self.id = id
        self.date = APIHelper.RFC3339DateTime(date) if date else None
        self.product_id = product_id
        self.description = description
        self.count = count
        self.customer_number = customer_number
        self.external_reference = external_reference
        self.department_id = department_id

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
        id = dictionary.get('ID')
        date = APIHelper.RFC3339DateTime.from_value(dictionary.get("Date")).datetime if dictionary.get("Date") else None
        product_id = dictionary.get('ProductID')
        description = dictionary.get('Description')
        count = dictionary.get('Count')
        customer_number = dictionary.get('CustomerNumber')
        external_reference = dictionary.get('ExternalReference')
        department_id = dictionary.get('DepartmentId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   date,
                   product_id,
                   description,
                   count,
                   customer_number,
                   external_reference,
                   department_id,
                   dictionary)


