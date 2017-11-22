from enum import IntEnum
from struct import pack, unpack
from binascii import hexlify

from ..command import CommandPacket
from ..opcode import OpCode
from ..transforms import _hex_address_to_bytes


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
            OpCode.GAP_ESTABLISH_LINK_REQUEST,
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
                    _hex_address_to_bytes(peer_addr))

    @property
    def high_duty_cycle(self):
        OFFSET, SIZE_OCTETS = 0, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def white_list(self):
        OFFSET, SIZE_OCTETS = 1, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def addr_type_peer(self):
        OFFSET, SIZE_OCTETS = 2, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def peer_addr(self):
        OFFSET, SIZE_OCTETS = 3, 6
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
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
            hexlify(self.peer_addr).decode('utf-8'),
        )
