from struct import unpack_from

from .. import VendorSpecificEvent
from hci.transforms import _bytes_to_hex_string


class ATTHandleValueNotification(VendorSpecificEvent):
    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def pdu_len(self):
        OFFSET, SIZE_OCTETS = 8, 1
        pdu_len = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', pdu_len)[0]

    @property
    def handle(self):
        OFFSET, SIZE_OCTETS = 9, 2
        handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', handle)[0]

    @property
    def value(self):
        OFFSET = 11
        value = self._get_data(OFFSET)
        return value

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {}, ({})',
            'PDU Length: {} ({})',
            'Handle: {} ({})',
            'Value: {}']).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.pdu_len),
            int(self.pdu_len),
            hex(self.handle),
            int(self.handle),
            _bytes_to_hex_string(self.value)
        )
