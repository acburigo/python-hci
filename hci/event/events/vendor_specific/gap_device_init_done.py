from binascii import hexlify
from struct import unpack_from

from .. import VendorSpecificEvent


class GAP_DeviceInitDone(VendorSpecificEvent):
    @property
    def dev_addrs(self):
        OFFSET, SIZE_OCTETS = 6, 6
        dev_addrs = self._get_data(OFFSET, SIZE_OCTETS)
        return dev_addrs

    @property
    def data_pkt_len(self):
        OFFSET, SIZE_OCTETS = 12, 2
        data_pkt_len = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', data_pkt_len)[0]

    @property
    def num_data_pkts(self):
        OFFSET, SIZE_OCTETS = 14, 1
        num_data_pkts = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', num_data_pkts)[0]

    @property
    def irk(self):
        OFFSET, SIZE_OCTETS = 15, 16
        irk = self._get_data(OFFSET, SIZE_OCTETS)
        return irk

    @property
    def csrk(self):
        OFFSET, SIZE_OCTETS = 31, 16
        csrk = self._get_data(OFFSET, SIZE_OCTETS)
        return csrk

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Device Address: {}',
            'Data Packet Length: {} ({})',
            'Num Data Packets: {} ({})',
            'IRK: {}',
            'CSRK: {}']).format(
            hexlify(self.dev_addrs).decode('utf-8'),
            hex(self.data_pkt_len),
            int(self.data_pkt_len),
            hex(self.num_data_pkts),
            int(self.num_data_pkts),
            hexlify(self.irk).decode('utf-8'),
            hexlify(self.csrk).decode('utf-8'))
