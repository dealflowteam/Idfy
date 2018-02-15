# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.account_list_item

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class AccountListItem(object):

    """Implementation of the 'AccountListItem' model.

    TODO: type model description here.

    Attributes:
        account_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        org_no (string): TODO: type description here.
        uni_customer_no (string): TODO: type description here.
        created (datetime): TODO: type description here.
        last_modified (datetime): TODO: type description here.
        dealer_id (string): TODO: type description here.
        dealer_name (string): TODO: type description here.
        dealer_reference (string): TODO: type description here.
        enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'AccountId',
        "name":'Name',
        "org_no":'OrgNo',
        "uni_customer_no":'UniCustomerNo',
        "created":'Created',
        "last_modified":'LastModified',
        "dealer_id":'DealerId',
        "dealer_name":'DealerName',
        "dealer_reference":'DealerReference',
        "enabled":'Enabled'
    }

    def __init__(self,
                 account_id=None,
                 name=None,
                 org_no=None,
                 uni_customer_no=None,
                 created=None,
                 last_modified=None,
                 dealer_id=None,
                 dealer_name=None,
                 dealer_reference=None,
                 enabled=None,
                 additional_properties = {}):
        """Constructor for the AccountListItem class"""

        # Initialize members of the class
        self.account_id = account_id
        self.name = name
        self.org_no = org_no
        self.uni_customer_no = uni_customer_no
        self.created = APIHelper.RFC3339DateTime(created) if created else None
        self.last_modified = APIHelper.RFC3339DateTime(last_modified) if last_modified else None
        self.dealer_id = dealer_id
        self.dealer_name = dealer_name
        self.dealer_reference = dealer_reference
        self.enabled = enabled

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
        account_id = dictionary.get('AccountId')
        name = dictionary.get('Name')
        org_no = dictionary.get('OrgNo')
        uni_customer_no = dictionary.get('UniCustomerNo')
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("Created")).datetime if dictionary.get("Created") else None
        last_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("LastModified")).datetime if dictionary.get("LastModified") else None
        dealer_id = dictionary.get('DealerId')
        dealer_name = dictionary.get('DealerName')
        dealer_reference = dictionary.get('DealerReference')
        enabled = dictionary.get('Enabled')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_id,
                   name,
                   org_no,
                   uni_customer_no,
                   created,
                   last_modified,
                   dealer_id,
                   dealer_name,
                   dealer_reference,
                   enabled,
                   dictionary)


