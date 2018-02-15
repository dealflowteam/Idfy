# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.account

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.resources
import idfy_rest_client.models.contact
import idfy_rest_client.models.address
import idfy_rest_client.models.dealer_info
import idfy_rest_client.models.settings

class Account(object):

    """Implementation of the 'Account' model.

    TODO: type model description here.

    Attributes:
        name (string): Name of the account owner (company)
        mva_number (string): Mva / Organization number
        company_phone (string): TODO: type description here.
        company_email (string): TODO: type description here.
        id (uuid|string): Account Id
        customer_number (string): Uni micro customer number
        resources (Resources): Logo / Styling
        company_url (string): TODO: type description here.
        contact (Contact): Company contact person
        address (Address): Company address
        dealer (DealerInfo): Dealer information
        settings (Settings): Other account settings
        country (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'Name',
        "mva_number":'MvaNumber',
        "company_phone":'CompanyPhone',
        "company_email":'CompanyEmail',
        "id":'Id',
        "customer_number":'CustomerNumber',
        "resources":'Resources',
        "company_url":'CompanyUrl',
        "contact":'Contact',
        "address":'Address',
        "dealer":'Dealer',
        "settings":'Settings',
        "country":'Country'
    }

    def __init__(self,
                 name=None,
                 mva_number=None,
                 company_phone=None,
                 company_email=None,
                 id=None,
                 customer_number=None,
                 resources=None,
                 company_url=None,
                 contact=None,
                 address=None,
                 dealer=None,
                 settings=None,
                 country=None,
                 additional_properties = {}):
        """Constructor for the Account class"""

        # Initialize members of the class
        self.name = name
        self.mva_number = mva_number
        self.company_phone = company_phone
        self.company_email = company_email
        self.id = id
        self.customer_number = customer_number
        self.resources = resources
        self.company_url = company_url
        self.contact = contact
        self.address = address
        self.dealer = dealer
        self.settings = settings
        self.country = country

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
        name = dictionary.get('Name')
        mva_number = dictionary.get('MvaNumber')
        company_phone = dictionary.get('CompanyPhone')
        company_email = dictionary.get('CompanyEmail')
        id = dictionary.get('Id')
        customer_number = dictionary.get('CustomerNumber')
        resources = idfy_rest_client.models.resources.Resources.from_dictionary(dictionary.get('Resources')) if dictionary.get('Resources') else None
        company_url = dictionary.get('CompanyUrl')
        contact = idfy_rest_client.models.contact.Contact.from_dictionary(dictionary.get('Contact')) if dictionary.get('Contact') else None
        address = idfy_rest_client.models.address.Address.from_dictionary(dictionary.get('Address')) if dictionary.get('Address') else None
        dealer = idfy_rest_client.models.dealer_info.DealerInfo.from_dictionary(dictionary.get('Dealer')) if dictionary.get('Dealer') else None
        settings = idfy_rest_client.models.settings.Settings.from_dictionary(dictionary.get('Settings')) if dictionary.get('Settings') else None
        country = dictionary.get('Country')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   mva_number,
                   company_phone,
                   company_email,
                   id,
                   customer_number,
                   resources,
                   company_url,
                   contact,
                   address,
                   dealer,
                   settings,
                   country,
                   dictionary)


