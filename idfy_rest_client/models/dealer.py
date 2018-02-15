# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.dealer

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.onboarding

class Dealer(object):

    """Implementation of the 'Dealer' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        customer_number (int): TODO: type description here.
        mva_number (string): TODO: type description here.
        company_phone (string): TODO: type description here.
        company_email (string): TODO: type description here.
        company_url (string): TODO: type description here.
        onboarding (Onboarding): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'Id',
        "name":'Name',
        "customer_number":'CustomerNumber',
        "mva_number":'MvaNumber',
        "company_phone":'CompanyPhone',
        "company_email":'CompanyEmail',
        "company_url":'CompanyUrl',
        "onboarding":'Onboarding'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 customer_number=None,
                 mva_number=None,
                 company_phone=None,
                 company_email=None,
                 company_url=None,
                 onboarding=None,
                 additional_properties = {}):
        """Constructor for the Dealer class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.customer_number = customer_number
        self.mva_number = mva_number
        self.company_phone = company_phone
        self.company_email = company_email
        self.company_url = company_url
        self.onboarding = onboarding

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
        id = dictionary.get('Id')
        name = dictionary.get('Name')
        customer_number = dictionary.get('CustomerNumber')
        mva_number = dictionary.get('MvaNumber')
        company_phone = dictionary.get('CompanyPhone')
        company_email = dictionary.get('CompanyEmail')
        company_url = dictionary.get('CompanyUrl')
        onboarding = idfy_rest_client.models.onboarding.Onboarding.from_dictionary(dictionary.get('Onboarding')) if dictionary.get('Onboarding') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   customer_number,
                   mva_number,
                   company_phone,
                   company_email,
                   company_url,
                   onboarding,
                   dictionary)


