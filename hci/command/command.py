from struct import *
from enum import IntEnum
import binascii


class Commands(IntEnum):
    LE_SET_EVENT_MASK = 0x2001
    LE_READ_BUFFER_SIZE = 0x2002
    LE_READ_LOCAL_SUPPORTED_FEATURES = 0x2003
    LE_SET_RANDOM_ADDRESS = 0x2005
    LE_SET_ADVERTISING_PARAMETERS = 0x2006
    LE_READ_ADVERTISING_CHANNEL_TX_POWER = 0x2007
    LE_SET_ADVERTISING_DATA = 0x2008
    LE_SET_SCAN_RESPONSE_DATA = 0x2009
    LE_SET_ADVERTISE_ENABLE = 0x200A
    LE_SET_SCAN_PARAMETERS = 0x200B
    LE_SET_SCAN_ENABLE = 0x200C
    LE_CREATE_CONNECTION = 0x200D
    LE_CREATE_CONNECTION_CANCEL = 0x200E
    LE_READ_WHITE_LIST_SIZE = 0x200F
    LE_CLEAR_WHITE_LIST = 0x2010
    LE_ADD_DEVICE_TO_WHITE_LIST = 0x2011
    LE_REMOVE_DEVICE_FROM_WHITE_LIST = 0x2012
    LE_CONNECTION_UPDATE = 0x2013
    LE_SET_HOST_CHANNEL_CLASSIFICATION = 0x2014
    LE_READ_CHANNEL_MAP = 0x2015
    LE_READ_REMOTE_USED_FEATURES = 0x2016
    LE_ENCRYPT = 0x2017
    LE_RAND = 0x2018
    LE_START_ENCRYPTION = 0x2019
    LE_LONG_TERM_KEY_REQUESTED_REPLY = 0x201A
    LE_LONG_TERM_KEY_REQUESTED_NEGATIVE_REPLY = 0x201B
    LE_READ_SUPPORTED_STATES = 0x201C
    LE_RECEIVER_TEST = 0x201D
    LE_TRANSMITTER_TEST = 0x201E
    LE_TEST_END_COMMAND = 0x201F
    LE_REMOTE_CONNECTION_PARAMETER_REQUEST_REPLY = 0x2020
    LE_REMOTE_CONNECTION_PARAMETER_REQUEST_NEGATIVE_REPLY = 0x2021
    LE_SET_DATA_LENGTH = 0x2022
    LE_READ_SUGGESTED_DEFAULT_DATA_LENGTH = 0x2023
    LE_WRITE_SUGGESTED_DEFAULT_DATA_LENGTH = 0x2024
    LE_READ_LOCAL_P256_PUBLIC_KEY = 0x2025
    LE_GENERATE_DHKEY = 0x2026
    LE_ADD_DEVICE_TO_RESOLVING_LIST = 0x2027
    LE_REMOVE_DEVICE_FROM_RESOLVING_LIST = 0x2028
    LE_CLEAR_RESOLVING_LIST = 0x2029
    LE_READ_RESOLVING_LIST_SIZE = 0x202A
    LE_READ_PEER_RESOLVABLE_ADDRESS = 0x202B
    LE_READ_LOCAL_RESOLVABLE_ADDRESS = 0x202C
    LE_SET_ADDRESS_RESOLUTION_ENABLE = 0x202D
    LE_SET_RESOLVABLE_PRIVATE_ADDRESS_TIMEOUT = 0x202E
    LE_READ_MAXIMUM_DATA_LENGTH = 0x202F

    DISCONNECT = 0x0406
    READ_REMOTE_VERSION_INFORMATION = 0x041D
    SET_EVENT_MASK = 0x0C01
    HCI_RESET = 0x0C03
    READ_TRANSMIT_POWER_LEVEL = 0x0C2D
    SET_CONTROLLER_TO_HOST_FLOW_CONTROL = 0x0C31
    HOST_BUFFER_SIZE = 0x0C33
    HOST_NUMBER_OF_COMPLETED_PACKETS = 0x0C35
    SET_EVENT_MASK_PAGE_2 = 0x0C63
    READ_AUTHENTICATED_PAYLOAD_TIMEOUT = 0x0C7B
    WRITE_AUTHENTICATED_PAYLOAD_TIMEOUT = 0x0C7C
    READ_LOCAL_VERSION_INFORMATION = 0x1001
    READ_LOCAL_SUPPORTED_COMMANDS = 0x1002
    READ_LOCAL_SUPPORTED_FEATURES = 0x1003
    READ_BD_ADDR = 0x1009
    READ_RSSI = 0x1405

    HCI_EXTENSION_SET_RX_GAIN = 0xFC00
    HCI_EXTENSION_SET_TX_POWER = 0xFC01
    HCI_EXTENSION_ONE_PACKET_PER_EVENT = 0xFC02
    HCI_EXTENSION_CLOCK_DIVIDE_ON_HALT = 0xFC03
    HCI_EXTENSION_DECLARE_NV_USAGE = 0xFC04
    HCI_EXTENSION_DECRYPT = 0xFC05
    HCI_EXTENSION_SET_LOCAL_SUPPORTED_FEATURES = 0xFC06
    HCI_EXTENSION_SET_FAST_TX_RESPONSE_TIME = 0xFC07
    HCI_EXTENSION_MODEM_TEST_TX = 0xFC08
    HCI_EXTENSION_MODEM_HOP_TEST_TX = 0xFC09
    HCI_EXTENSION_MODEM_TEST_RX = 0xFC0A
    HCI_EXTENSION_END_MODEM_TEST = 0xFC0B
    HCI_EXTENSION_SET_BDADDR = 0xFC0C
    HCI_EXTENSION_SET_SCA = 0xFC0D
    HCI_EXTENSION_ENABLE_PTM1 = 0xFC0E
    HCI_EXTENSION_SET_FREQUENCY_TUNING = 0xFC0F
    HCI_EXTENSION_SAVE_FREQUENCY_TUNING = 0xFC10
    HCI_EXTENSION_SET_MAX_DTM_TX_POWER = 0xFC11
    HCI_EXTENSION_MAP_PM_IO_PORT = 0xFC12
    HCI_EXTENSION_DISCONNECT_IMMEDIATE = 0xFC13
    HCI_EXTENSION_PACKET_ERROR_RATE = 0xFC14
    HCI_EXTENSION_PACKET_ERROR_RATE_BY_CHANNEL1 = 0xFC15
    HCI_EXTENSION_EXTEND_RF_RANGE = 0xFC16
    HCI_EXTENSION_ADVERTISER_EVENT_NOTICE = 0xFC17
    HCI_EXTENSION_CONNECTION_EVENT_NOTICE = 0xFC18
    HCI_EXTENSION_HALT_DURING_RF = 0xFC19
    HCI_EXTENSION_SET_SLAVE_LATENCY_OVERRIDE = 0xFC1A
    HCI_EXTENSION_BUILD_REVISION = 0xFC1B
    HCI_EXTENSION_DELAY_SLEEP = 0xFC1C
    HCI_EXTENSION_RESET_SYSTEM = 0xFC1D
    HCI_EXTENSION_OVERLAPPED_PROCESSING = 0xFC1E
    HCI_EXTENSION_NUMBER_COMPLETED_PACKETS_LIMIT = 0xFC1F
    HCI_EXTENSION_GET_CONNECTION_INFORMATION = 0xFC20
    HCI_EXTENSION_SET_MAX_DATA_LENGTH = 0xFC21
    HCI_EXTENSION_SCAN_EVENT_NOTICE = 0xFC22
    HCI_EXTENSION_SCAN_REQUEST_REPORT = 0xFC23

    L2CAP_DISCONNECTION_REQUEST = 0xFC86
    L2CAP_CONNECTION_PARAMETER_UPDATE_REQUEST = 0xFC92
    L2CAP_CONNECTION_REQUEST = 0xFC94
    L2CAP_CONNECTION_RESPONSE = 0xFC95
    L2CAP_FLOW_CONTROL_CREDIT = 0xFC96
    L2CAP_DATA = 0xFCF0
    L2CAP_REGISTER_PSM = 0xFCF1
    L2CAP_DEREGISTER_PSM = 0xFCF2
    L2CAP_PSM_INFO = 0xFCF3
    L2CAP_PSM_CHANNELS = 0xFCF4
    L2CAP_CHANNEL_INFO = 0xFCF5

    ATT_ERROR_RESPONSE = 0xFD01
    ATT_EXCHANGE_MTU_REQUEST = 0xFD02
    ATT_EXCHANGE_MTU_RESPONSE = 0xFD03
    ATT_FIND_INFORMATION_REQUEST = 0xFD04
    ATT_FIND_INFORMATION_RESPONSE = 0xFD05
    ATT_FIND_BY_TYPE_VALUE_REQUEST = 0xFD06
    ATT_FIND_BY_TYPE_VALUE_RESPONSE = 0xFD07
    ATT_READ_BY_TYPE_REQUEST = 0xFD08
    ATT_READ_BY_TYPE_RESPONSE = 0xFD09
    ATT_READ_REQUEST = 0xFD0A
    ATT_READ_RESPONSE = 0xFD0B
    ATT_READ_BLOB_REQUEST = 0xFD0C
    ATT_READ_BLOB_RESPONSE = 0xFD0D
    ATT_READ_MULTIPLE_REQUEST = 0xFD0E
    ATT_READ_MULTIPLE_RESPONSE = 0xFD0F
    ATT_READ_BY_GROUP_TYPE_REQUEST = 0xFD10
    ATT_READ_BY_GROUP_TYPE_RESPONSE = 0xFD11
    ATT_WRITE_REQUEST = 0xFD12
    ATT_WRITE_RESPONSE = 0xFD13
    ATT_PREPARE_WRITE_REQUEST = 0xFD16
    ATT_PREPARE_WRITE_RESPONSE = 0xFD17
    ATT_EXECUTE_WRITE_REQUEST = 0xFD18
    ATT_EXECUTE_WRITE_RESPONSE = 0xFD19
    ATT_HANDLE_VALUE_NOTIFICATION = 0xFD1B
    ATT_HANDLE_VALUE_INDICATION = 0xFD1D
    ATT_HANDLE_VALUE_CONFIRMATION = 0xFD1E

    GATT_DISCOVER_CHARACTERISTICS_BY_UUID = 0xFD88
    GATT_WRITE_LONG = 0xFD96

    GAP_DEVICE_INITIALIZATION = 0xFE00
    GAP_CONFIGURE_DEVICE_ADDRESS = 0xFE03
    GAP_DEVICE_DISCOVERY_REQUEST = 0xFE04
    GAP_DEVICE_DISCOVERY_CANCEL = 0xFE05
    GAP_MAKE_DISCOVERABLE = 0xFE06
    GAP_UPDATE_ADVERTISING_DATA = 0xFE07
    GAP_END_DISCOVERABLE = 0xFE08
    GAP_ESTABLISH_LINK_REQUEST = 0xFE09
    GAP_TERMINATE_LINK_REQUEST = 0xFE0A
    GAP_AUTHENTICATE = 0xFE0B
    GAP_PASSKEY_UPDATE = 0xFE0C
    GAP_SLAVE_SECURITY_REQUEST = 0xFE0D
    GAP_SIGNABLE = 0xFE0E
    GAP_BOND = 0xFE0F
    GAP_TERMINATE_AUTH = 0xFE10
    GAP_UPDATE_LINK_PARAMETER_REQUEST = 0xFE11
    GAP_UPDATE_LINK_PARAMETER_REQUEST_REPLY = 0xFE12
    GAP_SET_PARAMETER = 0xFE30
    GAP_GET_PARAMETER = 0xFE31
    GAP_RESOLVE_PRIVATE_ADDRESS = 0xFE32
    GAP_SET_ADVERTISEMENT_TOKEN = 0xFE33
    GAP_REMOVE_ADVERTISEMENT_TOKEN = 0xFE34
    GAP_UPDATE_ADVERTISEMENT_TOKENS = 0xFE35
    GAP_BOND_SET_PARAMETER = 0xFE36
    GAP_BOND_GET_PARAMETER = 0xFE37

    UTIL_RESERVED = 0xFE80
    UTIL_NV_READ = 0xFE81
    UTIL_NV_WRITE = 0xFE82

    RESERVED = 0xFF00

    USER_PROFILES = 0xFF80


