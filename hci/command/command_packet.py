from struct import pack, unpack

from ..hci_packet import HciPacket
from .opcode import OpCode


class CommandPacket(HciPacket):
    OFFSET_DATA_LENGTH = 0x03

    def __init__(self, opcode, parameters=b''):
        super().__init__(
            HciPacket.PacketType.COMMAND,
            CommandPacket._params_to_binary(opcode, parameters)
        )

    @staticmethod
    def _params_to_binary(opcode, parameters):
        fmt = '<HB%ds' % len(parameters)
        return pack(fmt, opcode, len(parameters), parameters)

    @property
    def opcode(self):
        OFFSET, SIZE_OCTETS = 1, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def parameter_total_length(self):
        OFFSET, SIZE_OCTETS = 3, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'OpCode: {} ({})',
            'Data Length: {} ({})',
        ]).format(
            hex(self.opcode),
            OpCode(self.opcode).name,
            hex(self.parameter_total_length),
            int(self.parameter_total_length),
        )
