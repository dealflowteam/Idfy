# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.update_document_request_wrapper

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.notification
import idfy_rest_client.models.contact_details
import idfy_rest_client.models.advanced

class UpdateDocumentRequestWrapper(object):

    """Implementation of the 'UpdateDocumentRequestWrapper' model.

    TODO: type model description here.

    Attributes:
        title (string): TODO: type description here.
        description (string): TODO: type description here.
        notification (Notification): Setup your own notification texts, and
            specify specail settings. Info: you also has to setup
            notifications on the signers you want to notify.
        contact_details (ContactDetails): TODO: type description here.
        advanced (Advanced): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title":'title',
        "description":'description',
        "notification":'notification',
        "contact_details":'contactDetails',
        "advanced":'advanced'
    }

    def __init__(self,
                 title=None,
                 description=None,
                 notification=None,
                 contact_details=None,
                 advanced=None,
                 additional_properties = {}):
        """Constructor for the UpdateDocumentRequestWrapper class"""

        # Initialize members of the class
        self.title = title
        self.description = description
        self.notification = notification
        self.contact_details = contact_details
        self.advanced = advanced

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
        title = dictionary.get('title')
        description = dictionary.get('description')
        notification = idfy_rest_client.models.notification.Notification.from_dictionary(dictionary.get('notification')) if dictionary.get('notification') else None
        contact_details = idfy_rest_client.models.contact_details.ContactDetails.from_dictionary(dictionary.get('contactDetails')) if dictionary.get('contactDetails') else None
        advanced = idfy_rest_client.models.advanced.Advanced.from_dictionary(dictionary.get('advanced')) if dictionary.get('advanced') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(title,
                   description,
                   notification,
                   contact_details,
                   advanced,
                   dictionary)