class CommandPacket:
    PACKET_TYPE = 0x01
    OFFSET_DATA_LENGTH = 0x03

    def __init__(self, opcode, parameters=b''):
        self.opcode = opcode
        self.parameter_total_length = len(parameters)
        self.parameters = parameters

    def _get_parameter(self, offset, size_octets):
        return self.parameters[offset: offset + size_octets]

    def to_binary(self):
        return pack('<BHB',
                    CommandPacket.PACKET_TYPE,
                    self.opcode,
                    self.parameter_total_length) + self.parameters

    def __str__(self):
        return '\n'.join([
            'Packet Type: {} ({})',
            'OpCode: {} ({})',
            'Data Length: {} ({})',
            'Parameters: {}',
        ]).format(
            hex(CommandPacket.PACKET_TYPE),
            int(CommandPacket.PACKET_TYPE),
            hex(self.opcode),
            Commands(self.opcode).name,
            hex(self.parameter_total_length),
            int(self.parameter_total_length),
            binascii.hexlify(self.parameters).decode('utf-8'),
        )

    @staticmethod
    def from_binary(buffer):
        opcode, parameter_total_length = unpack_from('<HB', buffer, offset=1)

        return CommandPacket(
            opcode=opcode,
            parameters=buffer[4:]
        )


def _hex_address_to_bytes(addr):
    return binascii.unhexlify(addr.replace(':', ''))


