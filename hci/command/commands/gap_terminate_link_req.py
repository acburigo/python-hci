from struct import pack, unpack

from ..command_packet import CommandPacket


class GAP_TerminateLinkReq(CommandPacket):
    Reason = {
        0x05: 'Authentication Failure',
        0x13: 'Remote User Terminated Connection',
        0x14: 'Remote Device Terminated Connection Due To Low Resources',
        0x15: 'Remote Device Terminated Connection due to Power Off',
        0x1A: 'Unsupported Remote Feature',
        0x29: 'Pairing With Unit Key Not Supported',
        0x3B: 'Unacceptable Connection Interval',
    }

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
            GAP_TerminateLinkReq.Reason[self.reason],
        )
