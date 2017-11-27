from struct import unpack_from

from .. import VendorSpecificEvent


class GAP_LinkParamUpdate(VendorSpecificEvent):
    @property
    def connection_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        connection_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_handle)[0]

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
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Connection Interval: {} ({})',
            'Connection Latency: {} ({})',
            'Connection Timeout: {} ({})']).format(
            hex(self.connection_handle),
            int(self.connection_handle),
            hex(self.connection_interval),
            int(self.connection_interval),
            hex(self.connection_latency),
            int(self.connection_latency),
            hex(self.connection_timeout),
            int(self.connection_timeout))
