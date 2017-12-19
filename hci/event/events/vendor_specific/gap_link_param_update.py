from struct import unpack_from

from .. import VendorSpecificEvent


class GAP_LinkParamUpdate(VendorSpecificEvent):
    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def connection_interval(self):
        OFFSET, SIZE_OCTETS = 8, 2
        connection_interval = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_interval)[0]

    @property
    def connection_latency(self):
        OFFSET, SIZE_OCTETS = 10, 2
        connection_latency = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_latency)[0]

    @property
    def connection_timeout(self):
        OFFSET, SIZE_OCTETS = 12, 2
        connection_timeout = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_timeout)[0]

    def __str__(self):
        CONN_INTERVAL_SCALE_CONST_MS = 1.25
        CONN_TIMEOUT_SCALE_CONST_MS = 10
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Connection Interval: {} ({} ms)',
            'Connection Latency: {} ({} connection events)',
            'Connection Timeout: {} ({} ms)']).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.connection_interval),
            int(self.connection_interval) * CONN_INTERVAL_SCALE_CONST_MS,
            hex(self.connection_latency),
            int(self.connection_latency),
            hex(self.connection_timeout),
            int(self.connection_timeout) * CONN_TIMEOUT_SCALE_CONST_MS)
