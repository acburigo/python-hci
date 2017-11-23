from enum import IntEnum
from struct import unpack, pack
from binascii import hexlify

from ..command_packet import CommandPacket
from ..opcode import OpCode
from ..transforms import _hex_address_to_bytes


class GAP_DeviceInit(CommandPacket):
    class ProfileRole(IntEnum):
        GAP_PROFILE_BROADCASTER = 0x01
        GAP_PROFILE_OBSERVER = 0x02
        GAP_PROFILE_PERIPHERAL = 0x04
        GAP_PROFILE_CENTRAL = 0x08

    def __init__(self, profile_role, max_scan_responses, irk, csrk,
                 sign_counter):
        super().__init__(
            OpCode.GAP_DEVICE_INITIALIZATION,
            GAP_DeviceInit._params_to_binary(
                profile_role, max_scan_responses, irk, csrk, sign_counter)
        )

    @staticmethod
    def _params_to_binary(profile_role, max_scan_responses, irk, csrk,
                          sign_counter):
        return pack('<BB16B16BI',
                    profile_role,
                    max_scan_responses,
                    *tuple(_hex_address_to_bytes(irk)),
                    *tuple(_hex_address_to_bytes(csrk)),
                    sign_counter)

    @property
    def profile_role(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def max_scan_responses(self):
        OFFSET, SIZE_OCTETS = 5, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def irk(self):
        OFFSET, SIZE_OCTETS = 6, 16
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    @property
    def csrk(self):
        OFFSET, SIZE_OCTETS = 22, 16
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    @property
    def sign_counter(self):
        OFFSET, SIZE_OCTETS = 38, 4
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<I', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Profile Role: {} ({})',
            'Max. Scan Responses: {} ({})',
            'IRK: {}',
            'CSRK: {}',
            'Sign Counter: {} ({})',
        ]).format(
            hex(self.profile_role),
            GAP_DeviceInit.ProfileRole(self.profile_role).name,
            hex(self.max_scan_responses),
            int(self.max_scan_responses),
            hexlify(self.irk).decode('utf-8'),
            hexlify(self.csrk).decode('utf-8'),
            hex(self.sign_counter),
            int(self.sign_counter),
        )
