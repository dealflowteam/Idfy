# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.notification_log_item

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class NotificationLogItem(object):

    """Implementation of the 'NotificationLogItem' model.

    TODO: type model description here.

    Attributes:
        sent_time_stamp (string): TODO: type description here.
        title (string): TODO: type description here.
        text (string): TODO: type description here.
        message_type (string): TODO: type description here.
        status (string): TODO: type description here.
        from_address (string): TODO: type description here.
        receiver (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sent_time_stamp":'sentTimeStamp',
        "title":'title',
        "text":'text',
        "message_type":'messageType',
        "status":'status',
        "from_address":'fromAddress',
        "receiver":'receiver'
    }

    def __init__(self,
                 sent_time_stamp=None,
                 title=None,
                 text=None,
                 message_type=None,
                 status=None,
                 from_address=None,
                 receiver=None,
                 additional_properties = {}):
        """Constructor for the NotificationLogItem class"""

        # Initialize members of the class
        self.sent_time_stamp = sent_time_stamp
        self.title = title
        self.text = text
        self.message_type = message_type
        self.status = status
        self.from_address = from_address
        self.receiver = receiver

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
        sent_time_stamp = dictionary.get('sentTimeStamp')
        title = dictionary.get('title')
        text = dictionary.get('text')
        message_type = dictionary.get('messageType')
        status = dictionary.get('status')
        from_address = dictionary.get('fromAddress')
        receiver = dictionary.get('receiver')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(sent_time_stamp,
                   title,
                   text,
                   message_type,
                   status,
                   from_address,
                   receiver,
                   dictionary)


