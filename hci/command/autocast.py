from .opcode import OpCode
from .commands import *


def _autocast(pkt):
    _opcode_to_class = {
        OpCode.ATT_EXCHANGE_MTU_REQUEST:
            ATT_ExchangeMtuReq,

        OpCode.GAP_DEVICE_DISCOVERY_REQUEST:
            GAP_DeviceDiscoveryRequest,

        OpCode.GAP_DEVICE_INITIALIZATION:
            GAP_DeviceInit,

        OpCode.GAP_ESTABLISH_LINK_REQUEST:
            GAP_EstablishLinkReq,

        OpCode.GAP_GET_PARAMETER:
            GAP_GetParam,

        OpCode.GAP_SET_PARAMETER:
            GAP_SetParam,

        OpCode.GAP_TERMINATE_LINK_REQUEST:
            GAP_TerminateLinkReq,

        OpCode.GAP_UPDATE_LINK_PARAMETER_REQUEST:
            GAP_UpdateLinkParamReq,

        OpCode.GAP_UPDATE_LINK_PARAMETER_REQUEST_REPLY:
            GAP_UpdateLinkParamReqReply,

        OpCode.GATT_DISC_ALL_CHAR_DESCS:
            GATT_DiscAllCharDescs,

        OpCode.GATT_READ:
            GATT_ReadCharValue,

        OpCode.GATT_WRITE:
            GATT_WriteCharValue,

        OpCode.HCI_EXTENSION_ONE_PACKET_PER_EVENT:
            HCI_EXT_OnePktPerEvt,

        OpCode.HCI_EXTENSION_PACKET_ERROR_RATE:
            HCI_EXT_PacketErrorRate,

        OpCode.HCI_EXTENSION_RESET_SYSTEM:
            HCI_EXT_ResetSystem,

        OpCode.HCI_EXTENSION_SET_TX_POWER:
            HCI_EXT_SetTxPower,

        OpCode.READ_RSSI:
            HCI_ReadRssi,

        OpCode.HCI_RESET:
            HCI_Reset,

        OpCode.LE_SET_DATA_LENGTH:
            LE_SetDataLength,

        OpCode.LE_SET_DEFAULT_PHY:
            LE_SetDefaultPhy,

        OpCode.LE_SET_PHY:
            LE_SetPhy,

        OpCode.UTIL_BUILD_REVISION:
            UTIL_BuildRevision,

        OpCode.UTIL_FORCE_BOOT:
            UTIL_ForceBoot,
    }

    try:
        pkt.__class__ = _opcode_to_class[pkt.opcode]
    except KeyError:
        pass

    return pkt
