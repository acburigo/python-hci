from .event_codes import EventCodes
from . import events


def _autocast(pkt):
    _event_code_to_class = {
        EventCodes.VENDOR_SPECIFIC_EVENT: events.VendorSpecificEvent
    }
    _class_to_autocast_func = {
        events.VendorSpecificEvent: events.vendor_specific._autocast
    }
    try:
        pkt.__class__ = _event_code_to_class[pkt.event_code]
        pkt = _class_to_autocast_func[type(pkt)](pkt)
    except KeyError:
        pass

    return pkt
