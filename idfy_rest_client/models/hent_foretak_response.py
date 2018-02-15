# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.hent_foretak_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.identifikasjon
import idfy_rest_client.models.navn_adresse
import idfy_rest_client.models.rating
import idfy_rest_client.models.historisk_rating
import idfy_rest_client.models.grunnfakta
import idfy_rest_client.models.juridisk
import idfy_rest_client.models.verv
import idfy_rest_client.models.aksjonar
import idfy_rest_client.models.datterselskap
import idfy_rest_client.models.okonomi_enk
import idfy_rest_client.models.nokkeltall_foretak
import idfy_rest_client.models.nokkeltall_bransje
import idfy_rest_client.models.nokkeltall_konsern
import idfy_rest_client.models.beta_sammendrag
import idfy_rest_client.models.beta_detaljer
import idfy_rest_client.models.losore
import idfy_rest_client.models.eiendom_norge
import idfy_rest_client.models.konsern_link
import idfy_rest_client.models.scoring
import idfy_rest_client.models.okonomi_sammendrag_foretak
import idfy_rest_client.models.okonomi_sammendrag_konsern
import idfy_rest_client.models.okonomi_detaljer_foretak
import idfy_rest_client.models.okonomi_detaljer_konsern
import idfy_rest_client.models.eiendeler_foretak
import idfy_rest_client.models.eiendeler_konsern
import idfy_rest_client.models.gjeld_egenkapital_foretak
import idfy_rest_client.models.gjeld_egenkapital_konsern
import idfy_rest_client.models.avdeling_data
import idfy_rest_client.models.rettighetshavere
import idfy_rest_client.models.eiendom_norge_liste
import idfy_rest_client.models.fullmakt_foretak
import idfy_rest_client.models.meldinger

