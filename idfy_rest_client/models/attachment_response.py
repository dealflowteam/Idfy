# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.attachment_response

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class AttachmentResponse(object):

    """Implementation of the 'AttachmentResponse' model.

    TODO: type model description here.

    Attributes:
        file_name (string): Filename with file extension. <span
            style="color:red;">We only support PDF for attachments</span>
        title (string): Give the attachment a title that will be presented to
            the user
        data (string): base 64 encoded attachment (utf-8)
        id (uuid|string): TODO: type description here.
        signers (list of uuid|string): Optional: Specify which signers that
            should be able to see / sign this attachment
        description (string): Optional: An optional description of the
            document
        mtype (Type): Choose between the following:  * <b>show_accept:</b> The
            signer will see the attachment before signing the main document
            (is default now)  * <b>read_accept:</b> The signer have to see the
            entire document before they can continue,   * <b>sign:</b> The
            signer has to sign the attachment (extra cost per signature)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_name":'fileName',
        "title":'title',
        "data":'data',
        "id":'id',
        "signers":'signers',
        "description":'description',
        "mtype":'type'
    }

    def __init__(self,
                 file_name=None,
                 title=None,
                 data=None,
                 id=None,
                 signers=None,
                 description=None,
                 mtype=None,
                 additional_properties = {}):
        """Constructor for the AttachmentResponse class"""

        # Initialize members of the class
        self.file_name = file_name
        self.title = title
        self.data = data
        self.id = id
        self.signers = signers
        self.description = description
        self.mtype = mtype

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
        file_name = dictionary.get('fileName')
        title = dictionary.get('title')
        data = dictionary.get('data')
        id = dictionary.get('id')
        signers = dictionary.get('signers')
        description = dictionary.get('description')
        mtype = dictionary.get('type')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(file_name,
                   title,
                   data,
                   id,
                   signers,
                   description,
                   mtype,
                   dictionary)


