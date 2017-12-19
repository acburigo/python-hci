from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class HCI_EXT_OnePktPerEvt(CommandPacket):
    class Control(IntEnum):
        HCI_EXT_DISABLE_ONE_PKT_PER_EVT = 0x00
        HCI_EXT_ENABLE_ONE_PKT_PER_EVT = 0x01

    def __init__(self, control):
        super().__init__(
            CommandPacket.OpCode.HCI_EXTENSION_ONE_PACKET_PER_EVENT,
            HCI_EXT_OnePktPerEvt._params_to_binary(control)
        )

    @staticmethod
    def _params_to_binary(control):
        return pack('<B', control)

    @property
    def control(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Control: {} ({})',
        ]).format(
            hex(self.control),
            HCI_EXT_OnePktPerEvt.Control(self.control).name,
        )
