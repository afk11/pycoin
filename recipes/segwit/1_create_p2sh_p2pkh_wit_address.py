#!/usr/bin/env python

# This script shows you how to create a "2-of-3" multisig address.
# It requires BIP32 private key file.

import os
import sys

from pycoin.key.BIP32Node import BIP32Node
from pycoin.key.Key import Key
from pycoin.encoding.hexbytes import h2b, b2h
from pycoin.ecdsa.secp256k1 import secp256k1_generator
from pycoin.symbols.btc import network as BitcoinMainnet

# this is a shortcut, probably more to it.
Key._ui_context = BitcoinMainnet.ui

address_for_script = BitcoinMainnet.ui.address_for_script
script_for_address = BitcoinMainnet.ui.script_for_address
script_for_p2pkh_wit = BitcoinMainnet.ui._script_info.script_for_p2pkh_wit
script_for_p2s = BitcoinMainnet.ui._script_info.script_for_p2s


def main():
    # turn the bip32 text into a BIP32Node object
    BIP32_KEY = BIP32Node.from_master_secret(h2b("000102030405060708090a0b0c0d0e0f"), secp256k1_generator)

    hash160 = BIP32_KEY.hash160(use_uncompressed=False)
    redeem_script = script_for_p2pkh_wit(hash160)

    script = script_for_p2s(redeem_script)
    address = address_for_script(script)

    print('WIF           ', BIP32_KEY.wif())
    print('redeem script ', b2h(redeem_script))
    print('output script ', b2h(script))
    print('address       ', address)


if __name__ == '__main__':
    main()
