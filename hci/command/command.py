from struct import pack
import binascii

from .opcode import OpCode


class CommandPacket:
    PACKET_TYPE = 0x01
    OFFSET_DATA_LENGTH = 0x03

    def __init__(self, opcode, parameters=b''):
        self.opcode = opcode
        self.parameter_total_length = len(parameters)
        self.parameters = parameters

    def _get_parameter(self, offset, size_octets):
        return self.parameters[offset: offset + size_octets]

    def to_binary(self):
        return pack('<BHB',
                    CommandPacket.PACKET_TYPE,
                    self.opcode,
                    self.parameter_total_length) + self.parameters

    def __str__(self):
        return '\n'.join([
            'Packet Type: {} ({})',
            'OpCode: {} ({})',
            'Data Length: {} ({})',
            'Parameters: {}',
        ]).format(
            hex(CommandPacket.PACKET_TYPE),
            int(CommandPacket.PACKET_TYPE),
            hex(self.opcode),
            OpCode(self.opcode).name,
            hex(self.parameter_total_length),
            int(self.parameter_total_length),
            binascii.hexlify(self.parameters).decode('utf-8'),
        )
