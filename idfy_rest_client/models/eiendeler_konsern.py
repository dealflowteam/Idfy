# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.eiendeler_konsern

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class EiendelerKonsern(object):

    """Implementation of the 'EiendelerKonsern' model.

    TODO: type model description here.

    Attributes:
        regnskaps_av_ar_field (int): TODO: type description here.
        regnskaps_av_mnd_field (int): TODO: type description here.
        sum_anleggsmidler_field (long|int): TODO: type description here.
        sum_immatrielle_eiendeler_field (long|int): TODO: type description
            here.
        forskning_utvikling_field (long|int): TODO: type description here.
        konsesjoner_field (long|int): TODO: type description here.
        utsatt_skattefordel_field (long|int): TODO: type description here.
        goodwill_field (long|int): TODO: type description here.
        sum_varige_driftsmidler_field (long|int): TODO: type description
            here.
        fast_eiendom_field (long|int): TODO: type description here.
        maskiner_anlegg_field (long|int): TODO: type description here.
        skip_rigg_fly_field (long|int): TODO: type description here.
        drifts_losore_field (long|int): TODO: type description here.
        sum_finansielle_anleggsmilder_field (long|int): TODO: type description
            here.
        invest_datter_field (long|int): TODO: type description here.
        invest_annet_konsern_field (long|int): TODO: type description here.
        konsernfordring_field (long|int): TODO: type description here.
        invest_tilknyttet_field (long|int): TODO: type description here.
        lan_tilknyttet_field (long|int): TODO: type description here.
        invest_aksjer_field (long|int): TODO: type description here.
        obligasjoner_field (long|int): TODO: type description here.
        pensjonsmidler_field (long|int): TODO: type description here.
        andre_anleggsmidler_field (long|int): TODO: type description here.
        sum_omlopsmidler_field (long|int): TODO: type description here.
        sum_varer_field (long|int): TODO: type description here.
        lager_ravarer_field (long|int): TODO: type description here.
        lager_uferdige_varer_field (long|int): TODO: type description here.
        lager_ferdige_varer_field (long|int): TODO: type description here.
        sum_fordringer_field (long|int): TODO: type description here.
        fordringer_kunder_field (long|int): TODO: type description here.
        fordringer_andre_field (long|int): TODO: type description here.
        fordringer_konsern_field (long|int): TODO: type description here.
        krav_innbet_selskapskapital_field (long|int): TODO: type description
            here.
        sum_investeringer_field (long|int): TODO: type description here.
        aksjer_konsern_field (long|int): TODO: type description here.
        aksjer_marked_field (long|int): TODO: type description here.
        obligasjoner_marked_field (long|int): TODO: type description here.
        andre_marked_fin_inv_field (long|int): TODO: type description here.
        andre_fin_inst_field (long|int): TODO: type description here.
        bankinnskudd_field (long|int): TODO: type description here.
        andre_omlopsmidler_field (long|int): TODO: type description here.
        sum_eiendeler_field (long|int): TODO: type description here.
        pantstillelser_field (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "regnskaps_av_ar_field":'regnskapsAvArField',
        "regnskaps_av_mnd_field":'regnskapsAvMndField',
        "sum_anleggsmidler_field":'sumAnleggsmidlerField',
        "sum_immatrielle_eiendeler_field":'sumImmatrielleEiendelerField',
        "forskning_utvikling_field":'forskningUtviklingField',
        "konsesjoner_field":'konsesjonerField',
        "utsatt_skattefordel_field":'utsattSkattefordelField',
        "goodwill_field":'goodwillField',
        "sum_varige_driftsmidler_field":'sumVarigeDriftsmidlerField',
        "fast_eiendom_field":'fastEiendomField',
        "maskiner_anlegg_field":'maskinerAnleggField',
        "skip_rigg_fly_field":'skipRiggFlyField',
        "drifts_losore_field":'driftsLosoreField',
        "sum_finansielle_anleggsmilder_field":'sumFinansielleAnleggsmilderField',
        "invest_datter_field":'investDatterField',
        "invest_annet_konsern_field":'investAnnetKonsernField',
        "konsernfordring_field":'konsernfordringField',
        "invest_tilknyttet_field":'investTilknyttetField',
        "lan_tilknyttet_field":'lanTilknyttetField',
        "invest_aksjer_field":'investAksjerField',
        "obligasjoner_field":'obligasjonerField',
        "pensjonsmidler_field":'pensjonsmidlerField',
        "andre_anleggsmidler_field":'andreAnleggsmidlerField',
        "sum_omlopsmidler_field":'sumOmlopsmidlerField',
        "sum_varer_field":'sumVarerField',
        "lager_ravarer_field":'lagerRavarerField',
        "lager_uferdige_varer_field":'lagerUferdigeVarerField',
        "lager_ferdige_varer_field":'lagerFerdigeVarerField',
        "sum_fordringer_field":'sumFordringerField',
        "fordringer_kunder_field":'fordringerKunderField',
        "fordringer_andre_field":'fordringerAndreField',
        "fordringer_konsern_field":'fordringerKonsernField',
        "krav_innbet_selskapskapital_field":'kravInnbetSelskapskapitalField',
        "sum_investeringer_field":'sumInvesteringerField',
        "aksjer_konsern_field":'aksjerKonsernField',
        "aksjer_marked_field":'aksjerMarkedField',
        "obligasjoner_marked_field":'obligasjonerMarkedField',
        "andre_marked_fin_inv_field":'andreMarkedFinInvField',
        "andre_fin_inst_field":'andreFinInstField',
        "bankinnskudd_field":'bankinnskuddField',
        "andre_omlopsmidler_field":'andreOmlopsmidlerField',
        "sum_eiendeler_field":'sumEiendelerField',
        "pantstillelser_field":'pantstillelserField'
    }

    def __init__(self,
                 regnskaps_av_ar_field=None,
                 regnskaps_av_mnd_field=None,
                 sum_anleggsmidler_field=None,
                 sum_immatrielle_eiendeler_field=None,
                 forskning_utvikling_field=None,
                 konsesjoner_field=None,
                 utsatt_skattefordel_field=None,
                 goodwill_field=None,
                 sum_varige_driftsmidler_field=None,
                 fast_eiendom_field=None,
                 maskiner_anlegg_field=None,
                 skip_rigg_fly_field=None,
                 drifts_losore_field=None,
                 sum_finansielle_anleggsmilder_field=None,
                 invest_datter_field=None,
                 invest_annet_konsern_field=None,
                 konsernfordring_field=None,
                 invest_tilknyttet_field=None,
                 lan_tilknyttet_field=None,
                 invest_aksjer_field=None,
                 obligasjoner_field=None,
                 pensjonsmidler_field=None,
                 andre_anleggsmidler_field=None,
                 sum_omlopsmidler_field=None,
                 sum_varer_field=None,
                 lager_ravarer_field=None,
                 lager_uferdige_varer_field=None,
                 lager_ferdige_varer_field=None,
                 sum_fordringer_field=None,
                 fordringer_kunder_field=None,
                 fordringer_andre_field=None,
                 fordringer_konsern_field=None,
                 krav_innbet_selskapskapital_field=None,
                 sum_investeringer_field=None,
                 aksjer_konsern_field=None,
                 aksjer_marked_field=None,
                 obligasjoner_marked_field=None,
                 andre_marked_fin_inv_field=None,
                 andre_fin_inst_field=None,
                 bankinnskudd_field=None,
                 andre_omlopsmidler_field=None,
                 sum_eiendeler_field=None,
                 pantstillelser_field=None,
                 additional_properties = {}):
        """Constructor for the EiendelerKonsern class"""

        # Initialize members of the class
        self.regnskaps_av_ar_field = regnskaps_av_ar_field
        self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        self.sum_anleggsmidler_field = sum_anleggsmidler_field
        self.sum_immatrielle_eiendeler_field = sum_immatrielle_eiendeler_field
        self.forskning_utvikling_field = forskning_utvikling_field
        self.konsesjoner_field = konsesjoner_field
        self.utsatt_skattefordel_field = utsatt_skattefordel_field
        self.goodwill_field = goodwill_field
        self.sum_varige_driftsmidler_field = sum_varige_driftsmidler_field
        self.fast_eiendom_field = fast_eiendom_field
        self.maskiner_anlegg_field = maskiner_anlegg_field
        self.skip_rigg_fly_field = skip_rigg_fly_field
        self.drifts_losore_field = drifts_losore_field
        self.sum_finansielle_anleggsmilder_field = sum_finansielle_anleggsmilder_field
        self.invest_datter_field = invest_datter_field
        self.invest_annet_konsern_field = invest_annet_konsern_field
        self.konsernfordring_field = konsernfordring_field
        self.invest_tilknyttet_field = invest_tilknyttet_field
        self.lan_tilknyttet_field = lan_tilknyttet_field
        self.invest_aksjer_field = invest_aksjer_field
        self.obligasjoner_field = obligasjoner_field
        self.pensjonsmidler_field = pensjonsmidler_field
        self.andre_anleggsmidler_field = andre_anleggsmidler_field
        self.sum_omlopsmidler_field = sum_omlopsmidler_field
        self.sum_varer_field = sum_varer_field
        self.lager_ravarer_field = lager_ravarer_field
        self.lager_uferdige_varer_field = lager_uferdige_varer_field
        self.lager_ferdige_varer_field = lager_ferdige_varer_field
        self.sum_fordringer_field = sum_fordringer_field
        self.fordringer_kunder_field = fordringer_kunder_field
        self.fordringer_andre_field = fordringer_andre_field
        self.fordringer_konsern_field = fordringer_konsern_field
        self.krav_innbet_selskapskapital_field = krav_innbet_selskapskapital_field
        self.sum_investeringer_field = sum_investeringer_field
        self.aksjer_konsern_field = aksjer_konsern_field
        self.aksjer_marked_field = aksjer_marked_field
        self.obligasjoner_marked_field = obligasjoner_marked_field
        self.andre_marked_fin_inv_field = andre_marked_fin_inv_field
        self.andre_fin_inst_field = andre_fin_inst_field
        self.bankinnskudd_field = bankinnskudd_field
        self.andre_omlopsmidler_field = andre_omlopsmidler_field
        self.sum_eiendeler_field = sum_eiendeler_field
        self.pantstillelser_field = pantstillelser_field

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
        sum_anleggsmidler_field = dictionary.get('sumAnleggsmidlerField')
        sum_immatrielle_eiendeler_field = dictionary.get('sumImmatrielleEiendelerField')
        forskning_utvikling_field = dictionary.get('forskningUtviklingField')
        konsesjoner_field = dictionary.get('konsesjonerField')
        utsatt_skattefordel_field = dictionary.get('utsattSkattefordelField')
        goodwill_field = dictionary.get('goodwillField')
        sum_varige_driftsmidler_field = dictionary.get('sumVarigeDriftsmidlerField')
        fast_eiendom_field = dictionary.get('fastEiendomField')
        maskiner_anlegg_field = dictionary.get('maskinerAnleggField')
        skip_rigg_fly_field = dictionary.get('skipRiggFlyField')
        drifts_losore_field = dictionary.get('driftsLosoreField')
        sum_finansielle_anleggsmilder_field = dictionary.get('sumFinansielleAnleggsmilderField')
        invest_datter_field = dictionary.get('investDatterField')
        invest_annet_konsern_field = dictionary.get('investAnnetKonsernField')
        konsernfordring_field = dictionary.get('konsernfordringField')
        invest_tilknyttet_field = dictionary.get('investTilknyttetField')
        lan_tilknyttet_field = dictionary.get('lanTilknyttetField')
        invest_aksjer_field = dictionary.get('investAksjerField')
        obligasjoner_field = dictionary.get('obligasjonerField')
        pensjonsmidler_field = dictionary.get('pensjonsmidlerField')
        andre_anleggsmidler_field = dictionary.get('andreAnleggsmidlerField')
        sum_omlopsmidler_field = dictionary.get('sumOmlopsmidlerField')
        sum_varer_field = dictionary.get('sumVarerField')
        lager_ravarer_field = dictionary.get('lagerRavarerField')
        lager_uferdige_varer_field = dictionary.get('lagerUferdigeVarerField')
        lager_ferdige_varer_field = dictionary.get('lagerFerdigeVarerField')
        sum_fordringer_field = dictionary.get('sumFordringerField')
        fordringer_kunder_field = dictionary.get('fordringerKunderField')
        fordringer_andre_field = dictionary.get('fordringerAndreField')
        fordringer_konsern_field = dictionary.get('fordringerKonsernField')
        krav_innbet_selskapskapital_field = dictionary.get('kravInnbetSelskapskapitalField')
        sum_investeringer_field = dictionary.get('sumInvesteringerField')
        aksjer_konsern_field = dictionary.get('aksjerKonsernField')
        aksjer_marked_field = dictionary.get('aksjerMarkedField')
        obligasjoner_marked_field = dictionary.get('obligasjonerMarkedField')
        andre_marked_fin_inv_field = dictionary.get('andreMarkedFinInvField')
        andre_fin_inst_field = dictionary.get('andreFinInstField')
        bankinnskudd_field = dictionary.get('bankinnskuddField')
        andre_omlopsmidler_field = dictionary.get('andreOmlopsmidlerField')
        sum_eiendeler_field = dictionary.get('sumEiendelerField')
        pantstillelser_field = dictionary.get('pantstillelserField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(regnskaps_av_ar_field,
                   regnskaps_av_mnd_field,
                   sum_anleggsmidler_field,
                   sum_immatrielle_eiendeler_field,
                   forskning_utvikling_field,
                   konsesjoner_field,
                   utsatt_skattefordel_field,
                   goodwill_field,
                   sum_varige_driftsmidler_field,
                   fast_eiendom_field,
                   maskiner_anlegg_field,
                   skip_rigg_fly_field,
                   drifts_losore_field,
                   sum_finansielle_anleggsmilder_field,
                   invest_datter_field,
                   invest_annet_konsern_field,
                   konsernfordring_field,
                   invest_tilknyttet_field,
                   lan_tilknyttet_field,
                   invest_aksjer_field,
                   obligasjoner_field,
                   pensjonsmidler_field,
                   andre_anleggsmidler_field,
                   sum_omlopsmidler_field,
                   sum_varer_field,
                   lager_ravarer_field,
                   lager_uferdige_varer_field,
                   lager_ferdige_varer_field,
                   sum_fordringer_field,
                   fordringer_kunder_field,
                   fordringer_andre_field,
                   fordringer_konsern_field,
                   krav_innbet_selskapskapital_field,
                   sum_investeringer_field,
                   aksjer_konsern_field,
                   aksjer_marked_field,
                   obligasjoner_marked_field,
                   andre_marked_fin_inv_field,
                   andre_fin_inst_field,
                   bankinnskudd_field,
                   andre_omlopsmidler_field,
                   sum_eiendeler_field,
                   pantstillelser_field,
                   dictionary)


