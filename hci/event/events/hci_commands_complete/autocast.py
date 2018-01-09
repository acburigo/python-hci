from hci.event.events import hci_commands_complete
from hci.command.opcode import OpCode


def _autocast(pkt):
    _opcode_to_class = {
        OpCode.READ_RSSI: hci_commands_complete.HCI_ReadRssi,
    }

    try:
        pkt.__class__ = _opcode_to_class[pkt.opcode]
    except KeyError:
        pass

    return pkt
