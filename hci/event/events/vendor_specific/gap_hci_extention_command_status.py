from struct import unpack_from
from binascii import hexlify

from .. import VendorSpecificEvent
from hci.command.opcode import OpCode


class GAP_HCI_ExtentionCommandStatus(VendorSpecificEvent):
    @property
    def opcode(self):
        OFFSET, SIZE_OCTETS = 6, 2
        opcode = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', opcode)[0]

    @property
    def data_length(self):
        OFFSET, SIZE_OCTETS = 8, 1
        data_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data_length)[0]

    @property
    def param_value(self):
        OFFSET, SIZE_OCTETS = 9, self.data_length
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'OpCode: {} ({})',
            'Data Length: {} ({})',
            'Param: {}']).format(
            hex(self.opcode),
            OpCode(self.opcode).name,
            hex(self.data_length),
            int(self.data_length),
            hexlify(self.param_value).decode('utf-8'))
