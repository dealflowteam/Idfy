# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.advanced_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.extra_info_document_response
import idfy_rest_client.models.security
import idfy_rest_client.models.time_to_live

class AdvancedResponse(object):

    """Implementation of the 'AdvancedResponse' model.

    TODO: type model description here.

    Attributes:
        extra_info (ExtraInfoDocumentResponse): Extra info about the document
            as requested
        tags (list of string): Mark the document with tags, these tags can be
            used to query for document data / events at a later time.
        attachments (int): Set how many attachments this signjob should have,
            when the document is created you can upload the attachments
            [here](#operation/Attachment_Create). <span style="color: red"> 
            Beware: if you set this value to 3, you MUST upload 3 attachments
            before anyone can sign this document.</span>
        required_signatures (int): Set how many signatures this document needs
            before it can be sealed and sat to complete
        created_by_application (string): The name of the application that
            created the document. Used for Idfy statistics
        get_social_security_number (bool): If your certificate allows it you
            can retrieve the signers social security number after a successful
            sign session
        security (Security): Security settings
        time_to_live (TimeToLive): Customize the time to live for the document
            and urls
        department_id (string): Set department Id to mark invoice with
            department

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "extra_info":'extraInfo',
        "tags":'tags',
        "attachments":'attachments',
        "required_signatures":'requiredSignatures',
        "created_by_application":'createdByApplication',
        "get_social_security_number":'getSocialSecurityNumber',
        "security":'security',
        "time_to_live":'timeToLive',
        "department_id":'departmentId'
    }

    def __init__(self,
                 extra_info=None,
                 tags=None,
                 attachments=None,
                 required_signatures=None,
                 created_by_application=None,
                 get_social_security_number=None,
                 security=None,
                 time_to_live=None,
                 department_id=None,
                 additional_properties = {}):
        """Constructor for the AdvancedResponse class"""

        # Initialize members of the class
        self.extra_info = extra_info
        self.tags = tags
        self.attachments = attachments
        self.required_signatures = required_signatures
        self.created_by_application = created_by_application
        self.get_social_security_number = get_social_security_number
        self.security = security
        self.time_to_live = time_to_live
        self.department_id = department_id

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
        extra_info = idfy_rest_client.models.extra_info_document_response.ExtraInfoDocumentResponse.from_dictionary(dictionary.get('extraInfo')) if dictionary.get('extraInfo') else None
        tags = dictionary.get('tags')
        attachments = dictionary.get('attachments')
        required_signatures = dictionary.get('requiredSignatures')
        created_by_application = dictionary.get('createdByApplication')
        get_social_security_number = dictionary.get('getSocialSecurityNumber')
        security = idfy_rest_client.models.security.Security.from_dictionary(dictionary.get('security')) if dictionary.get('security') else None
        time_to_live = idfy_rest_client.models.time_to_live.TimeToLive.from_dictionary(dictionary.get('timeToLive')) if dictionary.get('timeToLive') else None
        department_id = dictionary.get('departmentId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(extra_info,
                   tags,
                   attachments,
                   required_signatures,
                   created_by_application,
                   get_social_security_number,
                   security,
                   time_to_live,
                   department_id,
                   dictionary)


