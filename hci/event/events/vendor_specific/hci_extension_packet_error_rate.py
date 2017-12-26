from struct import unpack_from


from .. import VendorSpecificEvent


class HCI_Extension_PacketErrorRate(VendorSpecificEvent):

    @property
    def cmd_opcode(self):
        OFFSET, SIZE_OCTETS = 6, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def per_cmd(self):
        OFFSET, SIZE_OCTETS = 8, 1
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', conn_handle)[0]

    @property
    def num_pkts(self):
        OFFSET, SIZE_OCTETS = 9, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def num_crc_err(self):
        OFFSET, SIZE_OCTETS = 11, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def num_events(self):
        OFFSET, SIZE_OCTETS = 13, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def num_misssed_events(self):
        OFFSET, SIZE_OCTETS = 15, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Command OPCode: {} ({})',
            'Packet Error Rate Command: {} ({})',
            'Number Of Packets: {} ({})',
            'Number Of CRC Error: {} ({})',
            'Number Of Events: {} ({})',
            'Number Of Missed Events: {} ({})']).format(
            hex(self.cmd_opcode),
            int(self.cmd_opcode),
            hex(self.per_cmd),
            int(self.per_cmd),
            hex(self.num_pkts),
            int(self.num_pkts),
            hex(self.num_crc_err),
            int(self.num_crc_err),
            hex(self.num_events),
            int(self.num_events),
            hex(self.num_misssed_events),
            int(self.num_misssed_events))
