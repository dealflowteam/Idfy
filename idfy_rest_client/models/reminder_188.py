# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.reminder_188

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.email
import idfy_rest_client.models.sms

class Reminder188(object):

    """Implementation of the 'Reminder188' model.

    Here you can setup email/sms notifications reminding the signers that they
    have unsigned documents.

    Attributes:
        chron_schedule (string): Define a chron expression to control the
            interval of the reminders (Use utc time). We use quartz cron
            expressions, read more about it here:
            http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/
            crontrigger.html.
        max_reminders (int): Set the maximum number of reminders to be sent
            for each signer
        email (list of Email): Define your own email texts (Our default texts
            can be used by leaving this blank)
        sms (list of SMS): Define your own sms texts (Our default texts can be
            used by leaving this blank)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chron_schedule":'chronSchedule',
        "max_reminders":'maxReminders',
        "email":'email',
        "sms":'sms'
    }

    def __init__(self,
                 chron_schedule=None,
                 max_reminders=None,
                 email=None,
                 sms=None,
                 additional_properties = {}):
        """Constructor for the Reminder188 class"""

        # Initialize members of the class
        self.chron_schedule = chron_schedule
        self.max_reminders = max_reminders
        self.email = email
        self.sms = sms

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
        chron_schedule = dictionary.get('chronSchedule')
        max_reminders = dictionary.get('maxReminders')
        email = None
        if dictionary.get('email') != None:
            email = list()
            for structure in dictionary.get('email'):
                email.append(idfy_rest_client.models.email.Email.from_dictionary(structure))
        sms = None
        if dictionary.get('sms') != None:
            sms = list()
            for structure in dictionary.get('sms'):
                sms.append(idfy_rest_client.models.sms.SMS.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(chron_schedule,
                   max_reminders,
                   email,
                   sms,
                   dictionary)


