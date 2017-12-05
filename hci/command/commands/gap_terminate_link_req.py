from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class GAP_TerminateLinkReq(CommandPacket):
    class Reason(IntEnum):
        AUTHENTICATION_FAILURE = 0x05
        REMOTE_USER_TERMINATED_CONNECTION = 0x13
        REMOTE_DEVICE_TERMINATED_CONNECTION_LOW_RESOURCES = 0x14
        REMOTE_DEVICE_TERMINATED_CONNECTION_POWER_OFF = 0x15
        UNSUPPORTED_REMOTE_FEATURE = 0x1A
        PAIRING_WITH_UNIT_KEY_NOT_SUPPORTED = 0x29
        UNACCEPTABLE_CONNECTION_INTERVAL = 0x3B

    def __init__(self, conn_handle, reason):
        super().__init__(
            CommandPacket.OpCode.GAP_TERMINATE_LINK_REQUEST,
            GAP_TerminateLinkReq._params_to_binary(conn_handle, reason)
        )

    @staticmethod
    def _params_to_binary(conn_handle, reason):
        return pack('<HB', conn_handle, reason)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def reason(self):
        OFFSET, SIZE_OCTETS = 6, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Reason: {} ({})',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.reason),
            GAP_TerminateLinkReq.Reason(self.reason).name,
        )
