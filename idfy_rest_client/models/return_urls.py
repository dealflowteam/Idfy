# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.return_urls

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class ReturnUrls(object):

    """Implementation of the 'ReturnUrls' model.

    Return urls for the identity request

    Attributes:
        error (string): The url to be redirected to if the identification
            process fails. This url supports the following placeholders: [0]
            statuscode, [1] requestId, [2] ExternalReference (your unique
            id).
        abort (string): The url to be redirected to if the user aborts the
            identification process. This url supports the following
            placeholders: [1] requestId, [2] ExternalReference (your unique
            id).
        success (string): The return urls to be redirected to after the
            identification process is a success. This url supports the
            following placeholders: [1] requestId, [2] ExternalReference (your
            unique id).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'Error',
        "abort":'Abort',
        "success":'Success'
    }

    def __init__(self,
                 error=None,
                 abort=None,
                 success=None,
                 additional_properties = {}):
        """Constructor for the ReturnUrls class"""

        # Initialize members of the class
        self.error = error
        self.abort = abort
        self.success = success

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
        error = dictionary.get('Error')
        abort = dictionary.get('Abort')
        success = dictionary.get('Success')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(error,
                   abort,
                   success,
                   dictionary)


