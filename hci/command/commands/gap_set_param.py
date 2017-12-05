from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class GAP_SetParam(CommandPacket):
    class ParamId(IntEnum):
        TGAP_GEN_DISC_ADV_MIN = 0
        TGAP_LIM_ADV_TIMEOUT = 1
        TGAP_GEN_DISC_SCAN = 2
        TGAP_LIM_DISC_SCAN = 3
        TGAP_CONN_EST_ADV_TIMEOUT = 4
        TGAP_CONN_PARAM_TIMEOUT = 5
        TGAP_LIM_DISC_ADV_INT_MIN = 6
        TGAP_LIM_DISC_ADV_INT_MAX = 7
        TGAP_GEN_DISC_ADV_INT_MIN = 8
        TGAP_GEN_DISC_ADV_INT_MAX = 9
        TGAP_CONN_ADV_INT_MIN = 10
        TGAP_CONN_ADV_INT_MAX = 11
        TGAP_CONN_SCAN_INT = 12
        TGAP_CONN_SCAN_WIND = 13
        TGAP_CONN_HIGH_SCAN_INT = 14
        TGAP_CONN_HIGH_SCAN_WIND = 15
        TGAP_GEN_DISC_SCAN_INT = 16
        TGAP_GEN_DISC_SCAN_WIND = 17
        TGAP_LIM_DISC_SCAN_INT = 18
        TGAP_LIM_DISC_SCAN_WIND = 19
        TGAP_CONN_EST_ADV = 20
        TGAP_CONN_EST_INT_MIN = 21
        TGAP_CONN_EST_INT_MAX = 22
        TGAP_CONN_EST_SCAN_INT = 23
        TGAP_CONN_EST_SCAN_WIND = 24
        TGAP_CONN_EST_SUPERV_TIMEOUT = 25
        TGAP_CONN_EST_LATENCY = 26
        TGAP_CONN_EST_MIN_CE_LEN = 27
        TGAP_CONN_EST_MAX_CE_LEN = 28
        TGAP_PRIVATE_ADDR_INT = 29
        TGAP_CONN_PAUSE_CENTRAL = 30
        TGAP_CONN_PAUSE_PERIPHERAL = 31
        TGAP_SM_TIMEOUT = 32
        TGAP_SM_MIN_KEY_LEN = 33
        TGAP_SM_MAX_KEY_LEN = 34
        TGAP_FILTER_ADV_REPORTS = 35
        TGAP_SCAN_RSP_RSSI_MIN = 36
        TGAP_REJECT_CONN_PARAMS = 37
        TGAP_GAP_TESTCODE = 38
        TGAP_SM_TESTCODE = 39
        TGAP_GATT_TESTCODE = 100
        TGAP_ATT_TESTCODE = 101
        TGAP_GGS_TESTCODE = 102
        TGAP_L2CAP_TESTCODE = 103

    def __init__(self, param_id, param_value):
        super().__init__(
            CommandPacket.OpCode.GAP_SET_PARAMETER,
            GAP_SetParam._params_to_binary(param_id, param_value)
        )

    @staticmethod
    def _params_to_binary(param_id, param_value):
        return pack('<BH', param_id, param_value)

    @property
    def param_id(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def param_value(self):
        OFFSET, SIZE_OCTETS = 5, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Parameter ID: {} ({})',
            'Parameter Value: {} ({})',
        ]).format(
            hex(self.param_id),
            int(self.param_id),
            hex(self.param_value),
            int(self.param_value),
        )
