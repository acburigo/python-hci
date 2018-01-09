from struct import unpack_from

from .. import HCI_CommandComplete


class HCI_ReadRssi(HCI_CommandComplete):
    @property
    def handle(self):
        OFFSET, SIZE_OCTETS = 7, 2
        handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', handle)[0]

    @property
    def rssi(self):
        OFFSET, SIZE_OCTETS = 9, 1
        rssi = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', rssi)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Handle: {} ({})',
            'RSSI: {} ({})']).format(
            hex(self.handle),
            int(self.handle),
            hex(self.rssi),
            int(self.rssi))
