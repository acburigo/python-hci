from ..command_packet import CommandPacket


class UTIL_BuildRevision(CommandPacket):
    def __init__(self):
        super().__init__(CommandPacket.OpCode.UTIL_BUILD_REVISION)