class HentForetakResponse(object):

    """Implementation of the 'HentForetakResponse' model.

    TODO: type model description here.

    Attributes:
        identifikasjon_field (Identifikasjon): TODO: type description here.
        navn_adresse_field (NavnAdresse): TODO: type description here.
        rating_field (Rating): TODO: type description here.
        hist_rating_field (list of HistoriskRating): TODO: type description
            here.
        grunnfakta_field (Grunnfakta): TODO: type description here.
        juridisk_field (list of Juridisk): TODO: type description here.
        verv_field (list of Verv): TODO: type description here.
        aksjonar_field (list of Aksjonar): TODO: type description here.
        datterselskap_field (list of Datterselskap): TODO: type description
            here.
        okonomi_enk_field (list of OkonomiEnk): TODO: type description here.
        nokkeltall_foretak_field (list of NokkeltallForetak): TODO: type
            description here.
        nokkeltall_bransje_field (list of NokkeltallBransje): TODO: type
            description here.
        nokkeltall_konsern_field (list of NokkeltallKonsern): TODO: type
            description here.
        beta_sammendrag_field (BetaSammendrag): TODO: type description here.
        beta_detaljer_field (list of BetaDetaljer): TODO: type description
            here.
        losore_field (list of Losore): TODO: type description here.
        eiendom_norge_field (EiendomNorge): TODO: type description here.
        konsern_link_field (list of KonsernLink): TODO: type description
            here.
        scoring_field (Scoring): TODO: type description here.
        okonomi_sammendrag_foretak_field (list of OkonomiSammendragForetak):
            TODO: type description here.
        okonomi_sammendrag_konsern_field (list of OkonomiSammendragKonsern):
            TODO: type description here.
        okonomi_detaljer_foretak_field (list of OkonomiDetaljerForetak): TODO:
            type description here.
        okonomi_detaljer_konsern_field (list of OkonomiDetaljerKonsern): TODO:
            type description here.
        eiendeler_foretak_field (list of EiendelerForetak): TODO: type
            description here.
        eiendeler_konsern_field (list of EiendelerKonsern): TODO: type
            description here.
        gjeld_egenkapital_foretak_field (list of GjeldEgenkapitalForetak):
            TODO: type description here.
        gjeld_egenkapital_konsern_field (list of GjeldEgenkapitalKonsern):
            TODO: type description here.
        avdeling_data_field (AvdelingData): TODO: type description here.
        rettighetshavere_field (list of Rettighetshavere): TODO: type
            description here.
        eiendom_norge_liste_field (list of EiendomNorgeListe): TODO: type
            description here.
        fullmakt_foretak_field (list of FullmaktForetak): TODO: type
            description here.
        meldinger_field (list of Meldinger): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "identifikasjon_field":'identifikasjonField',
        "navn_adresse_field":'navnAdresseField',
        "rating_field":'ratingField',
        "hist_rating_field":'histRatingField',
        "grunnfakta_field":'grunnfaktaField',
        "juridisk_field":'juridiskField',
        "verv_field":'vervField',
        "aksjonar_field":'aksjonarField',
        "datterselskap_field":'datterselskapField',
        "okonomi_enk_field":'okonomiEnkField',
        "nokkeltall_foretak_field":'nokkeltallForetakField',
        "nokkeltall_bransje_field":'nokkeltallBransjeField',
        "nokkeltall_konsern_field":'nokkeltallKonsernField',
        "beta_sammendrag_field":'betaSammendragField',
        "beta_detaljer_field":'betaDetaljerField',
        "losore_field":'losoreField',
        "eiendom_norge_field":'eiendomNorgeField',
        "konsern_link_field":'konsernLinkField',
        "scoring_field":'scoringField',
        "okonomi_sammendrag_foretak_field":'okonomiSammendragForetakField',
        "okonomi_sammendrag_konsern_field":'okonomiSammendragKonsernField',
        "okonomi_detaljer_foretak_field":'okonomiDetaljerForetakField',
        "okonomi_detaljer_konsern_field":'okonomiDetaljerKonsernField',
        "eiendeler_foretak_field":'eiendelerForetakField',
        "eiendeler_konsern_field":'eiendelerKonsernField',
        "gjeld_egenkapital_foretak_field":'gjeldEgenkapitalForetakField',
        "gjeld_egenkapital_konsern_field":'gjeldEgenkapitalKonsernField',
        "avdeling_data_field":'avdelingDataField',
        "rettighetshavere_field":'rettighetshavereField',
        "eiendom_norge_liste_field":'eiendomNorgeListeField',
        "fullmakt_foretak_field":'fullmaktForetakField',
        "meldinger_field":'meldingerField'
    }

    def __init__(self,
                 identifikasjon_field=None,
                 navn_adresse_field=None,
                 rating_field=None,
                 hist_rating_field=None,
                 grunnfakta_field=None,
                 juridisk_field=None,
                 verv_field=None,
                 aksjonar_field=None,
                 datterselskap_field=None,
                 okonomi_enk_field=None,
                 nokkeltall_foretak_field=None,
                 nokkeltall_bransje_field=None,
                 nokkeltall_konsern_field=None,
                 beta_sammendrag_field=None,
                 beta_detaljer_field=None,
                 losore_field=None,
                 eiendom_norge_field=None,
                 konsern_link_field=None,
                 scoring_field=None,
                 okonomi_sammendrag_foretak_field=None,
                 okonomi_sammendrag_konsern_field=None,
                 okonomi_detaljer_foretak_field=None,
                 okonomi_detaljer_konsern_field=None,
                 eiendeler_foretak_field=None,
                 eiendeler_konsern_field=None,
                 gjeld_egenkapital_foretak_field=None,
                 gjeld_egenkapital_konsern_field=None,
                 avdeling_data_field=None,
                 rettighetshavere_field=None,
                 eiendom_norge_liste_field=None,
                 fullmakt_foretak_field=None,
                 meldinger_field=None,
                 additional_properties = {}):
        """Constructor for the HentForetakResponse class"""

        # Initialize members of the class
        self.identifikasjon_field = identifikasjon_field
        self.navn_adresse_field = navn_adresse_field
        self.rating_field = rating_field
        self.hist_rating_field = hist_rating_field
        self.grunnfakta_field = grunnfakta_field
        self.juridisk_field = juridisk_field
        self.verv_field = verv_field
        self.aksjonar_field = aksjonar_field
        self.datterselskap_field = datterselskap_field
        self.okonomi_enk_field = okonomi_enk_field
        self.nokkeltall_foretak_field = nokkeltall_foretak_field
        self.nokkeltall_bransje_field = nokkeltall_bransje_field
        self.nokkeltall_konsern_field = nokkeltall_konsern_field
        self.beta_sammendrag_field = beta_sammendrag_field
        self.beta_detaljer_field = beta_detaljer_field
        self.losore_field = losore_field
        self.eiendom_norge_field = eiendom_norge_field
        self.konsern_link_field = konsern_link_field
        self.scoring_field = scoring_field
        self.okonomi_sammendrag_foretak_field = okonomi_sammendrag_foretak_field
        self.okonomi_sammendrag_konsern_field = okonomi_sammendrag_konsern_field
        self.okonomi_detaljer_foretak_field = okonomi_detaljer_foretak_field
        self.okonomi_detaljer_konsern_field = okonomi_detaljer_konsern_field
        self.eiendeler_foretak_field = eiendeler_foretak_field
        self.eiendeler_konsern_field = eiendeler_konsern_field
        self.gjeld_egenkapital_foretak_field = gjeld_egenkapital_foretak_field
        self.gjeld_egenkapital_konsern_field = gjeld_egenkapital_konsern_field
        self.avdeling_data_field = avdeling_data_field
        self.rettighetshavere_field = rettighetshavere_field
        self.eiendom_norge_liste_field = eiendom_norge_liste_field
        self.fullmakt_foretak_field = fullmakt_foretak_field
        self.meldinger_field = meldinger_field

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
        identifikasjon_field = idfy_rest_client.models.identifikasjon.Identifikasjon.from_dictionary(dictionary.get('identifikasjonField')) if dictionary.get('identifikasjonField') else None
        navn_adresse_field = idfy_rest_client.models.navn_adresse.NavnAdresse.from_dictionary(dictionary.get('navnAdresseField')) if dictionary.get('navnAdresseField') else None
        rating_field = idfy_rest_client.models.rating.Rating.from_dictionary(dictionary.get('ratingField')) if dictionary.get('ratingField') else None
        hist_rating_field = None
        if dictionary.get('histRatingField') != None:
            hist_rating_field = list()
            for structure in dictionary.get('histRatingField'):
                hist_rating_field.append(idfy_rest_client.models.historisk_rating.HistoriskRating.from_dictionary(structure))
        grunnfakta_field = idfy_rest_client.models.grunnfakta.Grunnfakta.from_dictionary(dictionary.get('grunnfaktaField')) if dictionary.get('grunnfaktaField') else None
        juridisk_field = None
        if dictionary.get('juridiskField') != None:
            juridisk_field = list()
            for structure in dictionary.get('juridiskField'):
                juridisk_field.append(idfy_rest_client.models.juridisk.Juridisk.from_dictionary(structure))
        verv_field = None
        if dictionary.get('vervField') != None:
            verv_field = list()
            for structure in dictionary.get('vervField'):
                verv_field.append(idfy_rest_client.models.verv.Verv.from_dictionary(structure))
        aksjonar_field = None
        if dictionary.get('aksjonarField') != None:
            aksjonar_field = list()
            for structure in dictionary.get('aksjonarField'):
                aksjonar_field.append(idfy_rest_client.models.aksjonar.Aksjonar.from_dictionary(structure))
        datterselskap_field = None
        if dictionary.get('datterselskapField') != None:
            datterselskap_field = list()
            for structure in dictionary.get('datterselskapField'):
                datterselskap_field.append(idfy_rest_client.models.datterselskap.Datterselskap.from_dictionary(structure))
        okonomi_enk_field = None
        if dictionary.get('okonomiEnkField') != None:
            okonomi_enk_field = list()
            for structure in dictionary.get('okonomiEnkField'):
                okonomi_enk_field.append(idfy_rest_client.models.okonomi_enk.OkonomiEnk.from_dictionary(structure))
        nokkeltall_foretak_field = None
        if dictionary.get('nokkeltallForetakField') != None:
            nokkeltall_foretak_field = list()
            for structure in dictionary.get('nokkeltallForetakField'):
                nokkeltall_foretak_field.append(idfy_rest_client.models.nokkeltall_foretak.NokkeltallForetak.from_dictionary(structure))
        nokkeltall_bransje_field = None
        if dictionary.get('nokkeltallBransjeField') != None:
            nokkeltall_bransje_field = list()
            for structure in dictionary.get('nokkeltallBransjeField'):
                nokkeltall_bransje_field.append(idfy_rest_client.models.nokkeltall_bransje.NokkeltallBransje.from_dictionary(structure))
        nokkeltall_konsern_field = None
        if dictionary.get('nokkeltallKonsernField') != None:
            nokkeltall_konsern_field = list()
            for structure in dictionary.get('nokkeltallKonsernField'):
                nokkeltall_konsern_field.append(idfy_rest_client.models.nokkeltall_konsern.NokkeltallKonsern.from_dictionary(structure))
        beta_sammendrag_field = idfy_rest_client.models.beta_sammendrag.BetaSammendrag.from_dictionary(dictionary.get('betaSammendragField')) if dictionary.get('betaSammendragField') else None
        beta_detaljer_field = None
        if dictionary.get('betaDetaljerField') != None:
            beta_detaljer_field = list()
            for structure in dictionary.get('betaDetaljerField'):
                beta_detaljer_field.append(idfy_rest_client.models.beta_detaljer.BetaDetaljer.from_dictionary(structure))
        losore_field = None
        if dictionary.get('losoreField') != None:
            losore_field = list()
            for structure in dictionary.get('losoreField'):
                losore_field.append(idfy_rest_client.models.losore.Losore.from_dictionary(structure))
        eiendom_norge_field = idfy_rest_client.models.eiendom_norge.EiendomNorge.from_dictionary(dictionary.get('eiendomNorgeField')) if dictionary.get('eiendomNorgeField') else None
        konsern_link_field = None
        if dictionary.get('konsernLinkField') != None:
            konsern_link_field = list()
            for structure in dictionary.get('konsernLinkField'):
                konsern_link_field.append(idfy_rest_client.models.konsern_link.KonsernLink.from_dictionary(structure))
        scoring_field = idfy_rest_client.models.scoring.Scoring.from_dictionary(dictionary.get('scoringField')) if dictionary.get('scoringField') else None
        okonomi_sammendrag_foretak_field = None
        if dictionary.get('okonomiSammendragForetakField') != None:
            okonomi_sammendrag_foretak_field = list()
            for structure in dictionary.get('okonomiSammendragForetakField'):
                okonomi_sammendrag_foretak_field.append(idfy_rest_client.models.okonomi_sammendrag_foretak.OkonomiSammendragForetak.from_dictionary(structure))
        okonomi_sammendrag_konsern_field = None
        if dictionary.get('okonomiSammendragKonsernField') != None:
            okonomi_sammendrag_konsern_field = list()
            for structure in dictionary.get('okonomiSammendragKonsernField'):
                okonomi_sammendrag_konsern_field.append(idfy_rest_client.models.okonomi_sammendrag_konsern.OkonomiSammendragKonsern.from_dictionary(structure))
        okonomi_detaljer_foretak_field = None
        if dictionary.get('okonomiDetaljerForetakField') != None:
            okonomi_detaljer_foretak_field = list()
            for structure in dictionary.get('okonomiDetaljerForetakField'):
                okonomi_detaljer_foretak_field.append(idfy_rest_client.models.okonomi_detaljer_foretak.OkonomiDetaljerForetak.from_dictionary(structure))
        okonomi_detaljer_konsern_field = None
        if dictionary.get('okonomiDetaljerKonsernField') != None:
            okonomi_detaljer_konsern_field = list()
            for structure in dictionary.get('okonomiDetaljerKonsernField'):
                okonomi_detaljer_konsern_field.append(idfy_rest_client.models.okonomi_detaljer_konsern.OkonomiDetaljerKonsern.from_dictionary(structure))
        eiendeler_foretak_field = None
        if dictionary.get('eiendelerForetakField') != None:
            eiendeler_foretak_field = list()
            for structure in dictionary.get('eiendelerForetakField'):
                eiendeler_foretak_field.append(idfy_rest_client.models.eiendeler_foretak.EiendelerForetak.from_dictionary(structure))
        eiendeler_konsern_field = None
        if dictionary.get('eiendelerKonsernField') != None:
            eiendeler_konsern_field = list()
            for structure in dictionary.get('eiendelerKonsernField'):
                eiendeler_konsern_field.append(idfy_rest_client.models.eiendeler_konsern.EiendelerKonsern.from_dictionary(structure))
        gjeld_egenkapital_foretak_field = None
        if dictionary.get('gjeldEgenkapitalForetakField') != None:
            gjeld_egenkapital_foretak_field = list()
            for structure in dictionary.get('gjeldEgenkapitalForetakField'):
                gjeld_egenkapital_foretak_field.append(idfy_rest_client.models.gjeld_egenkapital_foretak.GjeldEgenkapitalForetak.from_dictionary(structure))
        gjeld_egenkapital_konsern_field = None
        if dictionary.get('gjeldEgenkapitalKonsernField') != None:
            gjeld_egenkapital_konsern_field = list()
            for structure in dictionary.get('gjeldEgenkapitalKonsernField'):
                gjeld_egenkapital_konsern_field.append(idfy_rest_client.models.gjeld_egenkapital_konsern.GjeldEgenkapitalKonsern.from_dictionary(structure))
        avdeling_data_field = idfy_rest_client.models.avdeling_data.AvdelingData.from_dictionary(dictionary.get('avdelingDataField')) if dictionary.get('avdelingDataField') else None
        rettighetshavere_field = None
        if dictionary.get('rettighetshavereField') != None:
            rettighetshavere_field = list()
            for structure in dictionary.get('rettighetshavereField'):
                rettighetshavere_field.append(idfy_rest_client.models.rettighetshavere.Rettighetshavere.from_dictionary(structure))
        eiendom_norge_liste_field = None
        if dictionary.get('eiendomNorgeListeField') != None:
            eiendom_norge_liste_field = list()
            for structure in dictionary.get('eiendomNorgeListeField'):
                eiendom_norge_liste_field.append(idfy_rest_client.models.eiendom_norge_liste.EiendomNorgeListe.from_dictionary(structure))
        fullmakt_foretak_field = None
        if dictionary.get('fullmaktForetakField') != None:
            fullmakt_foretak_field = list()
            for structure in dictionary.get('fullmaktForetakField'):
                fullmakt_foretak_field.append(idfy_rest_client.models.fullmakt_foretak.FullmaktForetak.from_dictionary(structure))
        meldinger_field = None
        if dictionary.get('meldingerField') != None:
            meldinger_field = list()
            for structure in dictionary.get('meldingerField'):
                meldinger_field.append(idfy_rest_client.models.meldinger.Meldinger.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(identifikasjon_field,
                   navn_adresse_field,
                   rating_field,
                   hist_rating_field,
                   grunnfakta_field,
                   juridisk_field,
                   verv_field,
                   aksjonar_field,
                   datterselskap_field,
                   okonomi_enk_field,
                   nokkeltall_foretak_field,
                   nokkeltall_bransje_field,
                   nokkeltall_konsern_field,
                   beta_sammendrag_field,
                   beta_detaljer_field,
                   losore_field,
                   eiendom_norge_field,
                   konsern_link_field,
                   scoring_field,
                   okonomi_sammendrag_foretak_field,
                   okonomi_sammendrag_konsern_field,
                   okonomi_detaljer_foretak_field,
                   okonomi_detaljer_konsern_field,
                   eiendeler_foretak_field,
                   eiendeler_konsern_field,
                   gjeld_egenkapital_foretak_field,
                   gjeld_egenkapital_konsern_field,
                   avdeling_data_field,
                   rettighetshavere_field,
                   eiendom_norge_liste_field,
                   fullmakt_foretak_field,
                   meldinger_field,
                   dictionary)


