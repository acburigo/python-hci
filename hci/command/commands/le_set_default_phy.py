from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class LE_SetDefaultPhy(CommandPacket):
    class AllPhys(IntEnum):
        ANY_TX = 1
        ANY_RX = 2

    class TxPhys(IntEnum):
        LE_1M = 1
        LE_2M = 2
        LE_CODED = 4

    class RxPhys(IntEnum):
        LE_1M = 1
        LE_2M = 2
        LE_CODED = 4

    def __init__(self, all_phys, tx_phys, rx_phys):
        super().__init__(
            CommandPacket.OpCode.LE_SET_DEFAULT_PHY,
            LE_SetDefaultPhy._params_to_binary(all_phys, tx_phys, rx_phys)
        )

    @staticmethod
    def _params_to_binary(all_phys, tx_phys, rx_phys):
        return pack('<BBB', all_phys, tx_phys, rx_phys)

    @property
    def all_phys(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def tx_phys(self):
        OFFSET, SIZE_OCTETS = 5, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def rx_phys(self):
        OFFSET, SIZE_OCTETS = 6, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        all_phys_str = ' | '.join([
            e.name for e in LE_SetDefaultPhy.AllPhys if e & self.all_phys])
        tx_phys_str = ' | '.join([
            e.name for e in LE_SetDefaultPhy.TxPhys if e & self.tx_phys])
        rx_phys_str = ' | '.join([
            e.name for e in LE_SetDefaultPhy.RxPhys if e & self.rx_phys])

        return super().__str__() + '\n' + '\n'.join([
            'All PHYs: {} ({})',
            'Tx PHYs: {} ({})',
            'Rx PHYs: {} ({})',
        ]).format(
            hex(self.all_phys),
            all_phys_str,
            hex(self.tx_phys),
            tx_phys_str,
            hex(self.rx_phys),
            rx_phys_str,
        )
