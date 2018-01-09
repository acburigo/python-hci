from struct import unpack_from

from .. import VendorSpecificEvent


class ATT_ExchangeMtuResponse(VendorSpecificEvent):
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
    def server_rx_mtu(self):
        OFFSET, SIZE_OCTETS = 9, 2
        server_rx_mtu = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', server_rx_mtu)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'PDU Length: {} ({})',
            'Server Rx MTU: {} ({})']).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.pdu_length),
            int(self.pdu_length),
            hex(self.server_rx_mtu),
            int(self.server_rx_mtu))
