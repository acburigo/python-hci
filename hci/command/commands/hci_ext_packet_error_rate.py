from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class HCI_EXT_PacketErrorRate(CommandPacket):

    class Command(IntEnum):
        HCI_EXT_PER_RESET = 0x00
        HCI_EXT_PER_READ = 0x01

    def __init__(self, conn_handle, command):
        super().__init__(
            CommandPacket.OpCode.HCI_EXTENSION_PACKET_ERROR_RATE,
            HCI_EXT_PacketErrorRate._params_to_binary(conn_handle, command)
        )

    @staticmethod
    def _params_to_binary(conn_handle, client_rx_mtu):
        return pack('<HB', conn_handle, client_rx_mtu)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def command(self):
        OFFSET, SIZE_OCTETS = 6, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Command: {} ({})',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.command),
            HCI_EXT_PacketErrorRate.Command(self.command).name,
        )
