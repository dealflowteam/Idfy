# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.create_identification_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class CreateIdentificationResponse(object):

    """Implementation of the 'CreateIdentificationResponse' model.

    The response of the Create Identitiy request

    Attributes:
        url (string): The url to use as src for iframe or to redirect the user
            to
        request_id (string): Requestid used to get the reponse form server
            afterwards

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'Url',
        "request_id":'RequestId'
    }

    def __init__(self,
                 url=None,
                 request_id=None,
                 additional_properties = {}):
        """Constructor for the CreateIdentificationResponse class"""

        # Initialize members of the class
        self.url = url
        self.request_id = request_id

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
        url = dictionary.get('Url')
        request_id = dictionary.get('RequestId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(url,
                   request_id,
                   dictionary)


