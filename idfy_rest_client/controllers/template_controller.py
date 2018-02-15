# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.template_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.pdf_template import PdfTemplate
from ..models.pdf_template_list_item import PdfTemplateListItem
from ..exceptions.api_exception import APIException

class TemplateController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def retrieve_data_source(self,
                             model,
                             xml_tempalte=None):
        """Does a POST request to /admin/template/datasource.

        Preview the underlaying template datasource

        Args:
            model (TemplatePreview): Preview model
            xml_tempalte (XmlTempalte, optional): Prefilled XmlSignature
                templates

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(model=model)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/datasource'
        _query_parameters = {
            'xmlTempalte': xml_tempalte
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(model))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def preview_template_from_model(self,
                                    model,
                                    xml_template=None):
        """Does a POST request to /admin/template/preview.

        Preview your PAdES template use your own signature file or choose the
        xmlTemplate prefilled

        Args:
            model (TemplatePreview): Preview model
            xml_template (XmlTemplate, optional): TODO: type description here.
                Example: 

        Returns:
            void: Response from the API. File response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(model=model)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/preview'
        _query_parameters = {
            'xmlTemplate': xml_template
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(model))
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def preview_template_from_id(self,
                                 model,
                                 id,
                                 xml_template=None):
        """Does a POST request to /admin/template/preview/{id}.

        Preview your PAdES template use your own signature file or choose the
        xmlTemplate prefilled

        Args:
            model (TemplateWithIdPreview): Preview model
            id (uuid|string): Template Id
            xml_template (XmlTemplate, optional): TODO: type description here.
                Example: 

        Returns:
            void: Response from the API. File response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(model=model,
                                 id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/preview/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_parameters = {
            'xmlTemplate': xml_template
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(model))
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def retrieve_default_coverpage_template(self):
        """Does a GET request to /admin/template/defaults/coverpage.

        Gets the HTML used as a template for the details page if not
        overridden by user

        Returns:
            PdfTemplate: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/defaults/coverpage'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PdfTemplate.from_dictionary)

    def retrieve_default_details_template(self,
                                          language):
        """Does a GET request to /admin/template/defaults/details.

        Gets the HTML used as a template for the details page if not
        overridden by user

        Args:
            language (Language185): Language of the details page

        Returns:
            string: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(language=language)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/defaults/details'
        _query_parameters = {
            'language': language
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def delete_template(self,
                        id):
        """Does a DELETE request to /admin/template/{id}.

        Deletes the PDF template

        Args:
            id (uuid|string): The template ID

        Returns:
            mixed: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_template(self,
                        id,
                        model):
        """Does a PUT request to /admin/template/{id}.

        Updates the given PDF template

        Args:
            id (uuid|string): The template ID
            model (UpdatePdfTemplate): The template body

        Returns:
            PdfTemplate: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id,
                                 model=model)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(model))
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PdfTemplate.from_dictionary)

    def retrieve_template(self,
                          id):
        """Does a GET request to /admin/template/{id}.

        Gets a PDF template

        Args:
            id (uuid|string): The template ID

        Returns:
            PdfTemplate: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PdfTemplate.from_dictionary)

    def create_template(self,
                        model):
        """Does a POST request to /admin/template.

        Creates a new PDF template

        Args:
            model (CreatePdfTemplate): Create PDF template body

        Returns:
            PdfTemplate: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(model=model)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(model))
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PdfTemplate.from_dictionary)

    def list_templates_for_account(self):
        """Does a GET request to /admin/template.

        Lists all the PDF template for the account

        Returns:
            list of PdfTemplateListItem: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/admin/template'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request', _context)
        elif _context.response.status_code == 403:
            raise APIException('Forbidden (Access denied)', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PdfTemplateListItem.from_dictionary)
