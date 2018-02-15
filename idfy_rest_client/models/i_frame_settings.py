# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.i_frame_settings

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class IFrameSettings(object):

    """Implementation of the 'iFrameSettings' model.

    iFrame settings
    REMARK! If using iframe the parent site have to be on https

    Attributes:
        domain (string): The domain of the site hosting the iFrame, this is
            used for the CSP policy and must be correct.
        web_messaging (bool): Should WebMessaging be used for redirect of the
            iFrame parent, modern browsers have some issues with childs
            redirecting parents without the same origin. To use this include
            this script:
            https://signerecommon.blob.core.windows.net/files/signereid_webmess
            aging.js
        height (int): Height of the frame when used in iFrame.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'Domain',
        "web_messaging":'WebMessaging',
        "height":'Height'
    }

    def __init__(self,
                 domain=None,
                 web_messaging=None,
                 height=None,
                 additional_properties = {}):
        """Constructor for the IFrameSettings class"""

        # Initialize members of the class
        self.domain = domain
        self.web_messaging = web_messaging
        self.height = height

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
        domain = dictionary.get('Domain')
        web_messaging = dictionary.get('WebMessaging')
        height = dictionary.get('Height')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(domain,
                   web_messaging,
                   height,
                   dictionary)


