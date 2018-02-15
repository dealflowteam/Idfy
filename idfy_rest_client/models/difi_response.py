# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.difi_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.company_info_difi_response

class DifiResponse(object):

    """Implementation of the 'DifiResponse' model.

    TODO: type model description here.

    Attributes:
        organizations (list of CompanyInfoDifiResponse): TODO: type
            description here.
        raw_data (string): TODO: type description here.
        request_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "organizations":'Organizations',
        "raw_data":'RawData',
        "request_id":'RequestId'
    }

    def __init__(self,
                 organizations=None,
                 raw_data=None,
                 request_id=None,
                 additional_properties = {}):
        """Constructor for the DifiResponse class"""

        # Initialize members of the class
        self.organizations = organizations
        self.raw_data = raw_data
        self.request_id = request_id

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
        organizations = None
        if dictionary.get('Organizations') != None:
            organizations = list()
            for structure in dictionary.get('Organizations'):
                organizations.append(idfy_rest_client.models.company_info_difi_response.CompanyInfoDifiResponse.from_dictionary(structure))
        raw_data = dictionary.get('RawData')
        request_id = dictionary.get('RequestId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(organizations,
                   raw_data,
                   request_id,
                   dictionary)


