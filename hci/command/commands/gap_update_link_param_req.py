from struct import unpack, pack

from ..command_packet import CommandPacket


class GAP_UpdateLinkParamReq(CommandPacket):
    def __init__(self, conn_handle, interval_min, interval_max, conn_latency,
                 conn_timeout):
        super().__init__(
            CommandPacket.OpCode.GAP_UPDATE_LINK_PARAMETER_REQUEST,
            GAP_UpdateLinkParamReq._params_to_binary(
                conn_handle, interval_min, interval_max, conn_latency,
                conn_timeout)
        )

    @staticmethod
    def _params_to_binary(conn_handle, interval_min, interval_max,
                          conn_latency, conn_timeout):
        return pack('<HHHHH',
                    conn_handle,
                    interval_min,
                    interval_max,
                    conn_latency,
                    conn_timeout)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def interval_min(self):
        OFFSET, SIZE_OCTETS = 6, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def interval_max(self):
        OFFSET, SIZE_OCTETS = 8, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def conn_latency(self):
        OFFSET, SIZE_OCTETS = 10, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def conn_timeout(self):
        OFFSET, SIZE_OCTETS = 12, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        CONN_INTERVAL_SCALE_CONST_MS = 1.25
        CONN_TIMEOUT_SCALE_CONST_MS = 10
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Minimum Connection Interval: {} ({} ms)',
            'Maximum Connection Interval: {} ({} ms)',
            'Connection Latency: {} ({} connection events)',
            'Connection Timeout: {} ({} ms)',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.interval_min),
            int(self.interval_min) * CONN_INTERVAL_SCALE_CONST_MS,
            hex(self.interval_max),
            int(self.interval_max) * CONN_INTERVAL_SCALE_CONST_MS,
            hex(self.conn_latency),
            int(self.conn_latency),
            hex(self.conn_timeout),
            int(self.conn_timeout) * CONN_TIMEOUT_SCALE_CONST_MS,
        )
