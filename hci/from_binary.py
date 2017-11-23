from .hci_packet import HciPacket
from .command import *
from .event import *


def _parse_pkt_length(buffer, pkt_type, pkt_offset):
    if (pkt_type == HciPacket.PacketType.COMMAND):
        offset = pkt_offset + CommandPacket.OFFSET_DATA_LENGTH
        data_length = unpack_from('<B', buffer, offset=offset)[0]
        pkt_length = 1 + CommandPacket.OFFSET_DATA_LENGTH + data_length

    elif (pkt_type == HciPacket.PacketType.EVENT):
        offset = pkt_offset + EventPacket.OFFSET_DATA_LENGTH
        data_length = unpack_from('<B', buffer, offset=offset)[0]
        pkt_length = 1 + EventPacket.OFFSET_DATA_LENGTH + data_length

    else:
        raise NotImplementedError()
    return pkt_length


def _parse_pkt_type(buffer, pkt_offset):
    return unpack_from('<B', buffer, offset=pkt_offset)[0]


def from_binary(buffer):
    pkts = []
    pkt_offset = 0

    while (pkt_offset < len(buffer)):
        pkt_type = _parse_pkt_type(buffer, pkt_offset)
        pkt_length = _parse_pkt_length(buffer, pkt_type, pkt_offset)
        pkt_buffer = buffer[pkt_offset:pkt_offset + pkt_length]

        if (pkt_type == HciPacket.PacketType.COMMAND):
            pkts.append(CommandPacket.from_binary(pkt_buffer))
        elif (pkt_type == HciPacket.PacketType.EVENT):
            pkts.append(EventPacket.from_binary(pkt_buffer))
        else:
            raise NotImplementedError()

        pkt_offset += pkt_length
    return pkts
