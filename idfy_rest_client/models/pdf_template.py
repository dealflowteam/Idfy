# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.pdf_template

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
from idfy_rest_client.api_helper import APIHelper
import idfy_rest_client.models.details_page_html
import idfy_rest_client.models.verified_template
import idfy_rest_client.models.labels

class PdfTemplate(object):

    """Implementation of the 'PdfTemplate' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        name (string): The name of the Pdf template
        cover_page_setting (CoverPageSetting): Coverpage is the page added to
            the document at the beginning or end that show a list of the
            signers. This settings hides that page or put it first or last.
            Default firstpage
        add_list_of_signatures_on_last_page_of_existing_pdf (bool): Coverpage
            is the page added to the document at the beginning or end that
            show a list of the signers. This settings hides that page or put
            it first or last. Default firstpage
        cover_page_html (string): The html template for the coverpage, if this
            is set it will override the default template. See our
            documentation on more info on how to make your own custom
            template.
        details_page_html (DetailsPageHtml): List of html templates for the
            details attatchments. If this is set for one or more language, it
            will override the default template. See our documentation on more
            info on how to make your own custom template.
        verified_template (VerifiedTemplate): List of labels for the verified
            label on the footer on each page. If this is set it will override
            the default text. See our documentation on more info on how to
            customize.
        labels (Labels): List of labels for the templates, this are used in
            the html templates. If this is set it will override the default
            labels. See our documentation on more info on how to customize.
        include_logo (bool): Include your logo in the Pdf template
        last_edited (datetime): Timestamp when the template is last edited

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'Id',
        "name":'Name',
        "cover_page_setting":'CoverPageSetting',
        "add_list_of_signatures_on_last_page_of_existing_pdf":'AddListOfSignaturesOnLastPageOfExistingPDF',
        "cover_page_html":'CoverPageHtml',
        "details_page_html":'DetailsPageHtml',
        "verified_template":'VerifiedTemplate',
        "labels":'Labels',
        "include_logo":'IncludeLogo',
        "last_edited":'LastEdited'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 cover_page_setting=None,
                 add_list_of_signatures_on_last_page_of_existing_pdf=None,
                 cover_page_html=None,
                 details_page_html=None,
                 verified_template=None,
                 labels=None,
                 include_logo=None,
                 last_edited=None,
                 additional_properties = {}):
        """Constructor for the PdfTemplate class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.cover_page_setting = cover_page_setting
        self.add_list_of_signatures_on_last_page_of_existing_pdf = add_list_of_signatures_on_last_page_of_existing_pdf
        self.cover_page_html = cover_page_html
        self.details_page_html = details_page_html
        self.verified_template = verified_template
        self.labels = labels
        self.include_logo = include_logo
        self.last_edited = APIHelper.RFC3339DateTime(last_edited) if last_edited else None

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
        id = dictionary.get('Id')
        name = dictionary.get('Name')
        cover_page_setting = dictionary.get('CoverPageSetting')
        add_list_of_signatures_on_last_page_of_existing_pdf = dictionary.get('AddListOfSignaturesOnLastPageOfExistingPDF')
        cover_page_html = dictionary.get('CoverPageHtml')
        details_page_html = idfy_rest_client.models.details_page_html.DetailsPageHtml.from_dictionary(dictionary.get('DetailsPageHtml')) if dictionary.get('DetailsPageHtml') else None
        verified_template = idfy_rest_client.models.verified_template.VerifiedTemplate.from_dictionary(dictionary.get('VerifiedTemplate')) if dictionary.get('VerifiedTemplate') else None
        labels = idfy_rest_client.models.labels.Labels.from_dictionary(dictionary.get('Labels')) if dictionary.get('Labels') else None
        include_logo = dictionary.get('IncludeLogo')
        last_edited = APIHelper.RFC3339DateTime.from_value(dictionary.get("LastEdited")).datetime if dictionary.get("LastEdited") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   cover_page_setting,
                   add_list_of_signatures_on_last_page_of_existing_pdf,
                   cover_page_html,
                   details_page_html,
                   verified_template,
                   labels,
                   include_logo,
                   last_edited,
                   dictionary)


