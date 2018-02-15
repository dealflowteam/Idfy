# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.status_201

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Status201(object):

    """Implementation of the 'Status201' model.

    TODO: type model description here.

    Attributes:
        document_status (DocumentStatus): The overall status for the document
        completed_packages (list of CompletedPackage): A list of all the
            completed files/packages on this document.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_status":'documentStatus',
        "completed_packages":'completedPackages'
    }

    def __init__(self,
                 document_status=None,
                 completed_packages=None,
                 additional_properties = {}):
        """Constructor for the Status201 class"""

        # Initialize members of the class
        self.document_status = document_status
        self.completed_packages = completed_packages

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
        document_status = dictionary.get('documentStatus')
        completed_packages = dictionary.get('completedPackages')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(document_status,
                   completed_packages,
                   dictionary)