class HCI_Reset(CommandPacket):
    def __init__(self):
        super().__init__(Commands.HCI_RESET)


class GAP_DeviceInit(CommandPacket):
    class ProfileRoles(IntEnum):
        GAP_PROFILE_BROADCASTER = 0x01
        GAP_PROFILE_OBSERVER = 0x02
        GAP_PROFILE_PERIPHERAL = 0x04
        GAP_PROFILE_CENTRAL = 0x08

    def __init__(self, profile_role, max_scan_responses, irk, csrk,
                 sign_counter):
        super().__init__(
            Commands.GAP_DEVICE_INITIALIZATION,
            GAP_DeviceInit._params_to_binary(
                profile_role, max_scan_responses, irk, csrk, sign_counter)
        )

    @staticmethod
    def _params_to_binary(profile_role, max_scan_responses, irk, csrk,
                          sign_counter):
        return pack('<BB16B16BI',
                    profile_role,
                    max_scan_responses,
                    *tuple(_hex_address_to_bytes(irk)),
                    *tuple(_hex_address_to_bytes(csrk)),
                    sign_counter)

    @property
    def profile_role(self):
        OFFSET, SIZE_OCTETS = 0, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def max_scan_responses(self):
        OFFSET, SIZE_OCTETS = 1, 1
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def irk(self):
        OFFSET, SIZE_OCTETS = 2, 16
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return data

    @property
    def csrk(self):
        OFFSET, SIZE_OCTETS = 18, 16
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return data

    @property
    def sign_counter(self):
        OFFSET, SIZE_OCTETS = 34, 4
        data = self._get_parameter(OFFSET, SIZE_OCTETS)
        return unpack('<I', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Profile Role: {} ({})',
            'Max. Scan Responses: {} ({})',
            'IRK: {}',
            'CSRK: {}',
            'Sign Counter: {} ({})',
        ]).format(
            hex(self.profile_role),
            GAP_DeviceInit.ProfileRoles(self.profile_role).name,
            hex(self.max_scan_responses),
            int(self.max_scan_responses),
            binascii.hexlify(self.irk).decode('utf-8'),
            binascii.hexlify(self.csrk).decode('utf-8'),
            hex(self.sign_counter),
            int(self.sign_counter),
        )
