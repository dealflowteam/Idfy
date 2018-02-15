# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.contact

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class Contact(object):

    """Implementation of the 'Contact' model.

    Company contact person

    Attributes:
        name (string): TODO: type description here.
        mobile (string): TODO: type description here.
        email (string): TODO: type description here.
        phone (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'Name',
        "mobile":'Mobile',
        "email":'Email',
        "phone":'Phone'
    }

    def __init__(self,
                 name=None,
                 mobile=None,
                 email=None,
                 phone=None,
                 additional_properties = {}):
        """Constructor for the Contact class"""

        # Initialize members of the class
        self.name = name
        self.mobile = mobile
        self.email = email
        self.phone = phone

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
        name = dictionary.get('Name')
        mobile = dictionary.get('Mobile')
        email = dictionary.get('Email')
        phone = dictionary.get('Phone')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   mobile,
                   email,
                   phone,
                   dictionary)


