from struct import unpack_from

from .. import VendorSpecificEvent
from hci.transforms import _bytes_to_hex_string


class ATT_ReadResponse(VendorSpecificEvent):
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
    def value(self):
        OFFSET = 9
        value = self._get_data(OFFSET)
        return value

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'PDU Length: {} ({})',
            'Value: {}']).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.pdu_length),
            int(self.pdu_length),
            _bytes_to_hex_string(self.value))
