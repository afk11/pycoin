#!/usr/bin/env python

# This script shows you how to spend coins from an incoming transaction.
# It expects an incoming transaction in hex format a file ("incoming-tx.hex")
# and a bitcoin address, and it spends the coins from the selected output of
# in incoming transaction to the address you choose.

# It does NOT sign the transaction. That's done by 4_sign_tx.py.

import sys

from pycoin.symbols.btc import network as BitcoinMainnet
from pycoin.coins.tx_utils import create_tx

script_for_address = BitcoinMainnet.ui.script_for_address
Tx = BitcoinMainnet.tx
TxIn = BitcoinMainnet.tx.TxIn
TxOut = BitcoinMainnet.tx.TxOut



def main():
    if len(sys.argv) != 4:
        print("usage: %s incoming_tx_hex_filename tx_out_index new_address" % sys.argv[0])
        sys.exit(-1)

    with open(sys.argv[1], "r") as f:
        tx_hex = f.readline().strip()

    # get the spendable from the prior transaction
    tx = Tx.from_hex(tx_hex)
    tx_out_index = int(sys.argv[2])
    spendable = tx.tx_outs_as_spendable()[tx_out_index]

    # make sure the address is valid
    payable = sys.argv[3]

    # create the unsigned transaction
    tx = create_tx([spendable], [payable])

    print("here is the transaction: %s" % tx.as_hex(include_unspents=True))


if __name__ == '__main__':
    main()