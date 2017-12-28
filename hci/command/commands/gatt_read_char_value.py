from struct import pack, unpack

from ..command_packet import CommandPacket


class GATT_ReadCharValue(CommandPacket):
    def __init__(self, conn_handle, handle):
        super().__init__(
            CommandPacket.OpCode.GATT_READ,
            GATT_ReadCharValue._params_to_binary(conn_handle, handle)
        )

    @staticmethod
    def _params_to_binary(conn_handle, handle):
        return pack('<HH', conn_handle, handle)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Handle: {} ({})',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.handle),
            int(self.handle),
        )
