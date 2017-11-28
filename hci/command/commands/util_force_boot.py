from ..command_packet import CommandPacket


class UTIL_ForceBoot(CommandPacket):
    def __init__(self):
        super().__init__(CommandPacket.OpCode.UTIL_FORCE_BOOT)
