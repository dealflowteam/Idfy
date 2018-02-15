# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signer_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.redirect_settings
import idfy_rest_client.models.signature_type
import idfy_rest_client.models.document_signature
import idfy_rest_client.models.extra_info_signer_response
import idfy_rest_client.models.signer_info
import idfy_rest_client.models.authentication
import idfy_rest_client.models.ui
import idfy_rest_client.models.notifications

class SignerResponse(object):

    """Implementation of the 'SignerResponse' model.

    TODO: type model description here.

    Attributes:
        external_signer_id (string): Your reference for the signer
        redirect_settings (RedirectSettings): Return urls and domain settings
        signature_type (SignatureType): TODO: type description here.
        id (uuid|string): Signer Id
        url (string): This is the url that the signer should use to sign the
            document
        document_signature (DocumentSignature): This property will get it's
            values when the signing is done, it contains name, date of birth
            of the signer and mroe.
        meta_data (dict<object, string>): A dicitonary with extra information
            from each identityprovider, and extra services. See developer
            documentation for more information
        extra_info (ExtraInfoSignerResponse): Extra info about the signer as
            requested
        signer_info (SignerInfo): Define the signers name, mobile and email if
            you are using notifications
        authentication (Authentication): Do you want the signer to
            authenticate before they can see the document?
        ui (UI): Here you can set language, styling and create dialogs the
            signer have to read before/after the signing
        notifications (Notifications): Enable and setup email/sms
            notifications for this specific signer
        tags (list of string): Coming soon
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
        "external_signer_id":'externalSignerId',
        "redirect_settings":'redirectSettings',
        "signature_type":'signatureType',
        "id":'id',
        "url":'url',
        "document_signature":'documentSignature',
        "meta_data":'metaData',
        "extra_info":'extraInfo',
        "signer_info":'signerInfo',
        "authentication":'authentication',
        "ui":'ui',
        "notifications":'notifications',
        "tags":'tags',
        "order":'order',
        "required":'required',
        "sign_url_expires":'signUrlExpires'
    }

    def __init__(self,
                 external_signer_id=None,
                 redirect_settings=None,
                 signature_type=None,
                 id=None,
                 url=None,
                 document_signature=None,
                 meta_data=None,
                 extra_info=None,
                 signer_info=None,
                 authentication=None,
                 ui=None,
                 notifications=None,
                 tags=None,
                 order=None,
                 required=None,
                 sign_url_expires=None,
                 additional_properties = {}):
        """Constructor for the SignerResponse class"""

        # Initialize members of the class
        self.external_signer_id = external_signer_id
        self.redirect_settings = redirect_settings
        self.signature_type = signature_type
        self.id = id
        self.url = url
        self.document_signature = document_signature
        self.meta_data = meta_data
        self.extra_info = extra_info
        self.signer_info = signer_info
        self.authentication = authentication
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
        external_signer_id = dictionary.get('externalSignerId')
        redirect_settings = idfy_rest_client.models.redirect_settings.RedirectSettings.from_dictionary(dictionary.get('redirectSettings')) if dictionary.get('redirectSettings') else None
        signature_type = idfy_rest_client.models.signature_type.SignatureType.from_dictionary(dictionary.get('signatureType')) if dictionary.get('signatureType') else None
        id = dictionary.get('id')
        url = dictionary.get('url')
        document_signature = idfy_rest_client.models.document_signature.DocumentSignature.from_dictionary(dictionary.get('documentSignature')) if dictionary.get('documentSignature') else None
        meta_data = dictionary.get('metaData')
        extra_info = idfy_rest_client.models.extra_info_signer_response.ExtraInfoSignerResponse.from_dictionary(dictionary.get('extraInfo')) if dictionary.get('extraInfo') else None
        signer_info = idfy_rest_client.models.signer_info.SignerInfo.from_dictionary(dictionary.get('signerInfo')) if dictionary.get('signerInfo') else None
        authentication = idfy_rest_client.models.authentication.Authentication.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None
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
        return cls(external_signer_id,
                   redirect_settings,
                   signature_type,
                   id,
                   url,
                   document_signature,
                   meta_data,
                   extra_info,
                   signer_info,
                   authentication,
                   ui,
                   notifications,
                   tags,
                   order,
                   required,
                   sign_url_expires,
                   dictionary)


