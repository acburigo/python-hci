from struct import pack, unpack
from binascii import hexlify

from ..command import CommandPacket
from ..opcode import OpCode


class GATT_WriteCharValue(CommandPacket):
    def __init__(self, conn_handle, handle, value):
        super().__init__(
            OpCode.GATT_WRITE,
            GATT_WriteCharValue._params_to_binary(conn_handle, handle, value)
        )

    @staticmethod
    def _params_to_binary(conn_handle, handle, value):
        assert type(value) is list
        return pack('<HH%dB' % len(value), conn_handle, handle, *tuple(value))

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 0, 2
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def handle(self):
        OFFSET, SIZE_OCTETS = 2, 2
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def value(self):
        OFFSET = 4
        SIZE_OCTETS = self.parameter_total_length - OFFSET
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<%ds' % SIZE_OCTETS, data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Handle: {} ({})',
            'Value: {}',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.handle),
            int(self.handle),
            hexlify(self.value).decode('utf-8'),
        )
