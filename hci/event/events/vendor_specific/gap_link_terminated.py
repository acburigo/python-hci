from enum import IntEnum
from struct import unpack_from

from .. import VendorSpecificEvent


class GAP_LinkTerminated(VendorSpecificEvent):
    class Reason(IntEnum):
        SUPERVISOR_TIMEOUT = 0X08
        PEER_REQUESTED = 0X13
        HOST_REQUESTED = 0X16
        CONTROL_PACKET_TIMEOUT = 0X22
        CONTROL_PACKET_INSTANT_PASSED = 0X28
        LSTO_VIOLATION = 0X3B
        MIC_FAILURE = 0X3D

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
            GAP_LinkTerminated.Reason(self.reason).name)
