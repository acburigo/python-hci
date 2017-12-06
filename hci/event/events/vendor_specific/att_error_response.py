from struct import unpack_from

from .. import VendorSpecificEvent


class ATT_ErrorResponse(VendorSpecificEvent):
    ERRORS = {
        0x01: 'The attribute handle given was not valid on this server.',
        0x02: 'The attribute cannot be read.',
        0x03: 'The attribute cannot be written.',
        0x04: 'The attribute PDU was invalid.',
        0x05: 'The attribute requires authentication before'
              'it can be read or written.',
        0x06: 'Attribute server does not support the request'
              'received from the client.',
        0x07: 'Offset specified was past the end of the attribute.',
        0x08: 'The attribute requires authorization before it can be'
              'read or written.',
        0x09: 'Too many prepare writes have been queued.',
        0x0A: 'No attribute found within the given attribute handle range.',
        0x0B: 'The attribute cannot be read or written using'
              'the Read Blob Request.',
        0x0C: 'The Encryption Key Size used for encrypting'
              'this link is insufficient.',
        0x0D: 'The attribute value length is invalid for the operation.',
        0x0E: 'The attribute request that was requested has encountered'
              'an error that was unlikely, and therefore could not be'
              'completed as requested.',
        0x0F: 'The attribute requires encryption before it can be'
              'read or written.',
        0x10: 'The attribute type is not a supported grouping attribute'
              'as defined by a higher layer specification.',
        0x11: 'Insufficient Resources to complete the request.',
        0x80: 'The attribute value is invalid for the operation.',
    }

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def pdu_length(self):
        OFFSET, SIZE_OCTETS = 8, 1
        pdu_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', pdu_length)[0]

    @property
    def requisition_opcode(self):
        OFFSET, SIZE_OCTETS = 9, 1
        requisition_opcode = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', requisition_opcode)[0]

    @property
    def handle(self):
        OFFSET, SIZE_OCTETS = 10, 2
        handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', handle)[0]

    @property
    def error_code(self):
        OFFSET, SIZE_OCTETS = 12, 1
        error_code = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', error_code)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'PDU Length: {} ({})',
            'Requition OpCode: {} ({})',
            'Handle: {} ({})',
            'Error Code: {} ({})']).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.pdu_length),
            int(self.pdu_length),
            hex(self.requisition_opcode),
            int(self.requisition_opcode),
            hex(self.handle),
            int(self.handle),
            hex(self.error_code),
            ATT_ErrorResponse.ERRORS[self.error_code])
