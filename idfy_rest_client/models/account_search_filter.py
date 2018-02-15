# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.account_search_filter

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class AccountSearchFilter(object):

    """Implementation of the 'AccountSearchFilter' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        org_no (string): TODO: type description here.
        uni_customer_no (string): TODO: type description here.
        created_before (datetime): TODO: type description here.
        created_after (datetime): TODO: type description here.
        last_modified_before (datetime): TODO: type description here.
        last_modified_after (datetime): TODO: type description here.
        dealer_name (string): TODO: type description here.
        dealer_reference (string): TODO: type description here.
        enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'Name',
        "org_no":'OrgNo',
        "uni_customer_no":'UniCustomerNo',
        "created_before":'CreatedBefore',
        "created_after":'CreatedAfter',
        "last_modified_before":'LastModifiedBefore',
        "last_modified_after":'LastModifiedAfter',
        "dealer_name":'DealerName',
        "dealer_reference":'DealerReference',
        "enabled":'Enabled'
    }

    def __init__(self,
                 name=None,
                 org_no=None,
                 uni_customer_no=None,
                 created_before=None,
                 created_after=None,
                 last_modified_before=None,
                 last_modified_after=None,
                 dealer_name=None,
                 dealer_reference=None,
                 enabled=None,
                 additional_properties = {}):
        """Constructor for the AccountSearchFilter class"""

        # Initialize members of the class
        self.name = name
        self.org_no = org_no
        self.uni_customer_no = uni_customer_no
        self.created_before = APIHelper.RFC3339DateTime(created_before) if created_before else None
        self.created_after = APIHelper.RFC3339DateTime(created_after) if created_after else None
        self.last_modified_before = APIHelper.RFC3339DateTime(last_modified_before) if last_modified_before else None
        self.last_modified_after = APIHelper.RFC3339DateTime(last_modified_after) if last_modified_after else None
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
        name = dictionary.get('Name')
        org_no = dictionary.get('OrgNo')
        uni_customer_no = dictionary.get('UniCustomerNo')
        created_before = APIHelper.RFC3339DateTime.from_value(dictionary.get("CreatedBefore")).datetime if dictionary.get("CreatedBefore") else None
        created_after = APIHelper.RFC3339DateTime.from_value(dictionary.get("CreatedAfter")).datetime if dictionary.get("CreatedAfter") else None
        last_modified_before = APIHelper.RFC3339DateTime.from_value(dictionary.get("LastModifiedBefore")).datetime if dictionary.get("LastModifiedBefore") else None
        last_modified_after = APIHelper.RFC3339DateTime.from_value(dictionary.get("LastModifiedAfter")).datetime if dictionary.get("LastModifiedAfter") else None
        dealer_name = dictionary.get('DealerName')
        dealer_reference = dictionary.get('DealerReference')
        enabled = dictionary.get('Enabled')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   org_no,
                   uni_customer_no,
                   created_before,
                   created_after,
                   last_modified_before,
                   last_modified_after,
                   dealer_name,
                   dealer_reference,
                   enabled,
                   dictionary)


