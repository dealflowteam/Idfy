# -*- coding: utf-8 -*-

"""
    idfy_rest_client.idfy_rest_client_client

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .configuration import Configuration
from .http.auth.o_auth_2 import OAuth2
from .controllers.business_registry_controller import BusinessRegistryController
from .controllers.themes_controller import ThemesController
from .controllers.language_sets_controller import LanguageSetsController
from .controllers.languages_controller import LanguagesController
from .controllers.account_controller import AccountController
from .controllers.events_controller import EventsController
from .controllers.signature_roles_check_controller import SignatureRolesCheckController
from .controllers.report_controller import ReportController
from .controllers.person_controller import PersonController
from .controllers.lei_controller import LeiController
from .controllers.geo_data_controller import GeoDataController
from .controllers.business_controller import BusinessController
from .controllers.signers_controller import SignersController
from .controllers.notifications_controller import NotificationsController
from .controllers.jwt_controller import JwtController
from .controllers.files_controller import FilesController
from .controllers.documents_controller import DocumentsController
from .controllers.attachments_controller import AttachmentsController
from .controllers.signature_controller import SignatureController
from .controllers.translations_controller import TranslationsController
from .controllers.template_controller import TemplateController
from .controllers.open_id_controller import OpenIDController
from .controllers.o_auth_api_client_controller import OAuthAPIClientController
from .controllers.dealer_controller import DealerController
from .controllers.mobile_info_controller import MobileInfoController
from .controllers.norwegian_bank_id_controller import NorwegianBankIDController
from .controllers.norwgian_bank_id_controller import NorwgianBankIDController
from .controllers.log_controller import LogController
from .controllers.identification_session_controller import IdentificationSessionController
from .controllers.webhooks_controller import WebhooksController
from .controllers.aml_controller import AmlController
from .controllers.invoice_controller import InvoiceController
from .controllers.o_auth_authorization_controller import OAuthAuthorizationController

class IdfyRestClientClient(object):

    auth = OAuth2
    config = Configuration

    @lazy_property
    def business_registry(self):
        return BusinessRegistryController()

    @lazy_property
    def themes(self):
        return ThemesController()

    @lazy_property
    def language_sets(self):
        return LanguageSetsController()

    @lazy_property
    def languages(self):
        return LanguagesController()

    @lazy_property
    def account(self):
        return AccountController()

    @lazy_property
    def events(self):
        return EventsController()

    @lazy_property
    def signature_roles_check(self):
        return SignatureRolesCheckController()

    @lazy_property
    def report(self):
        return ReportController()

    @lazy_property
    def person(self):
        return PersonController()

    @lazy_property
    def lei(self):
        return LeiController()

    @lazy_property
    def geo_data(self):
        return GeoDataController()

    @lazy_property
    def business(self):
        return BusinessController()

    @lazy_property
    def signers(self):
        return SignersController()

    @lazy_property
    def notifications(self):
        return NotificationsController()

    @lazy_property
    def jwt(self):
        return JwtController()

    @lazy_property
    def files(self):
        return FilesController()

    @lazy_property
    def documents(self):
        return DocumentsController()

    @lazy_property
    def attachments(self):
        return AttachmentsController()

    @lazy_property
    def signature(self):
        return SignatureController()

    @lazy_property
    def translations(self):
        return TranslationsController()

    @lazy_property
    def template(self):
        return TemplateController()

    @lazy_property
    def open_id(self):
        return OpenIDController()

    @lazy_property
    def o_auth_api_client(self):
        return OAuthAPIClientController()

    @lazy_property
    def dealer(self):
        return DealerController()

    @lazy_property
    def mobile_info(self):
        return MobileInfoController()

    @lazy_property
    def norwegian_bank_id(self):
        return NorwegianBankIDController()

    @lazy_property
    def norwgian_bank_id(self):
        return NorwgianBankIDController()

    @lazy_property
    def log(self):
        return LogController()

    @lazy_property
    def identification_session(self):
        return IdentificationSessionController()

    @lazy_property
    def webhooks(self):
        return WebhooksController()

    @lazy_property
    def aml(self):
        return AmlController()

    @lazy_property
    def invoice(self):
        return InvoiceController()

    @lazy_property
    def o_auth_authorization(self):
        return OAuthAuthorizationController()


    def __init__(self, 
                 o_auth_client_id = 't50406ae2701149be8d72063a4ac005d0',
                 o_auth_client_secret = 'b3bf4003f34acc146a8270cb991fa2afc3be4a72df2aae0b5db3067120ec23a6'):
        if o_auth_client_id != None:
            Configuration.o_auth_client_id = o_auth_client_id
        if o_auth_client_secret != None:
            Configuration.o_auth_client_secret = o_auth_client_secret


