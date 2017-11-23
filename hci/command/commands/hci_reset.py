from ..command_packet import CommandPacket
from ..opcode import OpCode


class HCI_Reset(CommandPacket):
    def __init__(self):
        super().__init__(OpCode.HCI_RESET)
