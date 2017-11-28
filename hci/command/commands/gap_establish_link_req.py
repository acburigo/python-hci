from enum import IntEnum
from struct import pack, unpack

from ..command_packet import CommandPacket
from hci.transforms import _hex_string_to_bytes
from hci.transforms import _bytes_to_hex_string


class GAP_EstablishLinkReq(CommandPacket):
    class HighDutyCycle(IntEnum):
        DISABLED = 0
        ENABLED = 1

    class WhiteList(IntEnum):
        DO_NOT_USE = 0
        USE = 1

    class AddrTypePeer(IntEnum):
        ADDRTYPE_PUBLIC = 0
        ADDRTYPE_STATIC = 1
        ADDRTYPE_PRIVATE_NONRESOLVE = 2
        ADDRTYPE_PRIVATE_RESOLVE = 3

    def __init__(self, high_duty_cycle, white_list, addr_type_peer, peer_addr):
        super().__init__(
            CommandPacket.OpCode.GAP_ESTABLISH_LINK_REQUEST,
            GAP_EstablishLinkReq._params_to_binary(high_duty_cycle,
                                                   white_list,
                                                   addr_type_peer,
                                                   peer_addr)
        )

    @staticmethod
    def _params_to_binary(high_duty_cycle, white_list, addr_type_peer,
                          peer_addr):
        return pack('<BBB6s',
                    high_duty_cycle,
                    white_list,
                    addr_type_peer,
                    _hex_string_to_bytes(peer_addr))

    @property
    def high_duty_cycle(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def white_list(self):
        OFFSET, SIZE_OCTETS = 5, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def addr_type_peer(self):
        OFFSET, SIZE_OCTETS = 6, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def peer_addr(self):
        OFFSET, SIZE_OCTETS = 7, 6
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'High Duty Cycle: {} ({})',
            'White List: {} ({})',
            'Address Type Peer: {} ({})',
            'Peer Address: {}',
        ]).format(
            hex(self.high_duty_cycle),
            GAP_EstablishLinkReq.HighDutyCycle(self.high_duty_cycle).name,
            hex(self.white_list),
            GAP_EstablishLinkReq.WhiteList(self.white_list).name,
            hex(self.addr_type_peer),
            GAP_EstablishLinkReq.AddrTypePeer(self.addr_type_peer).name,
            _bytes_to_hex_string(self.peer_addr),
        )
