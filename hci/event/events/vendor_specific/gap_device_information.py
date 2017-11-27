from struct import unpack_from

from .. import VendorSpecificEvent
from hci.transforms import _bytes_to_hex_string


class GAP_DeviceInformation(VendorSpecificEvent):
    @property
    def event_type(self):
        OFFSET, SIZE_OCTETS = 6, 1
        event_type = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', event_type)[0]

    @property
    def address_type(self):
        OFFSET, SIZE_OCTETS = 7, 1
        address_type = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', address_type)[0]

    @property
    def address(self):
        OFFSET, SIZE_OCTETS = 8, 6
        address = self._get_data(OFFSET, SIZE_OCTETS)
        return address

    @property
    def rssi(self):
        OFFSET, SIZE_OCTETS = 14, 1
        rssi = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', rssi)[0]

    @property
    def data_length(self):
        OFFSET, SIZE_OCTETS = 15, 1
        data_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data_length)[0]

    @property
    def data(self):
        OFFSET = 16
        data = self._get_data(OFFSET)
        return data

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Event Type: {} ({})',
            'Address Type: {} ({})',
            'Address: {}',
            'RSSI: {} ({})',
            'Data Length: {}',
            'Data: {}']).format(
            hex(self.event_type),
            GAP_DeviceInformation.EventType(self.event_type).name,
            hex(self.address_type),
            GAP_DeviceInformation.AdressType(self.address_type).name,
            _bytes_to_hex_string(self.address),
            hex(self.rssi),
            int(self.rssi),
            hex(self.data_length),
            int(self.data_length),
            _bytes_to_hex_string(self.data))
