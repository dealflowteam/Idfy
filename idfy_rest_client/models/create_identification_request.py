# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.create_identification_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.return_urls
import idfy_rest_client.models.i_frame_settings

class CreateIdentificationRequest(object):

    """Implementation of the 'CreateIdentificationRequest' model.

    Creates a Identity request

    Attributes:
        return_urls (ReturnUrls): The return urls to be redirected to after
            the identification process is done
        identity_provider (IdentityProvider): The identityprovider to use for
            the identification, if not set the user will get a list of all the
            e-ID assosiated with your account to choose from.
        i_frame (IFrameSettings): If the identity process should be done in an
            iframe this settings object would have to set. The redirect is
            then done in javascript.
        language (Language): The language to be used for the identification
            process, if not set the language of the users browser will be
            used.
        get_social_security_number (bool): Should the socialsecuritynumber be
            fetched from the identityprovider? Beware that there is an extra
            cost of doing this every time and one need permission to do it.
        pre_filled_social_security_number (string): If this is specified then
            the client will be prefilled with this value. (supported by
            Norwegian BankID, NemID and Tupas)
        page_title (string): Title of the identification page (Used when
            redirecting on larger devices). Not used in iFrame mode
        external_reference (string): The merchants reference to the
            identification process, this will also be used to identify an
            identification in a detailed invoice. It is an advantage if this
            is unique for each API call.
        addonservices (dict<object, string>): List of addon data that can be
            orderd. The result will be in MetaData list of the reponse

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "return_urls":'ReturnUrls',
        "identity_provider":'IdentityProvider',
        "i_frame":'iFrame',
        "language":'Language',
        "get_social_security_number":'GetSocialSecurityNumber',
        "pre_filled_social_security_number":'PreFilledSocialSecurityNumber',
        "page_title":'PageTitle',
        "external_reference":'ExternalReference',
        "addonservices":'Addonservices'
    }

    def __init__(self,
                 return_urls=None,
                 identity_provider=None,
                 i_frame=None,
                 language=None,
                 get_social_security_number=None,
                 pre_filled_social_security_number=None,
                 page_title=None,
                 external_reference=None,
                 addonservices=None,
                 additional_properties = {}):
        """Constructor for the CreateIdentificationRequest class"""

        # Initialize members of the class
        self.return_urls = return_urls
        self.identity_provider = identity_provider
        self.i_frame = i_frame
        self.language = language
        self.get_social_security_number = get_social_security_number
        self.pre_filled_social_security_number = pre_filled_social_security_number
        self.page_title = page_title
        self.external_reference = external_reference
        self.addonservices = addonservices

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
        return_urls = idfy_rest_client.models.return_urls.ReturnUrls.from_dictionary(dictionary.get('ReturnUrls')) if dictionary.get('ReturnUrls') else None
        identity_provider = dictionary.get('IdentityProvider')
        i_frame = idfy_rest_client.models.i_frame_settings.IFrameSettings.from_dictionary(dictionary.get('iFrame')) if dictionary.get('iFrame') else None
        language = dictionary.get('Language')
        get_social_security_number = dictionary.get('GetSocialSecurityNumber')
        pre_filled_social_security_number = dictionary.get('PreFilledSocialSecurityNumber')
        page_title = dictionary.get('PageTitle')
        external_reference = dictionary.get('ExternalReference')
        addonservices = dictionary.get('Addonservices')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(return_urls,
                   identity_provider,
                   i_frame,
                   language,
                   get_social_security_number,
                   pre_filled_social_security_number,
                   page_title,
                   external_reference,
                   addonservices,
                   dictionary)


