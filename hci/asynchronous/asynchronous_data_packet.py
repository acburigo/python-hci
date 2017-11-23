from ..hci_packet import HciPacket


class AsynchronousDataPacket(HciPacket):
    OFFSET_DATA_LENGTH = 0x03
