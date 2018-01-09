from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class HCI_EXT_ResetSystem(CommandPacket):

    class Mode(IntEnum):
        HCI_EXT_RESET_SYSTEM_HARD = 0x00
        HCI_EXT_RESET_SYSTEM_SOFT = 0x01

    def __init__(self, mode):
        super().__init__(
            CommandPacket.OpCode.HCI_EXTENSION_RESET_SYSTEM,
            HCI_EXT_ResetSystem._params_to_binary(mode)
        )

    @staticmethod
    def _params_to_binary(mode):
        return pack('<B', mode)

    @property
    def mode(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Mode: {} ({})',
        ]).format(
            hex(self.mode),
            HCI_EXT_ResetSystem.Mode(self.mode).name,
        )
