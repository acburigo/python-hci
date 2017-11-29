from struct import unpack_from

from .hci_packet import HciPacket
from .asynchronous import AsynchronousDataPacket
from .command import CommandPacket
from .event import EventPacket
from .autocast import _autocast


def _parse_pkt_length(buf, pkt_type, pkt_offset):
    if (pkt_type == HciPacket.PacketType.COMMAND):
        offset_data_length = CommandPacket.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<B', buf, offset=offset)[0]

    elif (pkt_type == HciPacket.PacketType.EVENT):
        offset_data_length = EventPacket.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<B', buf, offset=offset)[0]

    elif (pkt_type == HciPacket.PacketType.ASYNCHRONOUS_DATA):
        offset_data_length = AsynchronousDataPacket.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<H', buf, offset=offset)[0]

    else:
        raise NotImplementedError(pkt_type)

    pkt_length = 1 + offset_data_length + data_length
    return pkt_length


def _parse_pkt_type(buf, pkt_offset):
    return unpack_from('<B', buf, offset=pkt_offset)[0]


def from_binary(buf):
    PACKET_TYPE_SIZE_OCTETS = 1
    pkts = []
    pkt_offset = 0
    incomplete_pkt_data = b''

    while (pkt_offset < len(buf)):
        pkt_type = _parse_pkt_type(buf, pkt_offset)
        pkt_length = _parse_pkt_length(buf, pkt_type, pkt_offset)
        pkt_data = buf[pkt_offset:pkt_offset + pkt_length]

        if (len(pkt_data) < pkt_length):
            incomplete_pkt_data = pkt_data
            break

        pkt = HciPacket(pkt_type, pkt_data[PACKET_TYPE_SIZE_OCTETS:])
        pkt = _autocast(pkt)
        pkts.append(pkt)

        pkt_offset += pkt_length
    return pkts, incomplete_pkt_data
