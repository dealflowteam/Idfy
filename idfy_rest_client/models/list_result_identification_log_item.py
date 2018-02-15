# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.list_result_identification_log_item

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.identification_log_item

class ListResultIdentificationLogItem(object):

    """Implementation of the 'ListResult[IdentificationLogItem]' model.

    TODO: type model description here.

    Attributes:
        next_link (string): Link to the next results if not set there are less
            then the return limit of 1000
        total_links (int): The total amount of links (pages) for the list
        list (list of IdentificationLogItem): List of results

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "next_link":'NextLink',
        "total_links":'TotalLinks',
        "list":'List'
    }

    def __init__(self,
                 next_link=None,
                 total_links=None,
                 list=None,
                 additional_properties = {}):
        """Constructor for the ListResultIdentificationLogItem class"""

        # Initialize members of the class
        self.next_link = next_link
        self.total_links = total_links
        self.list = list

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
        next_link = dictionary.get('NextLink')
        total_links = dictionary.get('TotalLinks')
        list = None
        if dictionary.get('List') != None:
            list = list()
            for structure in dictionary.get('List'):
                list.append(idfy_rest_client.models.identification_log_item.IdentificationLogItem.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(next_link,
                   total_links,
                   list,
                   dictionary)


