from . import command
from . import event
from . import HciPacket


def _autocast(pkt):
    _packet_type_to_class = {
        HciPacket.PacketType.COMMAND: command.CommandPacket,
        HciPacket.PacketType.EVENT: event.EventPacket,
    }

    _class_to_autocast_func = {
        command.CommandPacket: command._autocast,
        event.EventPacket: event._autocast,
    }

    try:
        pkt.__class__ = _packet_type_to_class[pkt.packet_type]
        pkt = _class_to_autocast_func[type(pkt)](pkt)
    except KeyError:
        pass

    return pkt
