# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.collection_with_paging_document_summary

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.links
import idfy_rest_client.models.document_summary

class CollectionWithPagingDocumentSummary(object):

    """Implementation of the 'CollectionWithPaging[DocumentSummary]' model.

    TODO: type model description here.

    Attributes:
        offset (int): The offset of the current page.
        limit (int): The limit of the current paging options.
        size (long|int): The total size of the collection (irrespective of any
            paging options).
        links (Links): TODO: type description here.
        data (list of DocumentSummary): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "offset":'offset',
        "limit":'limit',
        "size":'size',
        "links":'links',
        "data":'data'
    }

    def __init__(self,
                 offset=None,
                 limit=None,
                 size=None,
                 links=None,
                 data=None,
                 additional_properties = {}):
        """Constructor for the CollectionWithPagingDocumentSummary class"""

        # Initialize members of the class
        self.offset = offset
        self.limit = limit
        self.size = size
        self.links = links
        self.data = data

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
        offset = dictionary.get('offset')
        limit = dictionary.get('limit')
        size = dictionary.get('size')
        links = idfy_rest_client.models.links.Links.from_dictionary(dictionary.get('links')) if dictionary.get('links') else None
        data = None
        if dictionary.get('data') != None:
            data = list()
            for structure in dictionary.get('data'):
                data.append(idfy_rest_client.models.document_summary.DocumentSummary.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(offset,
                   limit,
                   size,
                   links,
                   data,
                   dictionary)


