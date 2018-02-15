# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.data_to_sign

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.packaging

class DataToSign(object):

    """Implementation of the 'DataToSign' model.

    Data that should be signed

    Attributes:
        base_64_content (string): Base 64 encoded string of content, utf-8
        file_name (string): The document FileName, has to include a valid
            extension (.pdf, .xml, .txt, .doc, .docx, .rtf, .ott, odt)
        base_64_content_style_sheet (string): Stylesheet to be included if you
            are uploading xml
        convert_to_pdf (bool): Convert a non PDF file to PDF, supported
            formats are word documents, rich texformat and open office (.doc,
            docx, .rtf .odt and ott), Remark the document that is signed is
            not the original document.
        packaging (Packaging): Set how you want the signed file to be
            packaged

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "base_64_content":'base64Content',
        "file_name":'fileName',
        "base_64_content_style_sheet":'base64ContentStyleSheet',
        "convert_to_pdf":'convertToPDF',
        "packaging":'packaging'
    }

    def __init__(self,
                 base_64_content=None,
                 file_name=None,
                 base_64_content_style_sheet=None,
                 convert_to_pdf=None,
                 packaging=None,
                 additional_properties = {}):
        """Constructor for the DataToSign class"""

        # Initialize members of the class
        self.base_64_content = base_64_content
        self.file_name = file_name
        self.base_64_content_style_sheet = base_64_content_style_sheet
        self.convert_to_pdf = convert_to_pdf
        self.packaging = packaging

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
        base_64_content = dictionary.get('base64Content')
        file_name = dictionary.get('fileName')
        base_64_content_style_sheet = dictionary.get('base64ContentStyleSheet')
        convert_to_pdf = dictionary.get('convertToPDF')
        packaging = idfy_rest_client.models.packaging.Packaging.from_dictionary(dictionary.get('packaging')) if dictionary.get('packaging') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(base_64_content,
                   file_name,
                   base_64_content_style_sheet,
                   convert_to_pdf,
                   packaging,
                   dictionary)


