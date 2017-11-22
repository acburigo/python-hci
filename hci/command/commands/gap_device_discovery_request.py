from enum import IntEnum
from struct import pack, unpack

from ..command import CommandPacket
from ..opcode import OpCode


class GAP_DeviceDiscoveryRequest(CommandPacket):
    class Mode(IntEnum):
        NON_DISCOVERABLE_SCAN = 0
        GENERAL_MODE_SCAN = 1
        LIMITED_MODE_SCAN = 2
        SCAN_FOR_ALL_DEVICES = 3

    class ActiveScan(IntEnum):
        OFF = 0
        ON = 1

    class WhiteList(IntEnum):
        DO_NOT_USE = 0
        USE = 1

    def __init__(self, mode, active_scan, white_list):
        super().__init__(
            OpCode.GAP_DEVICE_DISCOVERY_REQUEST,
            GAP_DeviceDiscoveryRequest._params_to_binary(mode, active_scan,
                                                         white_list)
        )

    @staticmethod
    def _params_to_binary(mode, active_scan, white_list):
        return pack('<BBB', mode, active_scan, white_list)

    @property
    def mode(self):
        OFFSET, SIZE_OCTETS = 0, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def active_scan(self):
        OFFSET, SIZE_OCTETS = 1, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def white_list(self):
        OFFSET, SIZE_OCTETS = 2, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Mode: {} ({})',
            'Active Scan: {} ({})',
            'White List: {} ({})',
        ]).format(
            hex(self.mode),
            GAP_DeviceDiscoveryRequest.Mode(self.mode).name,
            hex(self.active_scan),
            GAP_DeviceDiscoveryRequest.ActiveScan(self.active_scan).name,
            hex(self.white_list),
            GAP_DeviceDiscoveryRequest.WhiteList(self.white_list).name,
        )
