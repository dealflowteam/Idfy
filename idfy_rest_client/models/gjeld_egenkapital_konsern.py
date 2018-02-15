# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.gjeld_egenkapital_konsern

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class GjeldEgenkapitalKonsern(object):

    """Implementation of the 'GjeldEgenkapitalKonsern' model.

    TODO: type model description here.

    Attributes:
        regnskaps_av_ar_field (int): TODO: type description here.
        regnskaps_av_mnd_field (int): TODO: type description here.
        sum_egenkapital_field (long|int): TODO: type description here.
        innskutt_egenkapital_field (long|int): TODO: type description here.
        selskapskapital_field (long|int): TODO: type description here.
        egne_aksjer_field (long|int): TODO: type description here.
        overkursfond_field (long|int): TODO: type description here.
        opptjent_egenkapital_field (long|int): TODO: type description here.
        fond_for_vurd_field (long|int): TODO: type description here.
        annen_egenkapital_field (long|int): TODO: type description here.
        minoritetsinteresser_field (long|int): TODO: type description here.
        sum_gjeld_field (long|int): TODO: type description here.
        avsetning_forpliktelser_field (long|int): TODO: type description
            here.
        pensjon_forpliktelser_field (long|int): TODO: type description here.
        utsatt_skatt_field (long|int): TODO: type description here.
        andre_avsetninger_field (long|int): TODO: type description here.
        sum_langsiktig_gjeld_field (long|int): TODO: type description here.
        annen_langsiktig_gjeld_field (long|int): TODO: type description here.
        konvertible_lan_lang_field (long|int): TODO: type description here.
        obligasjons_lan_field (long|int): TODO: type description here.
        gjeld_kreditt_lang_field (long|int): TODO: type description here.
        gjeld_konsern_lang_field (long|int): TODO: type description here.
        ansvarlig_lanekapital_field (long|int): TODO: type description here.
        ovrig_langsiktig_gjeld_field (long|int): TODO: type description here.
        sum_kortsiktig_gjeld_field (long|int): TODO: type description here.
        konvertible_lan_kort_field (long|int): TODO: type description here.
        sertifikat_lan_field (long|int): TODO: type description here.
        gjeld_kreditt_kort_field (long|int): TODO: type description here.
        kassakreditt_field (long|int): TODO: type description here.
        leverandor_gjeld_field (long|int): TODO: type description here.
        betalbar_skatt_field (long|int): TODO: type description here.
        skyld_offentlig_avgift_field (long|int): TODO: type description here.
        gjeld_konsern_kort_field (long|int): TODO: type description here.
        utbytte_field (long|int): TODO: type description here.
        annen_kortsiktig_gjeld_field (long|int): TODO: type description here.
        sum_gjeld_egenkapital_field (long|int): TODO: type description here.
        kassekredittlimit_field (long|int): TODO: type description here.
        skyld_konsernbidrag_field (long|int): TODO: type description here.
        avdrag_langsiktig_gjeld_field (long|int): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "regnskaps_av_ar_field":'regnskapsAvArField',
        "regnskaps_av_mnd_field":'regnskapsAvMndField',
        "sum_egenkapital_field":'sumEgenkapitalField',
        "innskutt_egenkapital_field":'innskuttEgenkapitalField',
        "selskapskapital_field":'selskapskapitalField',
        "egne_aksjer_field":'egneAksjerField',
        "overkursfond_field":'overkursfondField',
        "opptjent_egenkapital_field":'opptjentEgenkapitalField',
        "fond_for_vurd_field":'fondForVurdField',
        "annen_egenkapital_field":'annenEgenkapitalField',
        "minoritetsinteresser_field":'minoritetsinteresserField',
        "sum_gjeld_field":'sumGjeldField',
        "avsetning_forpliktelser_field":'avsetningForpliktelserField',
        "pensjon_forpliktelser_field":'pensjonForpliktelserField',
        "utsatt_skatt_field":'utsattSkattField',
        "andre_avsetninger_field":'andreAvsetningerField',
        "sum_langsiktig_gjeld_field":'sumLangsiktigGjeldField',
        "annen_langsiktig_gjeld_field":'annenLangsiktigGjeldField',
        "konvertible_lan_lang_field":'konvertibleLanLangField',
        "obligasjons_lan_field":'obligasjonsLanField',
        "gjeld_kreditt_lang_field":'gjeldKredittLangField',
        "gjeld_konsern_lang_field":'gjeldKonsernLangField',
        "ansvarlig_lanekapital_field":'ansvarligLanekapitalField',
        "ovrig_langsiktig_gjeld_field":'ovrigLangsiktigGjeldField',
        "sum_kortsiktig_gjeld_field":'sumKortsiktigGjeldField',
        "konvertible_lan_kort_field":'konvertibleLanKortField',
        "sertifikat_lan_field":'sertifikatLanField',
        "gjeld_kreditt_kort_field":'gjeldKredittKortField',
        "kassakreditt_field":'kassakredittField',
        "leverandor_gjeld_field":'leverandorGjeldField',
        "betalbar_skatt_field":'betalbarSkattField',
        "skyld_offentlig_avgift_field":'skyldOffentligAvgiftField',
        "gjeld_konsern_kort_field":'gjeldKonsernKortField',
        "utbytte_field":'utbytteField',
        "annen_kortsiktig_gjeld_field":'annenKortsiktigGjeldField',
        "sum_gjeld_egenkapital_field":'sumGjeldEgenkapitalField',
        "kassekredittlimit_field":'kassekredittlimitField',
        "skyld_konsernbidrag_field":'skyldKonsernbidragField',
        "avdrag_langsiktig_gjeld_field":'avdragLangsiktigGjeldField'
    }

    def __init__(self,
                 regnskaps_av_ar_field=None,
                 regnskaps_av_mnd_field=None,
                 sum_egenkapital_field=None,
                 innskutt_egenkapital_field=None,
                 selskapskapital_field=None,
                 egne_aksjer_field=None,
                 overkursfond_field=None,
                 opptjent_egenkapital_field=None,
                 fond_for_vurd_field=None,
                 annen_egenkapital_field=None,
                 minoritetsinteresser_field=None,
                 sum_gjeld_field=None,
                 avsetning_forpliktelser_field=None,
                 pensjon_forpliktelser_field=None,
                 utsatt_skatt_field=None,
                 andre_avsetninger_field=None,
                 sum_langsiktig_gjeld_field=None,
                 annen_langsiktig_gjeld_field=None,
                 konvertible_lan_lang_field=None,
                 obligasjons_lan_field=None,
                 gjeld_kreditt_lang_field=None,
                 gjeld_konsern_lang_field=None,
                 ansvarlig_lanekapital_field=None,
                 ovrig_langsiktig_gjeld_field=None,
                 sum_kortsiktig_gjeld_field=None,
                 konvertible_lan_kort_field=None,
                 sertifikat_lan_field=None,
                 gjeld_kreditt_kort_field=None,
                 kassakreditt_field=None,
                 leverandor_gjeld_field=None,
                 betalbar_skatt_field=None,
                 skyld_offentlig_avgift_field=None,
                 gjeld_konsern_kort_field=None,
                 utbytte_field=None,
                 annen_kortsiktig_gjeld_field=None,
                 sum_gjeld_egenkapital_field=None,
                 kassekredittlimit_field=None,
                 skyld_konsernbidrag_field=None,
                 avdrag_langsiktig_gjeld_field=None,
                 additional_properties = {}):
        """Constructor for the GjeldEgenkapitalKonsern class"""

        # Initialize members of the class
        self.regnskaps_av_ar_field = regnskaps_av_ar_field
        self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        self.sum_egenkapital_field = sum_egenkapital_field
        self.innskutt_egenkapital_field = innskutt_egenkapital_field
        self.selskapskapital_field = selskapskapital_field
        self.egne_aksjer_field = egne_aksjer_field
        self.overkursfond_field = overkursfond_field
        self.opptjent_egenkapital_field = opptjent_egenkapital_field
        self.fond_for_vurd_field = fond_for_vurd_field
        self.annen_egenkapital_field = annen_egenkapital_field
        self.minoritetsinteresser_field = minoritetsinteresser_field
        self.sum_gjeld_field = sum_gjeld_field
        self.avsetning_forpliktelser_field = avsetning_forpliktelser_field
        self.pensjon_forpliktelser_field = pensjon_forpliktelser_field
        self.utsatt_skatt_field = utsatt_skatt_field
        self.andre_avsetninger_field = andre_avsetninger_field
        self.sum_langsiktig_gjeld_field = sum_langsiktig_gjeld_field
        self.annen_langsiktig_gjeld_field = annen_langsiktig_gjeld_field
        self.konvertible_lan_lang_field = konvertible_lan_lang_field
        self.obligasjons_lan_field = obligasjons_lan_field
        self.gjeld_kreditt_lang_field = gjeld_kreditt_lang_field
        self.gjeld_konsern_lang_field = gjeld_konsern_lang_field
        self.ansvarlig_lanekapital_field = ansvarlig_lanekapital_field
        self.ovrig_langsiktig_gjeld_field = ovrig_langsiktig_gjeld_field
        self.sum_kortsiktig_gjeld_field = sum_kortsiktig_gjeld_field
        self.konvertible_lan_kort_field = konvertible_lan_kort_field
        self.sertifikat_lan_field = sertifikat_lan_field
        self.gjeld_kreditt_kort_field = gjeld_kreditt_kort_field
        self.kassakreditt_field = kassakreditt_field
        self.leverandor_gjeld_field = leverandor_gjeld_field
        self.betalbar_skatt_field = betalbar_skatt_field
        self.skyld_offentlig_avgift_field = skyld_offentlig_avgift_field
        self.gjeld_konsern_kort_field = gjeld_konsern_kort_field
        self.utbytte_field = utbytte_field
        self.annen_kortsiktig_gjeld_field = annen_kortsiktig_gjeld_field
        self.sum_gjeld_egenkapital_field = sum_gjeld_egenkapital_field
        self.kassekredittlimit_field = kassekredittlimit_field
        self.skyld_konsernbidrag_field = skyld_konsernbidrag_field
        self.avdrag_langsiktig_gjeld_field = avdrag_langsiktig_gjeld_field

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
        sum_egenkapital_field = dictionary.get('sumEgenkapitalField')
        innskutt_egenkapital_field = dictionary.get('innskuttEgenkapitalField')
        selskapskapital_field = dictionary.get('selskapskapitalField')
        egne_aksjer_field = dictionary.get('egneAksjerField')
        overkursfond_field = dictionary.get('overkursfondField')
        opptjent_egenkapital_field = dictionary.get('opptjentEgenkapitalField')
        fond_for_vurd_field = dictionary.get('fondForVurdField')
        annen_egenkapital_field = dictionary.get('annenEgenkapitalField')
        minoritetsinteresser_field = dictionary.get('minoritetsinteresserField')
        sum_gjeld_field = dictionary.get('sumGjeldField')
        avsetning_forpliktelser_field = dictionary.get('avsetningForpliktelserField')
        pensjon_forpliktelser_field = dictionary.get('pensjonForpliktelserField')
        utsatt_skatt_field = dictionary.get('utsattSkattField')
        andre_avsetninger_field = dictionary.get('andreAvsetningerField')
        sum_langsiktig_gjeld_field = dictionary.get('sumLangsiktigGjeldField')
        annen_langsiktig_gjeld_field = dictionary.get('annenLangsiktigGjeldField')
        konvertible_lan_lang_field = dictionary.get('konvertibleLanLangField')
        obligasjons_lan_field = dictionary.get('obligasjonsLanField')
        gjeld_kreditt_lang_field = dictionary.get('gjeldKredittLangField')
        gjeld_konsern_lang_field = dictionary.get('gjeldKonsernLangField')
        ansvarlig_lanekapital_field = dictionary.get('ansvarligLanekapitalField')
        ovrig_langsiktig_gjeld_field = dictionary.get('ovrigLangsiktigGjeldField')
        sum_kortsiktig_gjeld_field = dictionary.get('sumKortsiktigGjeldField')
        konvertible_lan_kort_field = dictionary.get('konvertibleLanKortField')
        sertifikat_lan_field = dictionary.get('sertifikatLanField')
        gjeld_kreditt_kort_field = dictionary.get('gjeldKredittKortField')
        kassakreditt_field = dictionary.get('kassakredittField')
        leverandor_gjeld_field = dictionary.get('leverandorGjeldField')
        betalbar_skatt_field = dictionary.get('betalbarSkattField')
        skyld_offentlig_avgift_field = dictionary.get('skyldOffentligAvgiftField')
        gjeld_konsern_kort_field = dictionary.get('gjeldKonsernKortField')
        utbytte_field = dictionary.get('utbytteField')
        annen_kortsiktig_gjeld_field = dictionary.get('annenKortsiktigGjeldField')
        sum_gjeld_egenkapital_field = dictionary.get('sumGjeldEgenkapitalField')
        kassekredittlimit_field = dictionary.get('kassekredittlimitField')
        skyld_konsernbidrag_field = dictionary.get('skyldKonsernbidragField')
        avdrag_langsiktig_gjeld_field = dictionary.get('avdragLangsiktigGjeldField')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(regnskaps_av_ar_field,
                   regnskaps_av_mnd_field,
                   sum_egenkapital_field,
                   innskutt_egenkapital_field,
                   selskapskapital_field,
                   egne_aksjer_field,
                   overkursfond_field,
                   opptjent_egenkapital_field,
                   fond_for_vurd_field,
                   annen_egenkapital_field,
                   minoritetsinteresser_field,
                   sum_gjeld_field,
                   avsetning_forpliktelser_field,
                   pensjon_forpliktelser_field,
                   utsatt_skatt_field,
                   andre_avsetninger_field,
                   sum_langsiktig_gjeld_field,
                   annen_langsiktig_gjeld_field,
                   konvertible_lan_lang_field,
                   obligasjons_lan_field,
                   gjeld_kreditt_lang_field,
                   gjeld_konsern_lang_field,
                   ansvarlig_lanekapital_field,
                   ovrig_langsiktig_gjeld_field,
                   sum_kortsiktig_gjeld_field,
                   konvertible_lan_kort_field,
                   sertifikat_lan_field,
                   gjeld_kreditt_kort_field,
                   kassakreditt_field,
                   leverandor_gjeld_field,
                   betalbar_skatt_field,
                   skyld_offentlig_avgift_field,
                   gjeld_konsern_kort_field,
                   utbytte_field,
                   annen_kortsiktig_gjeld_field,
                   sum_gjeld_egenkapital_field,
                   kassekredittlimit_field,
                   skyld_konsernbidrag_field,
                   avdrag_langsiktig_gjeld_field,
                   dictionary)


