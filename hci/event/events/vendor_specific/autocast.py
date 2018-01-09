from ..vendor_specific_events import VendorSpecificEvents
from hci.event.events import vendor_specific


def _autocast(pkt):
    _event_to_class = {
        VendorSpecificEvents.ATT_HANDLE_VALUE_NOTIFICATION:
            vendor_specific.ATT_HandleValueNotification,
        VendorSpecificEvents.GAP_DEVICE_INIT_DONE:
            vendor_specific.GAP_DeviceInitDone,
        VendorSpecificEvents.GAP_COMMAND_STATUS:
            vendor_specific.GAP_HCI_ExtentionCommandStatus,
        VendorSpecificEvents.GAP_DEVICE_INFORMATION:
            vendor_specific.GAP_DeviceInformation,
        VendorSpecificEvents.GAP_DEVICE_DISCOVERY:
            vendor_specific.GAP_DeviceDiscoveryDone,
        VendorSpecificEvents.GAP_LINK_ESTABLISHED:
            vendor_specific.GAP_LinkEstablished,
        VendorSpecificEvents.GAP_LINK_PARAMETER_UPDATE:
            vendor_specific.GAP_LinkParamUpdate,
        VendorSpecificEvents.ATT_WRITE_RESPONSE:
            vendor_specific.ATT_WriteResponse,
        VendorSpecificEvents.GAP_LINK_TERMINATED:
            vendor_specific.GAP_LinkTerminated,
        VendorSpecificEvents.ATT_EXCHANGE_MTU_RESPONSE:
            vendor_specific.ATT_ExchangeMtuResponse,
        VendorSpecificEvents.ATT_MTU_UPDATED_EVT:
            vendor_specific.ATT_MtuUpdated,
        VendorSpecificEvents.ATT_ERROR_RESPONSE:
            vendor_specific.ATT_ErrorResponse,
        VendorSpecificEvents.HCI_EXTENSION_PACKET_ERROR_RATE:
            vendor_specific.HCI_Extension_PacketErrorRate,
        VendorSpecificEvents.ATT_READ_RESPONSE:
            vendor_specific.ATT_ReadResponse,
        VendorSpecificEvents.HCI_EXTENSION_SET_TX_POWER:
            vendor_specific.HCI_EXT_SetTxPowerDone,
        VendorSpecificEvents.HCI_EXTENSION_RESET_SYSTEM:
            vendor_specific.HCI_EXT_ResetSystemDone,
    }

    try:
        pkt.__class__ = _event_to_class[pkt.event]
    except KeyError:
        pass

    return pkt
