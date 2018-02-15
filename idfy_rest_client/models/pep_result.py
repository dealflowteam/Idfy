# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.pep_result

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.address_list

class PepResult(object):

    """Implementation of the 'PepResult' model.

    List of all PEP items with match for the input request.

    Attributes:
        match_indicator (int): Quality indicator of match. Higher number means
            better match.
        title (string): May be a text string denoting title of position, job
            title, etc
        function (string): Additional details about what the person does
        comment (string): A comment of some kind may be present in some lists
        alias_list (list of string): Name aliases for the person. May be none,
            one or more.
        address_list (list of AddressList): List of addresses found in the
            lists
        url_list (list of string): URLs to source documents (May be used for
            further investigations)
        provider (string): Name of data provider
        source (string): The name of the source list, e.g. 'EU_GLOBAL',
            'PEP_Edge', 'UN_CONSOLIDATED'
        external_id (string): External identification
        last_update (datetime): Date of last update
        first_update (datetime): Date of first update
        name (string): Name of person
        gender (Gender): Gender of person
        nat_id_no (string): National Identification Number
        nationality (string): Two-letter code as specified in the ISO 3166
            standard
        birth_date (string): Date of birth for the person

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "match_indicator":'matchIndicator',
        "title":'title',
        "function":'function',
        "comment":'comment',
        "alias_list":'aliasList',
        "address_list":'addressList',
        "url_list":'urlList',
        "provider":'provider',
        "source":'source',
        "external_id":'externalId',
        "last_update":'lastUpdate',
        "first_update":'firstUpdate',
        "name":'name',
        "gender":'gender',
        "nat_id_no":'natIdNo',
        "nationality":'nationality',
        "birth_date":'birthDate'
    }

    def __init__(self,
                 match_indicator=None,
                 title=None,
                 function=None,
                 comment=None,
                 alias_list=None,
                 address_list=None,
                 url_list=None,
                 provider=None,
                 source=None,
                 external_id=None,
                 last_update=None,
                 first_update=None,
                 name=None,
                 gender=None,
                 nat_id_no=None,
                 nationality=None,
                 birth_date=None,
                 additional_properties = {}):
        """Constructor for the PepResult class"""

        # Initialize members of the class
        self.match_indicator = match_indicator
        self.title = title
        self.function = function
        self.comment = comment
        self.alias_list = alias_list
        self.address_list = address_list
        self.url_list = url_list
        self.provider = provider
        self.source = source
        self.external_id = external_id
        self.last_update = APIHelper.RFC3339DateTime(last_update) if last_update else None
        self.first_update = APIHelper.RFC3339DateTime(first_update) if first_update else None
        self.name = name
        self.gender = gender
        self.nat_id_no = nat_id_no
        self.nationality = nationality
        self.birth_date = birth_date

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
        match_indicator = dictionary.get('matchIndicator')
        title = dictionary.get('title')
        function = dictionary.get('function')
        comment = dictionary.get('comment')
        alias_list = dictionary.get('aliasList')
        address_list = None
        if dictionary.get('addressList') != None:
            address_list = list()
            for structure in dictionary.get('addressList'):
                address_list.append(idfy_rest_client.models.address_list.AddressList.from_dictionary(structure))
        url_list = dictionary.get('urlList')
        provider = dictionary.get('provider')
        source = dictionary.get('source')
        external_id = dictionary.get('externalId')
        last_update = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastUpdate")).datetime if dictionary.get("lastUpdate") else None
        first_update = APIHelper.RFC3339DateTime.from_value(dictionary.get("firstUpdate")).datetime if dictionary.get("firstUpdate") else None
        name = dictionary.get('name')
        gender = dictionary.get('gender')
        nat_id_no = dictionary.get('natIdNo')
        nationality = dictionary.get('nationality')
        birth_date = dictionary.get('birthDate')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(match_indicator,
                   title,
                   function,
                   comment,
                   alias_list,
                   address_list,
                   url_list,
                   provider,
                   source,
                   external_id,
                   last_update,
                   first_update,
                   name,
                   gender,
                   nat_id_no,
                   nationality,
                   birth_date,
                   dictionary)


