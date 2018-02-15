# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_hent_person_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.person_identifikasjon
import idfy_rest_client.models.person_navn_adresse
import idfy_rest_client.models.person_scoring
import idfy_rest_client.models.person_delomrader
import idfy_rest_client.models.person_beta_sammendrag
import idfy_rest_client.models.person_beta_detaljer
import idfy_rest_client.models.person_ligning
import idfy_rest_client.models.person_disponibel_inntekt
import idfy_rest_client.models.person_narings_interesser
import idfy_rest_client.models.person_eiendom_norge
import idfy_rest_client.models.person_eiendom_liste
import idfy_rest_client.models.person_losore
import idfy_rest_client.models.person_tidligere_navn_adresse
import idfy_rest_client.models.person_fullmakt_foretak
import idfy_rest_client.models.person_meldinger

class PersonHentPersonResponse(object):

    """Implementation of the 'Person.HentPersonResponse' model.

    TODO: type model description here.

    Attributes:
        identifikasjon_field (PersonIdentifikasjon): TODO: type description
            here.
        navn_adresse_field (PersonNavnAdresse): TODO: type description here.
        scoring_field (PersonScoring): TODO: type description here.
        delomrader_field (list of PersonDelomrader): TODO: type description
            here.
        beta_sammendrag_field (PersonBetaSammendrag): TODO: type description
            here.
        beta_detaljer_field (list of PersonBetaDetaljer): TODO: type
            description here.
        ligning_field (list of PersonLigning): TODO: type description here.
        disponibel_inntekt_field (list of PersonDisponibelInntekt): TODO: type
            description here.
        narings_interesser_field (list of PersonNaringsInteresser): TODO: type
            description here.
        eiendom_norge_field (PersonEiendomNorge): TODO: type description
            here.
        eiendom_liste_field (list of PersonEiendomListe): TODO: type
            description here.
        losore_field (list of PersonLosore): TODO: type description here.
        tidligere_navn_adresse_field (list of PersonTidligereNavnAdresse):
            TODO: type description here.
        fullmakt_foretak_field (list of PersonFullmaktForetak): TODO: type
            description here.
        meldinger_field (list of PersonMeldinger): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "identifikasjon_field":'identifikasjonField',
        "navn_adresse_field":'navnAdresseField',
        "scoring_field":'scoringField',
        "delomrader_field":'delomraderField',
        "beta_sammendrag_field":'betaSammendragField',
        "beta_detaljer_field":'betaDetaljerField',
        "ligning_field":'ligningField',
        "disponibel_inntekt_field":'disponibelInntektField',
        "narings_interesser_field":'naringsInteresserField',
        "eiendom_norge_field":'eiendomNorgeField',
        "eiendom_liste_field":'eiendomListeField',
        "losore_field":'losoreField',
        "tidligere_navn_adresse_field":'tidligereNavnAdresseField',
        "fullmakt_foretak_field":'fullmaktForetakField',
        "meldinger_field":'meldingerField'
    }

    def __init__(self,
                 identifikasjon_field=None,
                 navn_adresse_field=None,
                 scoring_field=None,
                 delomrader_field=None,
                 beta_sammendrag_field=None,
                 beta_detaljer_field=None,
                 ligning_field=None,
                 disponibel_inntekt_field=None,
                 narings_interesser_field=None,
                 eiendom_norge_field=None,
                 eiendom_liste_field=None,
                 losore_field=None,
                 tidligere_navn_adresse_field=None,
                 fullmakt_foretak_field=None,
                 meldinger_field=None,
                 additional_properties = {}):
        """Constructor for the PersonHentPersonResponse class"""

        # Initialize members of the class
        self.identifikasjon_field = identifikasjon_field
        self.navn_adresse_field = navn_adresse_field
        self.scoring_field = scoring_field
        self.delomrader_field = delomrader_field
        self.beta_sammendrag_field = beta_sammendrag_field
        self.beta_detaljer_field = beta_detaljer_field
        self.ligning_field = ligning_field
        self.disponibel_inntekt_field = disponibel_inntekt_field
        self.narings_interesser_field = narings_interesser_field
        self.eiendom_norge_field = eiendom_norge_field
        self.eiendom_liste_field = eiendom_liste_field
        self.losore_field = losore_field
        self.tidligere_navn_adresse_field = tidligere_navn_adresse_field
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
        identifikasjon_field = idfy_rest_client.models.person_identifikasjon.PersonIdentifikasjon.from_dictionary(dictionary.get('identifikasjonField')) if dictionary.get('identifikasjonField') else None
        navn_adresse_field = idfy_rest_client.models.person_navn_adresse.PersonNavnAdresse.from_dictionary(dictionary.get('navnAdresseField')) if dictionary.get('navnAdresseField') else None
        scoring_field = idfy_rest_client.models.person_scoring.PersonScoring.from_dictionary(dictionary.get('scoringField')) if dictionary.get('scoringField') else None
        delomrader_field = None
        if dictionary.get('delomraderField') != None:
            delomrader_field = list()
            for structure in dictionary.get('delomraderField'):
                delomrader_field.append(idfy_rest_client.models.person_delomrader.PersonDelomrader.from_dictionary(structure))
        beta_sammendrag_field = idfy_rest_client.models.person_beta_sammendrag.PersonBetaSammendrag.from_dictionary(dictionary.get('betaSammendragField')) if dictionary.get('betaSammendragField') else None
        beta_detaljer_field = None
        if dictionary.get('betaDetaljerField') != None:
            beta_detaljer_field = list()
            for structure in dictionary.get('betaDetaljerField'):
                beta_detaljer_field.append(idfy_rest_client.models.person_beta_detaljer.PersonBetaDetaljer.from_dictionary(structure))
        ligning_field = None
        if dictionary.get('ligningField') != None:
            ligning_field = list()
            for structure in dictionary.get('ligningField'):
                ligning_field.append(idfy_rest_client.models.person_ligning.PersonLigning.from_dictionary(structure))
        disponibel_inntekt_field = None
        if dictionary.get('disponibelInntektField') != None:
            disponibel_inntekt_field = list()
            for structure in dictionary.get('disponibelInntektField'):
                disponibel_inntekt_field.append(idfy_rest_client.models.person_disponibel_inntekt.PersonDisponibelInntekt.from_dictionary(structure))
        narings_interesser_field = None
        if dictionary.get('naringsInteresserField') != None:
            narings_interesser_field = list()
            for structure in dictionary.get('naringsInteresserField'):
                narings_interesser_field.append(idfy_rest_client.models.person_narings_interesser.PersonNaringsInteresser.from_dictionary(structure))
        eiendom_norge_field = idfy_rest_client.models.person_eiendom_norge.PersonEiendomNorge.from_dictionary(dictionary.get('eiendomNorgeField')) if dictionary.get('eiendomNorgeField') else None
        eiendom_liste_field = None
        if dictionary.get('eiendomListeField') != None:
            eiendom_liste_field = list()
            for structure in dictionary.get('eiendomListeField'):
                eiendom_liste_field.append(idfy_rest_client.models.person_eiendom_liste.PersonEiendomListe.from_dictionary(structure))
        losore_field = None
        if dictionary.get('losoreField') != None:
            losore_field = list()
            for structure in dictionary.get('losoreField'):
                losore_field.append(idfy_rest_client.models.person_losore.PersonLosore.from_dictionary(structure))
        tidligere_navn_adresse_field = None
        if dictionary.get('tidligereNavnAdresseField') != None:
            tidligere_navn_adresse_field = list()
            for structure in dictionary.get('tidligereNavnAdresseField'):
                tidligere_navn_adresse_field.append(idfy_rest_client.models.person_tidligere_navn_adresse.PersonTidligereNavnAdresse.from_dictionary(structure))
        fullmakt_foretak_field = None
        if dictionary.get('fullmaktForetakField') != None:
            fullmakt_foretak_field = list()
            for structure in dictionary.get('fullmaktForetakField'):
                fullmakt_foretak_field.append(idfy_rest_client.models.person_fullmakt_foretak.PersonFullmaktForetak.from_dictionary(structure))
        meldinger_field = None
        if dictionary.get('meldingerField') != None:
            meldinger_field = list()
            for structure in dictionary.get('meldingerField'):
                meldinger_field.append(idfy_rest_client.models.person_meldinger.PersonMeldinger.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(identifikasjon_field,
                   navn_adresse_field,
                   scoring_field,
                   delomrader_field,
                   beta_sammendrag_field,
                   beta_detaljer_field,
                   ligning_field,
                   disponibel_inntekt_field,
                   narings_interesser_field,
                   eiendom_norge_field,
                   eiendom_liste_field,
                   losore_field,
                   tidligere_navn_adresse_field,
                   fullmakt_foretak_field,
                   meldinger_field,
                   dictionary)


