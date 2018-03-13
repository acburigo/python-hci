from struct import pack, unpack

from ..command_packet import CommandPacket


class GATT_DiscAllCharDescs(CommandPacket):
    def __init__(self, conn_handle, start_handle, end_handle):
        super().__init__(
            CommandPacket.OpCode.GATT_DISC_ALL_CHAR_DESCS,
            GATT_DiscAllCharDescs._params_to_binary(
                conn_handle, start_handle, end_handle)
        )

    @staticmethod
    def _params_to_binary(conn_handle, start_handle, end_handle):
        return pack('<HHH', conn_handle, start_handle, end_handle)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def start_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def end_handle(self):
        OFFSET, SIZE_OCTETS = 8, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Start Handle: {} ({})',
            'End Handle: {} ({})',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.start_handle),
            int(self.start_handle),
            hex(self.end_handle),
            int(self.end_handle),
        )
