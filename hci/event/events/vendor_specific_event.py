from struct import unpack_from
from hci.event import EventPacket
from .vendor_specific import VendorSpecificEvents


class VendorSpecificEvent(EventPacket):
    STATUS = {0x00: 'Success', 0x10: 'Failure'}

    @property
    def event(self):
        OFFSET, SIZE_OCTETS = 3, 2
        event = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', event)[0]

    @property
    def status(self):
        OFFSET, SIZE_OCTETS = 5, 1
        status = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', status)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Event: {} ({})',
            'Status: {} ({})']).format(
            hex(self.event), VendorSpecificEvents(self.event).name,
            hex(self.status), VendorSpecificEvent.STATUS[self.status])
