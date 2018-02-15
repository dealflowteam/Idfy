# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.search_result

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.lei_record

class SearchResult(object):

    """Implementation of the 'SearchResult' model.

    TODO: type model description here.

    Attributes:
        next_url (string): TODO: type description here.
        start (int): TODO: type description here.
        num_found (int): TODO: type description here.
        rows (int): TODO: type description here.
        results (list of LeiRecord): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "next_url":'next_url',
        "start":'Start',
        "num_found":'NumFound',
        "rows":'Rows',
        "results":'Results'
    }

    def __init__(self,
                 next_url=None,
                 start=None,
                 num_found=None,
                 rows=None,
                 results=None,
                 additional_properties = {}):
        """Constructor for the SearchResult class"""

        # Initialize members of the class
        self.next_url = next_url
        self.start = start
        self.num_found = num_found
        self.rows = rows
        self.results = results

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
        next_url = dictionary.get('next_url')
        start = dictionary.get('Start')
        num_found = dictionary.get('NumFound')
        rows = dictionary.get('Rows')
        results = None
        if dictionary.get('Results') != None:
            results = list()
            for structure in dictionary.get('Results'):
                results.append(idfy_rest_client.models.lei_record.LeiRecord.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(next_url,
                   start,
                   num_found,
                   rows,
                   results,
                   dictionary)


