from enum import IntEnum
from struct import unpack_from

from hci.event import EventPacket
from .vendor_specific_events import VendorSpecificEvents


class VendorSpecificEvent(EventPacket):
    class Status(IntEnum):
        SUCCESS = 0x00
        FAILURE = 0x01
        INVALIDPARAMETER = 0x02
        INVALID_TASK = 0x03
        MSG_BUFFER_NOT_AVAIL = 0x04
        INVALID_MSG_POINTER = 0x05
        INVALID_EVENT_ID = 0x06
        INVALID_INTERRUPT_ID = 0x07
        NO_TIMER_AVAIL = 0x08
        NV_ITEM_UNINIT = 0x09
        NV_OPER_FAILED = 0x0A
        INVALID_MEM_SIZE = 0x0B
        NV_BAD_ITEM_LEN = 0x0C
        BLE_NOT_READY = 0X10
        BLE_ALREADY_IN_REQUESTED_MODE = 0X11
        BLE_INCORRECT_MODE = 0X12
        BLE_MEMALLOC_ERROR = 0X13
        BLE_NOT_CONNECTED = 0X14
        BLE_NO_RESOURCES = 0X15
        BLE_PENDING = 0X16
        BLE_TIMEOUT = 0X17
        BLE_INVALID_RANGE = 0X18
        BLE_LINK_ENCRYPTED = 0X19
        BLE_PROCEDURE_COMPLETE = 0X1A
        BLE_GAP_USER_CANCELED = 0X30
        BLE_GAP_CONN_NOT_ACCEPTABLE = 0X31
        BLE_GAP_BOND_REJECTED = 0X32
        BLE_INVALID_PDU = 0X40
        BLE_INSUFFICIENT_AUTHEN = 0X41
        BLE_INSUFFICIENT_ENCRYPT = 0X42
        BLE_INSUFFICIENT_KEY_SIZE = 0x43
        INVALID_TASK_ID = 0xFF

    class EventType(IntEnum):
        CONNECTABLE_UNDIRECTED_ADVERTISEMENT = 0x00
        CONNECTABLE_DIRECTED_ADVERTISEMENT = -0x01
        DISCOVERABLE_UNDIRECTED_ADVERTISEMENT = 0x02
        NON_CONNECTABLE_UNDIRECTED_ADVERTISEMENT = 0x03
        SCAN_RESPONSE = 4

    class AdressType(IntEnum):
        ADDRTYPE_PUBLIC = 0x00
        ADDRTYPE_STATIC = 0x01
        ADDRTYPE_PRIVATE_NONRESOLVE = 0x02
        ADDRTYPE_PRIVATE_RESOLVE = 0x03

    @property
    def event(self):
        OFFSET, SIZE_OCTETS = 3, 2
        event = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', event)[0]

    @property
    def status(self):
        OFFSET, SIZE_OCTETS = 5, 1
        status = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', status)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Event: {} ({})',
            'Status: {} ({})']).format(
            hex(self.event),
            VendorSpecificEvents(self.event).name,
            hex(self.status),
            VendorSpecificEvent.Status(self.status).name)
