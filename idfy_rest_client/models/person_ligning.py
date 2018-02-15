# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.person_ligning

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class PersonLigning(object):

    """Implementation of the 'Person.Ligning' model.

    TODO: type model description here.

    Attributes:
        skatte_ar_field (int): TODO: type description here.
        formue_field (long|int): TODO: type description here.
        endring_formue_field (float): TODO: type description here.
        inntekt_field (long|int): TODO: type description here.
        endring_inntekt_field (float): TODO: type description here.
        skatt_field (long|int): TODO: type description here.
        skatte_klasse_field (string): TODO: type description here.
        skatte_klasse_utl_field (string): TODO: type description here.
        kommunenr_field (string): TODO: type description here.
        kommune_navn_field (string): TODO: type description here.
        brutto_inntekt_field (long|int): TODO: type description here.
        gjeldsgrad_1_field (float): TODO: type description here.
        gjeldsgrad_2_field (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "skatte_ar_field":'skatteArField',
        "formue_field":'formueField',
        "endring_formue_field":'endringFormueField',
        "inntekt_field":'inntektField',
        "endring_inntekt_field":'endringInntektField',
        "skatt_field":'skattField',
        "skatte_klasse_field":'skatteKlasseField',
        "skatte_klasse_utl_field":'skatteKlasseUtlField',
        "kommunenr_field":'kommunenrField',
        "kommune_navn_field":'kommuneNavnField',
        "brutto_inntekt_field":'bruttoInntektField',
        "gjeldsgrad_1_field":'gjeldsgrad1Field',
        "gjeldsgrad_2_field":'gjeldsgrad2Field'
    }

    def __init__(self,
                 skatte_ar_field=None,
                 formue_field=None,
                 endring_formue_field=None,
                 inntekt_field=None,
                 endring_inntekt_field=None,
                 skatt_field=None,
                 skatte_klasse_field=None,
                 skatte_klasse_utl_field=None,
                 kommunenr_field=None,
                 kommune_navn_field=None,
                 brutto_inntekt_field=None,
                 gjeldsgrad_1_field=None,
                 gjeldsgrad_2_field=None,
                 additional_properties = {}):
        """Constructor for the PersonLigning class"""

        # Initialize members of the class
        self.skatte_ar_field = skatte_ar_field
        self.formue_field = formue_field
        self.endring_formue_field = endring_formue_field
        self.inntekt_field = inntekt_field
        self.endring_inntekt_field = endring_inntekt_field
        self.skatt_field = skatt_field
        self.skatte_klasse_field = skatte_klasse_field
        self.skatte_klasse_utl_field = skatte_klasse_utl_field
        self.kommunenr_field = kommunenr_field
        self.kommune_navn_field = kommune_navn_field
        self.brutto_inntekt_field = brutto_inntekt_field
        self.gjeldsgrad_1_field = gjeldsgrad_1_field
        self.gjeldsgrad_2_field = gjeldsgrad_2_field

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
        skatte_ar_field = dictionary.get('skatteArField')
        formue_field = dictionary.get('formueField')
        endring_formue_field = dictionary.get('endringFormueField')
        inntekt_field = dictionary.get('inntektField')
        endring_inntekt_field = dictionary.get('endringInntektField')
        skatt_field = dictionary.get('skattField')
        skatte_klasse_field = dictionary.get('skatteKlasseField')
        skatte_klasse_utl_field = dictionary.get('skatteKlasseUtlField')
        kommunenr_field = dictionary.get('kommunenrField')
        kommune_navn_field = dictionary.get('kommuneNavnField')
        brutto_inntekt_field = dictionary.get('bruttoInntektField')
        gjeldsgrad_1_field = dictionary.get('gjeldsgrad1Field')
        gjeldsgrad_2_field = dictionary.get('gjeldsgrad2Field')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(skatte_ar_field,
                   formue_field,
                   endring_formue_field,
                   inntekt_field,
                   endring_inntekt_field,
                   skatt_field,
                   skatte_klasse_field,
                   skatte_klasse_utl_field,
                   kommunenr_field,
                   kommune_navn_field,
                   brutto_inntekt_field,
                   gjeldsgrad_1_field,
                   gjeldsgrad_2_field,
                   dictionary)


