from ..command_packet import CommandPacket


class HCI_Reset(CommandPacket):
    def __init__(self):
        super().__init__(CommandPacket.OpCode.HCI_RESET)
