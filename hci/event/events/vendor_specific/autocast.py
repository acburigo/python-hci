from ..vendor_specific_events import VendorSpecificEvents
from hci.event.events import vendor_specific


def _autocast(pkt):
    _event_to_class = {
        VendorSpecificEvents.ATT_HANDLE_VALUE_NOTIFICATION:
            vendor_specific.ATTHandleValueNotification,
        VendorSpecificEvents.GAP_DEVICE_INIT_DONE:
            vendor_specific.GAP_DeviceInitDone,
        VendorSpecificEvents.GAP_COMMAND_STATUS:
            vendor_specific.GAP_HCI_ExtentionCommandStatus,
        VendorSpecificEvents.GAP_DEVICE_INFORMATION:
            vendor_specific.GAP_DeviceInformation,
        VendorSpecificEvents.GAP_DEVICE_DISCOVERY:
            vendor_specific.GAP_DeviceDiscoveryDone
    }

    try:
        pkt.__class__ = _event_to_class[pkt.event]
    except KeyError:
        pass

    return pkt
