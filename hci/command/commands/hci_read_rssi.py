from struct import pack, unpack

from ..command_packet import CommandPacket


class HCI_ReadRSSI(CommandPacket):
    def __init__(self, conn_handle):
        super().__init__(
            CommandPacket.OpCode.READ_RSSI,
            HCI_ReadRSSI._params_to_binary(conn_handle)
        )

    @staticmethod
    def _params_to_binary(conn_handle):
        return pack('<H', conn_handle)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
        )
