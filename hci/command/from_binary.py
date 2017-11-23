from struct import unpack_from
from .command_packet import CommandPacket
from .commands import *
from .opcode import OpCode


_opcode_to_class = {
    OpCode.GAP_DEVICE_DISCOVERY_REQUEST: GAP_DeviceDiscoveryRequest,
    OpCode.GAP_DEVICE_INITIALIZATION: GAP_DeviceInit,
    OpCode.GAP_ESTABLISH_LINK_REQUEST: GAP_EstablishLinkReq,
    OpCode.GAP_GET_PARAMETER: GAP_GetParam,
    OpCode.GATT_WRITE: GATT_WriteCharValue,
    OpCode.HCI_RESET: HCI_Reset,
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
