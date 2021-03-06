from .event_codes import EventCodes
from . import events


def _autocast(pkt):
    _event_code_to_class = {
        EventCodes.VENDOR_SPECIFIC_EVENT: events.VendorSpecificEvent,
        EventCodes.HCI_COMMAND_COMPLETE: events.HCI_CommandComplete
    }
    _class_to_autocast_func = {
        events.VendorSpecificEvent: events.vendor_specific._autocast,
        events.HCI_CommandComplete: events.hci_commands_complete._autocast,
    }
    try:
        pkt.__class__ = _event_code_to_class[pkt.event_code]
        pkt = _class_to_autocast_func[type(pkt)](pkt)
    except KeyError:
        pass

    return pkt
