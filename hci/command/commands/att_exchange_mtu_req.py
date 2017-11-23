from struct import pack, unpack

from ..command_packet import CommandPacket
from ..opcode import OpCode


class ATT_ExchangeMTUReq(CommandPacket):
    def __init__(self, conn_handle, client_rx_mtu):
        super().__init__(
            OpCode.ATT_EXCHANGE_MTU_REQUEST,
            ATT_ExchangeMTUReq._params_to_binary(conn_handle, client_rx_mtu)
        )

    @staticmethod
    def _params_to_binary(conn_handle, client_rx_mtu):
        return pack('<HH', conn_handle, client_rx_mtu)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def client_rx_mtu(self):
        OFFSET, SIZE_OCTETS = 6, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'Client RX MTU: {} ({})',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.client_rx_mtu),
            int(self.client_rx_mtu),
        )
