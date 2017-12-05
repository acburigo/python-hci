from struct import unpack_from

from .. import VendorSpecificEvent
from hci.transforms import _bytes_to_hex_string


class GAP_DeviceDiscoveryDone(VendorSpecificEvent):
    class DeviceInfo:
        def __init__(self, data):
            self._data = data

        @property
        def event_type(self):
            OFFSET, SIZE_OCTETS = 0, 1
            event_type = self._data[OFFSET:OFFSET + SIZE_OCTETS]
            return unpack_from('<B', event_type)[0]

        @property
        def address_type(self):
            OFFSET, SIZE_OCTETS = 1, 1
            address_type = self._data[OFFSET:OFFSET + SIZE_OCTETS]
            return unpack_from('<B', address_type)[0]

        @property
        def address(self):
            OFFSET, SIZE_OCTETS = 2, 6
            address = self._data[OFFSET:OFFSET + SIZE_OCTETS][::-1]
            return address

        def __str__(self):
            return '\n'.join([
                'Event Type: {} ({})',
                'Address Type: {} ({})',
                'Address: {}']).format(
                hex(self.event_type),
                GAP_DeviceDiscoveryDone.EventType(self.event_type).name,
                hex(self.address_type),
                GAP_DeviceDiscoveryDone.AdressType(self.address_type).name,
                _bytes_to_hex_string(self.address))

    @property
    def num_devices(self):
        OFFSET, SIZE_OCTETS = 6, 1
        num_devices = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', num_devices)[0]

    @property
    def devices(self):
        OFFSET, DEVICE_INFO_SIZE_OCTETS = 7, 8
        data = self._get_data(OFFSET)
        devices = []
        for i in range(0, len(data), DEVICE_INFO_SIZE_OCTETS):
            device_data = data[i:i + DEVICE_INFO_SIZE_OCTETS]
            devices.append(GAP_DeviceDiscoveryDone.DeviceInfo(device_data))
        return devices

    def __str__(self):
        event_string = ['Number of Devices: {} ({})'.format(
            hex(self.num_devices),
            int(self.num_devices))]
        for i, device in enumerate(self.devices):
            event_string.append('Device {}\n{}'.format(i, str(device)))
        return super().__str__() + '\n' + '\n'.join(event_string)
