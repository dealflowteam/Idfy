# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.aml_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.sanction_result
import idfy_rest_client.models.pep_result
import idfy_rest_client.models.verified_person

class AmlResponse(object):

    """Implementation of the 'AmlResponse' model.

    TODO: type model description here.

    Attributes:
        bisnode_reference (string): Reference identifying the current request.
            May be used for tracing
        sanction_results (list of SanctionResult): List of all Sanction items
            with match for the input request.
        pep_results (list of PepResult): List of all PEP items with match for
            the input request.
        verified_person (VerifiedPerson): Data retrieved before the actual
            screening (data enhancement).
        message (string): Response message could for example be: No result
            from PEP and/or SANCTION screening.
        report_data (string): Base64 encoded PDF

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bisnode_reference":'bisnodeReference',
        "sanction_results":'sanctionResults',
        "pep_results":'pepResults',
        "verified_person":'VerifiedPerson',
        "message":'message',
        "report_data":'reportData'
    }

    def __init__(self,
                 bisnode_reference=None,
                 sanction_results=None,
                 pep_results=None,
                 verified_person=None,
                 message=None,
                 report_data=None,
                 additional_properties = {}):
        """Constructor for the AmlResponse class"""

        # Initialize members of the class
        self.bisnode_reference = bisnode_reference
        self.sanction_results = sanction_results
        self.pep_results = pep_results
        self.verified_person = verified_person
        self.message = message
        self.report_data = report_data

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
        bisnode_reference = dictionary.get('bisnodeReference')
        sanction_results = None
        if dictionary.get('sanctionResults') != None:
            sanction_results = list()
            for structure in dictionary.get('sanctionResults'):
                sanction_results.append(idfy_rest_client.models.sanction_result.SanctionResult.from_dictionary(structure))
        pep_results = None
        if dictionary.get('pepResults') != None:
            pep_results = list()
            for structure in dictionary.get('pepResults'):
                pep_results.append(idfy_rest_client.models.pep_result.PepResult.from_dictionary(structure))
        verified_person = idfy_rest_client.models.verified_person.VerifiedPerson.from_dictionary(dictionary.get('VerifiedPerson')) if dictionary.get('VerifiedPerson') else None
        message = dictionary.get('message')
        report_data = dictionary.get('reportData')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(bisnode_reference,
                   sanction_results,
                   pep_results,
                   verified_person,
                   message,
                   report_data,
                   dictionary)


