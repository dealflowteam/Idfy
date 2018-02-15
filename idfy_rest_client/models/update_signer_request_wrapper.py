# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.update_signer_request_wrapper

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.redirect_settings
import idfy_rest_client.models.signer_info
import idfy_rest_client.models.extra_info_signer_request
import idfy_rest_client.models.ui
import idfy_rest_client.models.notifications

class UpdateSignerRequestWrapper(object):

    """Implementation of the 'UpdateSignerRequestWrapper' model.

    TODO: type model description here.

    Attributes:
        redirect_settings (RedirectSettings): Return urls and domain settings
        signer_info (SignerInfo): Define the signers name, mobile and email if
            you are using notifications
        extra_info (ExtraInfoSignerRequest): Coming soon: Do you want to
            collect extra info about this specific signer? (for example
            personal information)
        ui (UI): Here you can set language, styling and create dialogs the
            signer have to read before/after the signing
        notifications (Notifications): Enable / setup email/sms notifications
            for this specific signer
        tags (list of string): Signer tags
        order (int): You can define a specific sign order /queue for the
            signers if you want to.
        required (bool): If some of the signers are marked as required, the
            other signers are not allowed to sign before the required ones
            have signed the document
        sign_url_expires (datetime): How long before the signers url should
            expire? (ISO 8601). This can be set if you only want a limited
            time to live for each sign url (If you generate a new url at a
            later time this will also have this limited lifetime). Defaults to
            the document lifetime.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "redirect_settings":'redirectSettings',
        "signer_info":'signerInfo',
        "extra_info":'extraInfo',
        "ui":'ui',
        "notifications":'notifications',
        "tags":'tags',
        "order":'order',
        "required":'required',
        "sign_url_expires":'signUrlExpires'
    }

    def __init__(self,
                 redirect_settings=None,
                 signer_info=None,
                 extra_info=None,
                 ui=None,
                 notifications=None,
                 tags=None,
                 order=None,
                 required=None,
                 sign_url_expires=None,
                 additional_properties = {}):
        """Constructor for the UpdateSignerRequestWrapper class"""

        # Initialize members of the class
        self.redirect_settings = redirect_settings
        self.signer_info = signer_info
        self.extra_info = extra_info
        self.ui = ui
        self.notifications = notifications
        self.tags = tags
        self.order = order
        self.required = required
        self.sign_url_expires = APIHelper.RFC3339DateTime(sign_url_expires) if sign_url_expires else None

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
        redirect_settings = idfy_rest_client.models.redirect_settings.RedirectSettings.from_dictionary(dictionary.get('redirectSettings')) if dictionary.get('redirectSettings') else None
        signer_info = idfy_rest_client.models.signer_info.SignerInfo.from_dictionary(dictionary.get('signerInfo')) if dictionary.get('signerInfo') else None
        extra_info = idfy_rest_client.models.extra_info_signer_request.ExtraInfoSignerRequest.from_dictionary(dictionary.get('extraInfo')) if dictionary.get('extraInfo') else None
        ui = idfy_rest_client.models.ui.UI.from_dictionary(dictionary.get('ui')) if dictionary.get('ui') else None
        notifications = idfy_rest_client.models.notifications.Notifications.from_dictionary(dictionary.get('notifications')) if dictionary.get('notifications') else None
        tags = dictionary.get('tags')
        order = dictionary.get('order')
        required = dictionary.get('required')
        sign_url_expires = APIHelper.RFC3339DateTime.from_value(dictionary.get("signUrlExpires")).datetime if dictionary.get("signUrlExpires") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(redirect_settings,
                   signer_info,
                   extra_info,
                   ui,
                   notifications,
                   tags,
                   order,
                   required,
                   sign_url_expires,
                   dictionary)


