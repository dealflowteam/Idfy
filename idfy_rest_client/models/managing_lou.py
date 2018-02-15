# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.managing_lou

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper

class ManagingLou(object):

    """Implementation of the 'ManagingLou' model.

    TODO: type model description here.

    Attributes:
        lei (string): TODO: type description here.
        prefix (string): TODO: type description here.
        name (string): TODO: type description here.
        website (string): TODO: type description here.
        operational (string): TODO: type description here.
        endorsement_date (datetime): TODO: type description here.
        sponsor (string): TODO: type description here.
        sponsor_country (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lei":'Lei',
        "prefix":'Prefix',
        "name":'Name',
        "website":'Website',
        "operational":'Operational',
        "endorsement_date":'EndorsementDate',
        "sponsor":'Sponsor',
        "sponsor_country":'SponsorCountry'
    }

    def __init__(self,
                 lei=None,
                 prefix=None,
                 name=None,
                 website=None,
                 operational=None,
                 endorsement_date=None,
                 sponsor=None,
                 sponsor_country=None,
                 additional_properties = {}):
        """Constructor for the ManagingLou class"""

        # Initialize members of the class
        self.lei = lei
        self.prefix = prefix
        self.name = name
        self.website = website
        self.operational = operational
        self.endorsement_date = APIHelper.RFC3339DateTime(endorsement_date) if endorsement_date else None
        self.sponsor = sponsor
        self.sponsor_country = sponsor_country

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
        lei = dictionary.get('Lei')
        prefix = dictionary.get('Prefix')
        name = dictionary.get('Name')
        website = dictionary.get('Website')
        operational = dictionary.get('Operational')
        endorsement_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("EndorsementDate")).datetime if dictionary.get("EndorsementDate") else None
        sponsor = dictionary.get('Sponsor')
        sponsor_country = dictionary.get('SponsorCountry')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(lei,
                   prefix,
                   name,
                   website,
                   operational,
                   endorsement_date,
                   sponsor,
                   sponsor_country,
                   dictionary)


