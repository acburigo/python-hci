from struct import pack, unpack
from enum import IntEnum


class HciPacket:
    class PacketType(IntEnum):
        COMMAND = 0x01
        ASYNCHRONOUS_DATA = 0x02
        SYNCHRONOUS_DATA = 0x03
        EVENT = 0x04

    def __init__(self, packet_type, payload):
        self._data = HciPacket._params_to_binary(packet_type, payload)

    @staticmethod
    def _params_to_binary(packet_type, payload):
        fmt = '<B%ds' % len(payload)
        return pack(fmt, packet_type, payload)

    def _get_data(self, offset, size_octets=None):
        if (size_octets is not None):
            return self._data[offset: offset + size_octets]
        else:
            return self._data[offset:]

    @property
    def binary(self):
        return self._data

    @property
    def packet_type(self):
        OFFSET, SIZE_OCTETS = 0, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return '\n'.join([
            'Packet Type: {} ({})',
        ]).format(
            hex(self.packet_type),
            HciPacket.PacketType(self.packet_type).name,
        )
