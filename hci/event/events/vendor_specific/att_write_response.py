from struct import unpack_from

from .. import VendorSpecificEvent


class ATT_WriteResponse(VendorSpecificEvent):
    @property
    def connection_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        connection_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_handle)[0]

    @property
    def pdu_length(self):
        OFFSET, SIZE_OCTETS = 8, 1
        pdu_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', pdu_length)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'PDU Legth: {} ({})']).format(
            hex(self.connection_handle),
            int(self.connection_handle),
            hex(self.pdu_length),
            int(self.pdu_length))
