from enum import IntEnum
from struct import unpack_from

from .. import VendorSpecificEvent
from hci.transforms import _bytes_to_hex_string


class GAP_LinkEstablished(VendorSpecificEvent):
    class GAP_Profiles(IntEnum):
        GAP_PROFILE_BROADCASTER = 0x01
        GAP_PROFILE_OBSERVER = 0x02
        GAP_PROFILE_PERIPHERAL = 0x04
        GAP_PROFILE_CENTRAL = 0x08

    @property
    def device_address_type(self):
        OFFSET, SIZE_OCTETS = 6, 1
        device_address_type = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', device_address_type)[0]

    @property
    def device_address(self):
        OFFSET, SIZE_OCTETS = 7, 6
        device_address = self._get_data(OFFSET, SIZE_OCTETS)[::-1]
        return device_address

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 13, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def connection_role(self):
        OFFSET, SIZE_OCTETS = 15, 1
        connection_role = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', connection_role)[0]

    @property
    def connection_interval(self):
        OFFSET, SIZE_OCTETS = 16, 2
        connection_interval = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_interval)[0]

    @property
    def connection_latency(self):
        OFFSET, SIZE_OCTETS = 18, 2
        connection_latency = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_latency)[0]

    @property
    def connection_timeout(self):
        OFFSET, SIZE_OCTETS = 20, 2
        connection_timeout = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', connection_timeout)[0]

    @property
    def clock_accuracy(self):
        OFFSET, SIZE_OCTETS = 22, 1
        clock_accuracy = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', clock_accuracy)[0]

    def __str__(self):
        CONN_INTERVAL_SCALE_CONST_MS = 1.25
        CONN_TIMEOUT_SCALE_CONST_MS = 10
        return super().__str__() + '\n' + '\n'.join([
            'Device Address Type: {} ({})',
            'Device Address: {}',
            'Connection Handle: {} ({})',
            'Connection Role: {} ({})',
            'Connection Interval: {} ({} ms)',
            'Connection Latency: {} ({} connection events)',
            'Connection Timeout: {} ({} ms)',
            'Clock Accuracy: {} ({})']).format(
            hex(self.device_address_type),
            GAP_LinkEstablished.AdressType(self.device_address_type).name,
            _bytes_to_hex_string(self.device_address),
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.connection_role),
            GAP_LinkEstablished.GAP_Profiles(self.connection_role).name,
            hex(self.connection_interval),
            int(self.connection_interval) * CONN_INTERVAL_SCALE_CONST_MS,
            hex(self.connection_latency),
            int(self.connection_latency),
            hex(self.connection_timeout),
            int(self.connection_timeout) * CONN_TIMEOUT_SCALE_CONST_MS,
            hex(self.clock_accuracy),
            int(self.clock_accuracy))
