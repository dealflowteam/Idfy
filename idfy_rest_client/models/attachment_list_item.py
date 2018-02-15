# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.attachment_list_item

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class AttachmentListItem(object):

    """Implementation of the 'AttachmentListItem' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        title (string): TODO: type description here.
        description (string): TODO: type description here.
        mtype (Type): TODO: type description here.
        file_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "title":'title',
        "description":'description',
        "mtype":'type',
        "file_name":'fileName'
    }

    def __init__(self,
                 id=None,
                 title=None,
                 description=None,
                 mtype=None,
                 file_name=None,
                 additional_properties = {}):
        """Constructor for the AttachmentListItem class"""

        # Initialize members of the class
        self.id = id
        self.title = title
        self.description = description
        self.mtype = mtype
        self.file_name = file_name

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
        id = dictionary.get('id')
        title = dictionary.get('title')
        description = dictionary.get('description')
        mtype = dictionary.get('type')
        file_name = dictionary.get('fileName')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   title,
                   description,
                   mtype,
                   file_name,
                   dictionary)


