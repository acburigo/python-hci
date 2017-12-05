from struct import unpack_from

from .. import VendorSpecificEvent


class GAP_LinkTerminated(VendorSpecificEvent):
    REASON = {0x08: 'Supervisor Timeout',
              0x13: 'Peer Requested',
              0x16: 'Host Requested',
              0x22: 'Control Packet Timeout',
              0x28: 'Control Packet Instant Passed',
              0x3B: 'LSTO Violation',
              0x3D: 'MIC Failure'}

    @property
    def connection_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        connection_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_handle)[0]

    @property
    def reason(self):
        OFFSET, SIZE_OCTETS = 8, 1
        reason = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', reason)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Reason {} ({})']).format(
            hex(self.connection_handle),
            int(self.connection_handle),
            hex(self.reason),
            GAP_LinkTerminated.REASON[self.reason])
