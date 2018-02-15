# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_rights

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.signature_object

class SignatureRights(object):

    """Implementation of the 'SignatureRights' model.

    TODO: type model description here.

    Attributes:
        mva_number (int): TODO: type description here.
        name (string): TODO: type description here.
        signatur (SignatureObject): TODO: type description here.
        prokura (SignatureObject): TODO: type description here.
        report (string): TODO: type description here.
        request_id (string): TODO: type description here.
        report_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mva_number":'MvaNumber',
        "name":'Name',
        "signatur":'Signatur',
        "prokura":'Prokura',
        "report":'Report',
        "request_id":'RequestId',
        "report_id":'ReportId'
    }

    def __init__(self,
                 mva_number=None,
                 name=None,
                 signatur=None,
                 prokura=None,
                 report=None,
                 request_id=None,
                 report_id=None,
                 additional_properties = {}):
        """Constructor for the SignatureRights class"""

        # Initialize members of the class
        self.mva_number = mva_number
        self.name = name
        self.signatur = signatur
        self.prokura = prokura
        self.report = report
        self.request_id = request_id
        self.report_id = report_id

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
        mva_number = dictionary.get('MvaNumber')
        name = dictionary.get('Name')
        signatur = idfy_rest_client.models.signature_object.SignatureObject.from_dictionary(dictionary.get('Signatur')) if dictionary.get('Signatur') else None
        prokura = idfy_rest_client.models.signature_object.SignatureObject.from_dictionary(dictionary.get('Prokura')) if dictionary.get('Prokura') else None
        report = dictionary.get('Report')
        request_id = dictionary.get('RequestId')
        report_id = dictionary.get('ReportId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mva_number,
                   name,
                   signatur,
                   prokura,
                   report,
                   request_id,
                   report_id,
                   dictionary)


