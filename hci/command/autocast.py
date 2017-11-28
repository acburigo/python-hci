from .opcode import OpCode
from .commands import *


def _autocast(pkt):
    _opcode_to_class = {
        OpCode.ATT_EXCHANGE_MTU_REQUEST: ATT_ExchangeMTUReq,
        OpCode.GAP_DEVICE_DISCOVERY_REQUEST: GAP_DeviceDiscoveryRequest,
        OpCode.GAP_DEVICE_INITIALIZATION: GAP_DeviceInit,
        OpCode.GAP_ESTABLISH_LINK_REQUEST: GAP_EstablishLinkReq,
        OpCode.GAP_GET_PARAMETER: GAP_GetParam,
        OpCode.GATT_WRITE: GATT_WriteCharValue,
        OpCode.HCI_RESET: HCI_Reset,
        OpCode.UTIL_BUILD_REVISION: UTIL_BuildRevision,
    }

    try:
        pkt.__class__ = _opcode_to_class[pkt.opcode]
    except KeyError:
        pass

    return pkt
