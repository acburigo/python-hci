from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class HCI_EXT_SetTxPower(CommandPacket):

    class TxPower(IntEnum):
        HCI_EXT_TX_POWER_MINUS_21_DBM = 0x00
        HCI_EXT_TX_POWER_MINUS_18_DBM = 0x01
        HCI_EXT_TX_POWER_MINUS_15_DBM = 0x02
        HCI_EXT_TX_POWER_MINUS_12_DBM = 0x03
        HCI_EXT_TX_POWER_MINUS_9_DBM = 0x04
        HCI_EXT_TX_POWER_MINUS_6_DBM = 0x05
        HCI_EXT_TX_POWER_MINUS_3_DBM = 0x06
        HCI_EXT_TX_POWER_0_DBM = 0x07
        HCI_EXT_TX_POWER_1_DBM = 0x08
        HCI_EXT_TX_POWER_2_DBM = 0x09
        HCI_EXT_TX_POWER_3_DBM = 0x0a
        HCI_EXT_TX_POWER_4_DBM = 0x0b
        HCI_EXT_TX_POWER_5_DBM = 0x0c

    def __init__(self, tx_power):
        super().__init__(
            CommandPacket.OpCode.HCI_EXTENSION_SET_TX_POWER,
            HCI_EXT_SetTxPower._params_to_binary(tx_power)
        )

    @staticmethod
    def _params_to_binary(tx_power):
        return pack('<B', tx_power)

    @property
    def tx_power(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Tx Power: {} ({})',
        ]).format(
            hex(self.tx_power),
            HCI_EXT_SetTxPower.TxPower(self.tx_power).name,
        )
