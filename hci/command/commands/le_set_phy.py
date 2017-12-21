from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class LE_SetPhy(CommandPacket):
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

    class PhyOptions(IntEnum):
        ANY_CODING = 0
        S2_CODING = 1
        S8_CODING = 2

    def __init__(self, conn_handle, all_phys, tx_phys, rx_phys, phy_options):
        super().__init__(
            CommandPacket.OpCode.LE_SET_PHY,
            LE_SetPhy._params_to_binary(
                conn_handle, all_phys, tx_phys, rx_phys, phy_options)
        )

    @staticmethod
    def _params_to_binary(
            conn_handle, all_phys, tx_phys, rx_phys, phy_options):
        return pack('<HBBBH',
                    conn_handle, all_phys, tx_phys, rx_phys, phy_options)

    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def all_phys(self):
        OFFSET, SIZE_OCTETS = 6, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def tx_phys(self):
        OFFSET, SIZE_OCTETS = 7, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def rx_phys(self):
        OFFSET, SIZE_OCTETS = 8, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def phy_options(self):
        OFFSET, SIZE_OCTETS = 9, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        all_phys_str = ' | '.join([
            e.name for e in LE_SetPhy.AllPhys if e & self.all_phys])
        tx_phys_str = ' | '.join([
            e.name for e in LE_SetPhy.TxPhys if e & self.tx_phys])
        rx_phys_str = ' | '.join([
            e.name for e in LE_SetPhy.RxPhys if e & self.rx_phys])

        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'All PHYs: {} ({})',
            'Tx PHYs: {} ({})',
            'Rx PHYs: {} ({})',
            'PHY Options: {} ({})',
        ]).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.all_phys),
            all_phys_str,
            hex(self.tx_phys),
            tx_phys_str,
            hex(self.rx_phys),
            rx_phys_str,
            hex(self.phy_options),
            LE_SetPhy.PhyOptions(self.phy_options).name,
        )
