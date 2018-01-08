from struct import unpack_from

from hci.command.opcode import OpCode
from .. import VendorSpecificEvent


class HCI_EXT_SetTxPowerDone(VendorSpecificEvent):
    @property
    def cmd_opcode(self):
        OFFSET, SIZE_OCTETS = 6, 2
        cmd_opcode = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', cmd_opcode)[0]

    def __str__(self):
        return super().__str__() + '\n' + 'Command Opcode: {} ({})'.format(
            hex(self.cmd_opcode),
            OpCode(self.cmd_opcode).name)
