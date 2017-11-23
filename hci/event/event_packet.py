from struct import unpack_from

from hci import HciPacket
from hci.event.event_codes import EventCodes


class EventPacket(HciPacket):
    OFFSET_DATA_LENGTH = 2

    @property
    def event_code(self):
        OFFSET, SIZE_OCTETS = 1, 1
        event_code = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', event_code)[0]

    @property
    def data_length(self):
        OFFSET, SIZE_OCTETS = 2, 1
        data_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data_length)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Event Code: {} ({})',
            'Data Length: {} ({})',
        ]).format(
            hex(self.event_code),
            EventCodes(self.event_code).name,
            hex(self.data_length),
            int(self.data_length),
        )
