from struct import unpack_from

from .hci_packet import HciPacket
from .command import CommandPacket
from .event import EventPacket
from .autocast import _autocast


def _parse_pkt_length(buf, pkt_type, pkt_offset):
    if (pkt_type == HciPacket.PacketType.COMMAND):
        offset = pkt_offset + CommandPacket.OFFSET_DATA_LENGTH
        data_length = unpack_from('<B', buf, offset=offset)[0]
        pkt_length = 1 + CommandPacket.OFFSET_DATA_LENGTH + data_length

    elif (pkt_type == HciPacket.PacketType.EVENT):
        offset = pkt_offset + EventPacket.OFFSET_DATA_LENGTH
        data_length = unpack_from('<B', buf, offset=offset)[0]
        pkt_length = 1 + EventPacket.OFFSET_DATA_LENGTH + data_length

    else:
        raise NotImplementedError()
    return pkt_length


def _parse_pkt_type(buf, pkt_offset):
    return unpack_from('<B', buf, offset=pkt_offset)[0]


def from_binary(buf):
    pkts = []
    pkt_offset = 0

    while (pkt_offset < len(buf)):
        pkt_type = _parse_pkt_type(buf, pkt_offset)
        pkt_length = _parse_pkt_length(buf, pkt_type, pkt_offset)
        payload = buf[pkt_offset + 1:pkt_offset + pkt_length]

        pkt = HciPacket(pkt_type, payload)
        pkt = _autocast(pkt)
        pkts.append(pkt)

        pkt_offset += pkt_length
    return pkts
