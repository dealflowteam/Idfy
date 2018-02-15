# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.redirect_settings

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class RedirectSettings(object):

    """Implementation of the 'RedirectSettings' model.

    TODO: type model description here.

    Attributes:
        redirect_mode (RedirectMode): Define if you want redirect or
            webmessaging or both
        domain (string): The domain your website is hosted on  <span
            style="color: red;">Required if you specify iframe on any of the
            signers</span>)
        error (string): The signer is returned to this url if something goes
            wrong. <span style="color: red;">Required if you specify redirect
            on any of the signers </span>
        cancel (string): The signer is returned to this url if the signing has
            been canceled  <span style="color: red;">Required if you specify
            redirect on any of the signers </span>
        success (string): The signer is returned to this url after a
            successfull signing  <span style="color: red;">Required if you
            specify redirect on any of the signers </span>

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "redirect_mode":'redirectMode',
        "domain":'domain',
        "error":'error',
        "cancel":'cancel',
        "success":'success'
    }

    def __init__(self,
                 redirect_mode=None,
                 domain=None,
                 error=None,
                 cancel=None,
                 success=None,
                 additional_properties = {}):
        """Constructor for the RedirectSettings class"""

        # Initialize members of the class
        self.redirect_mode = redirect_mode
        self.domain = domain
        self.error = error
        self.cancel = cancel
        self.success = success

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
        redirect_mode = dictionary.get('redirectMode')
        domain = dictionary.get('domain')
        error = dictionary.get('error')
        cancel = dictionary.get('cancel')
        success = dictionary.get('success')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(redirect_mode,
                   domain,
                   error,
                   cancel,
                   success,
                   dictionary)


