import binascii


def _hex_string_to_bytes(addr, revert=True):
    b = binascii.unhexlify(addr.replace(':', ''))

    if (revert):
        b = b[::-1]

    return b


def _bytes_to_hex_string(data):
    return ':'.join('{:02X}'.format(byte) for byte in data)
