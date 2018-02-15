# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.identification_complete_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class IdentificationCompleteResponse(object):

    """Implementation of the 'IdentificationCompleteResponse' model.

    TODO: type model description here.

    Attributes:
        done (bool): Is the idenfication process done?

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "done":'Done'
    }

    def __init__(self,
                 done=None,
                 additional_properties = {}):
        """Constructor for the IdentificationCompleteResponse class"""

        # Initialize members of the class
        self.done = done

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
        done = dictionary.get('Done')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(done,
                   dictionary)


