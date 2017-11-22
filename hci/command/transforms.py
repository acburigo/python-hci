import binascii


def _hex_address_to_bytes(addr):
    return binascii.unhexlify(addr.replace(':', ''))
