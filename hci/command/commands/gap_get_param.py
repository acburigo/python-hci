from struct import pack, unpack

from ..command import CommandPacket
from ..opcode import OpCode


class GAP_GetParam(CommandPacket):
    def __init__(self, param_id):
        super().__init__(
            OpCode.GAP_GET_PARAMETER,
            GAP_GetParam._params_to_binary(param_id)
        )

    @staticmethod
    def _params_to_binary(param_id):
        return pack('<B', param_id)

    @property
    def param_id(self):
        OFFSET, SIZE_OCTETS = 0, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Parameter ID: {} ({})',
        ]).format(
            hex(self.param_id),
            int(self.param_id),
        )
