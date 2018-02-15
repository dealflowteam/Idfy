# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.create_bank_id_mobile_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.error

class CreateBankIDMobileResponse(object):

    """Implementation of the 'CreateBankIDMobileResponse' model.

    The reponse of the create BankID mobile request

    Attributes:
        request_id (string): Signere requestid used to get the reponse form
            server afterwards
        merchant_ref (string): The merchant ref to show to the end user (SNILL
            BANK)
        error (Error): Information about error if the identification process
            failed. (Only set if an error occured, if not is null)
        ok (bool): Status if the request started without errors
        invalid_mobile_number_or_date_of_birth (bool): Indicates if the Mobile
            number of the date of birth was invalid. These could be 2 things: 
            1 the user does not have BankID mobile,   2. Wrong input data (the
            combination of mobile and date of birth does not match

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id":'RequestId',
        "merchant_ref":'MerchantRef',
        "error":'Error',
        "ok":'OK',
        "invalid_mobile_number_or_date_of_birth":'InvalidMobileNumberOrDateOfBirth'
    }

    def __init__(self,
                 request_id=None,
                 merchant_ref=None,
                 error=None,
                 ok=None,
                 invalid_mobile_number_or_date_of_birth=None,
                 additional_properties = {}):
        """Constructor for the CreateBankIDMobileResponse class"""

        # Initialize members of the class
        self.request_id = request_id
        self.merchant_ref = merchant_ref
        self.error = error
        self.ok = ok
        self.invalid_mobile_number_or_date_of_birth = invalid_mobile_number_or_date_of_birth

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
        request_id = dictionary.get('RequestId')
        merchant_ref = dictionary.get('MerchantRef')
        error = idfy_rest_client.models.error.Error.from_dictionary(dictionary.get('Error')) if dictionary.get('Error') else None
        ok = dictionary.get('OK')
        invalid_mobile_number_or_date_of_birth = dictionary.get('InvalidMobileNumberOrDateOfBirth')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(request_id,
                   merchant_ref,
                   error,
                   ok,
                   invalid_mobile_number_or_date_of_birth,
                   dictionary)


