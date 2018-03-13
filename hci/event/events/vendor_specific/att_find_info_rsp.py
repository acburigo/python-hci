from enum import IntEnum
from struct import unpack_from

from .. import VendorSpecificEvent
from hci.transforms import _bytes_to_hex_string


class ATT_FindInfoRsp(VendorSpecificEvent):
    class Info:
        def __init__(self, data):
            self._data = data

        @property
        def handle(self):
            SIZE_OCTETS = 2
            handle = self._data[:SIZE_OCTETS]
            return unpack_from('<H', handle)[0]

        @property
        def uuid(self):
            OFFSET = 2
            uuid = self._data[OFFSET:]
            return _bytes_to_hex_string(uuid)

        def __str__(self):
            return '\n'.join([
                'Handle: {} ({})',
                'uuid: {}']).format(
                    hex(self.handle),
                    int(self.handle),
                    self.uuid)

    class ReturnFormatKeys(IntEnum):
        UUID16BITS = 0x01
        UUID128BITS = 0x02

    RETURN_FORMAT = {
        ReturnFormatKeys.UUID16BITS: 'A list of 1 or more handles with'
                                     ' their 16-bit Bluetooth UUIDs',
        ReturnFormatKeys.UUID128BITS: 'A list of 1 or more handles with'
                                      ' their 128-bit UUIDs'}

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def pdu_length(self):
        OFFSET, SIZE_OCTETS = 8, 1
        pdu_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', pdu_length)[0]

    @property
    def format(self):
        OFFSET, SIZE_OCTETS = 9, 1
        frmt = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', frmt)[0]

    def _infer_info_size_octets(self):
        if self.format == self.ReturnFormatKeys.UUID16BITS:
            return 4
        elif self.format == self.ReturnFormatKeys.UUID128BITS:
            return 18

    @property
    def infos(self):
        OFFSET = 10
        data = self._get_data(OFFSET)
        infos = []
        size = self._infer_info_size_octets()
        for i in range(0, len(data), size):
            info_data = data[i: i + size]
            infos.append(self.Info(info_data))
        return infos

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'PDU Length: {} ({})',
            'Format: {} ({})',
            '{}']).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.pdu_length),
            int(self.pdu_length),
            hex(self.format),
            self.RETURN_FORMAT[self.format],
            '\n'.join([str(info) for info in self.infos]))
