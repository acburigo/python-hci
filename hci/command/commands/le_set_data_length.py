from struct import pack, unpack

from ..command_packet import CommandPacket


class LE_SetDataLength(CommandPacket):
    def __init__(self, conn_handle, tx_octets, tx_time):
        super().__init__(
            CommandPacket.OpCode.LE_SET_DATA_LENGTH,
            LE_SetDataLength._params_to_binary(conn_handle, tx_octets, tx_time)
        )

    @staticmethod
    def _params_to_binary(conn_handle, tx_octets, tx_time):
        return pack('<HHH', conn_handle, tx_octets, tx_time)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def tx_octets(self):
        OFFSET, SIZE_OCTETS = 6, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def tx_time(self):
        OFFSET, SIZE_OCTETS = 8, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Max. Transmit Payload: {} ({} bytes)',
            'Max. Transmit Time: {} ({} us)',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.tx_octets),
            int(self.tx_octets),
            hex(self.tx_time),
            int(self.tx_time),
        )
