# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.labels

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Labels(object):

    """Implementation of the 'Labels' model.

    TODO: type model description here.

    Attributes:
        en (dict<object, string>): TODO: type description here.
        no (dict<object, string>): TODO: type description here.
        sv (dict<object, string>): TODO: type description here.
        da (dict<object, string>): TODO: type description here.
        fi (dict<object, string>): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "en":'en',
        "no":'no',
        "sv":'sv',
        "da":'da',
        "fi":'fi'
    }

    def __init__(self,
                 en=None,
                 no=None,
                 sv=None,
                 da=None,
                 fi=None,
                 additional_properties = {}):
        """Constructor for the Labels class"""

        # Initialize members of the class
        self.en = en
        self.no = no
        self.sv = sv
        self.da = da
        self.fi = fi

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
        en = dictionary.get('en')
        no = dictionary.get('no')
        sv = dictionary.get('sv')
        da = dictionary.get('da')
        fi = dictionary.get('fi')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(en,
                   no,
                   sv,
                   da,
                   fi,
                   dictionary)


