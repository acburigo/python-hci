# Python HCI

This is a library for creating and parsing HCI packets.

**This library is under construction.**

## Supported Python Versions

This library currently supports **Python 3.5** and possibly latter versions.

## Usage

### Create binary packet:

```
In [1]: import hci

In [2]: pkt = hci.command.ATT_ExchangeMTUReq(conn_handle=0x0000, client_rx_mtu=100)

In [3]: print(pkt)
Packet Type: 0x1 (COMMAND)
OpCode: 0xfd02 (ATT_EXCHANGE_MTU_REQUEST)
  OGF: 0x3f (VENDOR_SPECIFIC)
  OCF: 0x102 (258)
Data Length: 0x4 (4)
Connection Handle: 0x0 (0)
Client RX MTU: 0x64 (100)

In [4]: print(pkt.binary)
b'\x01\x02\xfd\x04\x00\x00d\x00'
```

### Parse binary packet:

```
In [1]: import hci

In [2]: pkts, _ = hci.from_binary(b'\x01\x02\xfd\x04\x00\x00d\x00')

In [3]: print(pkts[0])
Packet Type: 0x1 (COMMAND)
OpCode: 0xfd02 (ATT_EXCHANGE_MTU_REQUEST)
  OGF: 0x3f (VENDOR_SPECIFIC)
  OCF: 0x102 (258)
Data Length: 0x4 (4)
Connection Handle: 0x0 (0)
Client RX MTU: 0x64 (100)
```

## Installation

For installing an official release, you may issue the following command:

`pip install hci`

If you are interested in the latest (possibly unstable) features, you may issue the following command:

`pip install git+https://github.com/acburigo/python-hci`

## References
- [Bluetooth Core Specification 5.0](https://www.bluetooth.com/specifications/bluetooth-core-specification)
- [Texas Instruments BLE Vendor Specific HCI Guide](http://www.ti.com/tool/BLE-STACK)

## Developers

This repository is currently maintained by [Arthur Crippa Búrigo](https://github.com/acburigo) and [Pedro Gyrão](https://github.com/pedrogyrao).
