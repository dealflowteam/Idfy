# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.okonomi_detaljer_konsern

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class OkonomiDetaljerKonsern(object):

    """Implementation of the 'OkonomiDetaljerKonsern' model.

    TODO: type model description here.

    Attributes:
        regnskaps_av_ar_field (int): TODO: type description here.
        regnskaps_av_mnd_field (int): TODO: type description here.
        totalinntekt_field (long|int): TODO: type description here.
        salgsinntekter_field (long|int): TODO: type description here.
        annen_driftsinntekt_field (long|int): TODO: type description here.
        varekostnad_field (long|int): TODO: type description here.
        beholdningsendring_field (long|int): TODO: type description here.
        lonnskostnad_field (long|int): TODO: type description here.
        avskrivninger_field (long|int): TODO: type description here.
        nedskrivninger_field (long|int): TODO: type description here.
        annen_driftskostnad_field (long|int): TODO: type description here.
        drifts_resultat_field (long|int): TODO: type description here.
        inntekt_inv_datter_field (long|int): TODO: type description here.
        inntekt_inv_konsern_field (long|int): TODO: type description here.
        inntekt_inv_annen_field (long|int): TODO: type description here.
        renteinntekt_konsern_field (long|int): TODO: type description here.
        renteinntekt_annen_field (long|int): TODO: type description here.
        finansinntekt_annen_field (long|int): TODO: type description here.
        finansinntekt_field (long|int): TODO: type description here.
        verdiendring_mar_fin_omlopsmidler_field (long|int): TODO: type
            description here.
        nedskrivning_mar_fin_omlopsmidler_field (long|int): TODO: type
            description here.
        nedskrivning_fin_anleggsmidler_field (long|int): TODO: type
            description here.
        rentekostnad_konsern_field (long|int): TODO: type description here.
        annen_rentekostnad_field (long|int): TODO: type description here.
        annen_finanskostnad_field (long|int): TODO: type description here.
        finanskostnad_field (long|int): TODO: type description here.
        ord_resultat_for_skatt_field (long|int): TODO: type description here.
        skatt_ord_resultat_field (long|int): TODO: type description here.
        ord_resultat_field (long|int): TODO: type description here.
        ekstraord_inntekt_field (long|int): TODO: type description here.
        ekstraord_kostnad_field (long|int): TODO: type description here.
        skatt_ekstraord_resultat_field (long|int): TODO: type description
            here.
        sum_skatt_field (long|int): TODO: type description here.
        minoritets_interesser_field (long|int): TODO: type description here.
        ars_resultat_field (long|int): TODO: type description here.
        konsernbidrag_field (long|int): TODO: type description here.
        utbytte_field (long|int): TODO: type description here.
        til_fond_vurd_for_field (long|int): TODO: type description here.
        til_annen_egenkapital_field (long|int): TODO: type description here.
        tap_krav_field (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "regnskaps_av_ar_field":'regnskapsAvArField',
        "regnskaps_av_mnd_field":'regnskapsAvMndField',
        "totalinntekt_field":'totalinntektField',
        "salgsinntekter_field":'salgsinntekterField',
        "annen_driftsinntekt_field":'annenDriftsinntektField',
        "varekostnad_field":'varekostnadField',
        "beholdningsendring_field":'beholdningsendringField',
        "lonnskostnad_field":'lonnskostnadField',
        "avskrivninger_field":'avskrivningerField',
        "nedskrivninger_field":'nedskrivningerField',
        "annen_driftskostnad_field":'annenDriftskostnadField',
        "drifts_resultat_field":'driftsResultatField',
        "inntekt_inv_datter_field":'inntektInvDatterField',
        "inntekt_inv_konsern_field":'inntektInvKonsernField',
        "inntekt_inv_annen_field":'inntektInvAnnenField',
        "renteinntekt_konsern_field":'renteinntektKonsernField',
        "renteinntekt_annen_field":'renteinntektAnnenField',
        "finansinntekt_annen_field":'finansinntektAnnenField',
        "finansinntekt_field":'finansinntektField',
        "verdiendring_mar_fin_omlopsmidler_field":'verdiendringMarFinOmlopsmidlerField',
        "nedskrivning_mar_fin_omlopsmidler_field":'nedskrivningMarFinOmlopsmidlerField',
        "nedskrivning_fin_anleggsmidler_field":'nedskrivningFinAnleggsmidlerField',
        "rentekostnad_konsern_field":'rentekostnadKonsernField',
        "annen_rentekostnad_field":'annenRentekostnadField',
        "annen_finanskostnad_field":'annenFinanskostnadField',
        "finanskostnad_field":'finanskostnadField',
        "ord_resultat_for_skatt_field":'ordResultatForSkattField',
        "skatt_ord_resultat_field":'skattOrdResultatField',
        "ord_resultat_field":'ordResultatField',
        "ekstraord_inntekt_field":'ekstraordInntektField',
        "ekstraord_kostnad_field":'ekstraordKostnadField',
        "skatt_ekstraord_resultat_field":'skattEkstraordResultatField',
        "sum_skatt_field":'sumSkattField',
        "minoritets_interesser_field":'minoritetsInteresserField',
        "ars_resultat_field":'arsResultatField',
        "konsernbidrag_field":'konsernbidragField',
        "utbytte_field":'utbytteField',
        "til_fond_vurd_for_field":'tilFondVurdForField',
        "til_annen_egenkapital_field":'tilAnnenEgenkapitalField',
        "tap_krav_field":'tapKravField'
    }

    def __init__(self,
                 regnskaps_av_ar_field=None,
                 regnskaps_av_mnd_field=None,
                 totalinntekt_field=None,
                 salgsinntekter_field=None,
                 annen_driftsinntekt_field=None,
                 varekostnad_field=None,
                 beholdningsendring_field=None,
                 lonnskostnad_field=None,
                 avskrivninger_field=None,
                 nedskrivninger_field=None,
                 annen_driftskostnad_field=None,
                 drifts_resultat_field=None,
                 inntekt_inv_datter_field=None,
                 inntekt_inv_konsern_field=None,
                 inntekt_inv_annen_field=None,
                 renteinntekt_konsern_field=None,
                 renteinntekt_annen_field=None,
                 finansinntekt_annen_field=None,
                 finansinntekt_field=None,
                 verdiendring_mar_fin_omlopsmidler_field=None,
                 nedskrivning_mar_fin_omlopsmidler_field=None,
                 nedskrivning_fin_anleggsmidler_field=None,
                 rentekostnad_konsern_field=None,
                 annen_rentekostnad_field=None,
                 annen_finanskostnad_field=None,
                 finanskostnad_field=None,
                 ord_resultat_for_skatt_field=None,
                 skatt_ord_resultat_field=None,
                 ord_resultat_field=None,
                 ekstraord_inntekt_field=None,
                 ekstraord_kostnad_field=None,
                 skatt_ekstraord_resultat_field=None,
                 sum_skatt_field=None,
                 minoritets_interesser_field=None,
                 ars_resultat_field=None,
                 konsernbidrag_field=None,
                 utbytte_field=None,
                 til_fond_vurd_for_field=None,
                 til_annen_egenkapital_field=None,
                 tap_krav_field=None,
                 additional_properties = {}):
        """Constructor for the OkonomiDetaljerKonsern class"""

        # Initialize members of the class
        self.regnskaps_av_ar_field = regnskaps_av_ar_field
        self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        self.totalinntekt_field = totalinntekt_field
        self.salgsinntekter_field = salgsinntekter_field
        self.annen_driftsinntekt_field = annen_driftsinntekt_field
        self.varekostnad_field = varekostnad_field
        self.beholdningsendring_field = beholdningsendring_field
        self.lonnskostnad_field = lonnskostnad_field
        self.avskrivninger_field = avskrivninger_field
        self.nedskrivninger_field = nedskrivninger_field
        self.annen_driftskostnad_field = annen_driftskostnad_field
        self.drifts_resultat_field = drifts_resultat_field
        self.inntekt_inv_datter_field = inntekt_inv_datter_field
        self.inntekt_inv_konsern_field = inntekt_inv_konsern_field
        self.inntekt_inv_annen_field = inntekt_inv_annen_field
        self.renteinntekt_konsern_field = renteinntekt_konsern_field
        self.renteinntekt_annen_field = renteinntekt_annen_field
        self.finansinntekt_annen_field = finansinntekt_annen_field
        self.finansinntekt_field = finansinntekt_field
        self.verdiendring_mar_fin_omlopsmidler_field = verdiendring_mar_fin_omlopsmidler_field
        self.nedskrivning_mar_fin_omlopsmidler_field = nedskrivning_mar_fin_omlopsmidler_field
        self.nedskrivning_fin_anleggsmidler_field = nedskrivning_fin_anleggsmidler_field
        self.rentekostnad_konsern_field = rentekostnad_konsern_field
        self.annen_rentekostnad_field = annen_rentekostnad_field
        self.annen_finanskostnad_field = annen_finanskostnad_field
        self.finanskostnad_field = finanskostnad_field
        self.ord_resultat_for_skatt_field = ord_resultat_for_skatt_field
        self.skatt_ord_resultat_field = skatt_ord_resultat_field
        self.ord_resultat_field = ord_resultat_field
        self.ekstraord_inntekt_field = ekstraord_inntekt_field
        self.ekstraord_kostnad_field = ekstraord_kostnad_field
        self.skatt_ekstraord_resultat_field = skatt_ekstraord_resultat_field
        self.sum_skatt_field = sum_skatt_field
        self.minoritets_interesser_field = minoritets_interesser_field
        self.ars_resultat_field = ars_resultat_field
        self.konsernbidrag_field = konsernbidrag_field
        self.utbytte_field = utbytte_field
        self.til_fond_vurd_for_field = til_fond_vurd_for_field
        self.til_annen_egenkapital_field = til_annen_egenkapital_field
        self.tap_krav_field = tap_krav_field

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
        regnskaps_av_ar_field = dictionary.get('regnskapsAvArField')
        regnskaps_av_mnd_field = dictionary.get('regnskapsAvMndField')
        totalinntekt_field = dictionary.get('totalinntektField')
        salgsinntekter_field = dictionary.get('salgsinntekterField')
        annen_driftsinntekt_field = dictionary.get('annenDriftsinntektField')
        varekostnad_field = dictionary.get('varekostnadField')
        beholdningsendring_field = dictionary.get('beholdningsendringField')
        lonnskostnad_field = dictionary.get('lonnskostnadField')
        avskrivninger_field = dictionary.get('avskrivningerField')
        nedskrivninger_field = dictionary.get('nedskrivningerField')
        annen_driftskostnad_field = dictionary.get('annenDriftskostnadField')
        drifts_resultat_field = dictionary.get('driftsResultatField')
        inntekt_inv_datter_field = dictionary.get('inntektInvDatterField')
        inntekt_inv_konsern_field = dictionary.get('inntektInvKonsernField')
        inntekt_inv_annen_field = dictionary.get('inntektInvAnnenField')
        renteinntekt_konsern_field = dictionary.get('renteinntektKonsernField')
        renteinntekt_annen_field = dictionary.get('renteinntektAnnenField')
        finansinntekt_annen_field = dictionary.get('finansinntektAnnenField')
        finansinntekt_field = dictionary.get('finansinntektField')
        verdiendring_mar_fin_omlopsmidler_field = dictionary.get('verdiendringMarFinOmlopsmidlerField')
        nedskrivning_mar_fin_omlopsmidler_field = dictionary.get('nedskrivningMarFinOmlopsmidlerField')
        nedskrivning_fin_anleggsmidler_field = dictionary.get('nedskrivningFinAnleggsmidlerField')
        rentekostnad_konsern_field = dictionary.get('rentekostnadKonsernField')
        annen_rentekostnad_field = dictionary.get('annenRentekostnadField')
        annen_finanskostnad_field = dictionary.get('annenFinanskostnadField')
        finanskostnad_field = dictionary.get('finanskostnadField')
        ord_resultat_for_skatt_field = dictionary.get('ordResultatForSkattField')
        skatt_ord_resultat_field = dictionary.get('skattOrdResultatField')
        ord_resultat_field = dictionary.get('ordResultatField')
        ekstraord_inntekt_field = dictionary.get('ekstraordInntektField')
        ekstraord_kostnad_field = dictionary.get('ekstraordKostnadField')
        skatt_ekstraord_resultat_field = dictionary.get('skattEkstraordResultatField')
        sum_skatt_field = dictionary.get('sumSkattField')
        minoritets_interesser_field = dictionary.get('minoritetsInteresserField')
        ars_resultat_field = dictionary.get('arsResultatField')
        konsernbidrag_field = dictionary.get('konsernbidragField')
        utbytte_field = dictionary.get('utbytteField')
        til_fond_vurd_for_field = dictionary.get('tilFondVurdForField')
        til_annen_egenkapital_field = dictionary.get('tilAnnenEgenkapitalField')
        tap_krav_field = dictionary.get('tapKravField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(regnskaps_av_ar_field,
                   regnskaps_av_mnd_field,
                   totalinntekt_field,
                   salgsinntekter_field,
                   annen_driftsinntekt_field,
                   varekostnad_field,
                   beholdningsendring_field,
                   lonnskostnad_field,
                   avskrivninger_field,
                   nedskrivninger_field,
                   annen_driftskostnad_field,
                   drifts_resultat_field,
                   inntekt_inv_datter_field,
                   inntekt_inv_konsern_field,
                   inntekt_inv_annen_field,
                   renteinntekt_konsern_field,
                   renteinntekt_annen_field,
                   finansinntekt_annen_field,
                   finansinntekt_field,
                   verdiendring_mar_fin_omlopsmidler_field,
                   nedskrivning_mar_fin_omlopsmidler_field,
                   nedskrivning_fin_anleggsmidler_field,
                   rentekostnad_konsern_field,
                   annen_rentekostnad_field,
                   annen_finanskostnad_field,
                   finanskostnad_field,
                   ord_resultat_for_skatt_field,
                   skatt_ord_resultat_field,
                   ord_resultat_field,
                   ekstraord_inntekt_field,
                   ekstraord_kostnad_field,
                   skatt_ekstraord_resultat_field,
                   sum_skatt_field,
                   minoritets_interesser_field,
                   ars_resultat_field,
                   konsernbidrag_field,
                   utbytte_field,
                   til_fond_vurd_for_field,
                   til_annen_egenkapital_field,
                   tap_krav_field,
                   dictionary)


