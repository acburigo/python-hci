from struct import unpack_from
from .command import CommandPacket
from .commands import *
from .opcode import OpCode


_opcode_to_class = {
    OpCode.HCI_RESET: HCI_Reset,
    OpCode.GAP_DEVICE_INITIALIZATION: GAP_DeviceInit,
}


def from_binary(buf):
    opcode, parameter_total_length = unpack_from('<HB', buf, offset=1)

    pkt = CommandPacket(
        opcode=opcode,
        parameters=buf[4:]
    )

    try:
        pkt.__class__ = _opcode_to_class[pkt.opcode]
    except KeyError:
        pass

    return pkt
