## 1. Generate a private key & address

./python 1_create_p2sh_p2pkh_wit_address.py 

    WIF            L52XzL2cMkHxqxBXRyEpnPQZGUs3uKiL3R11XbAdHigRzDozKZeW
    redeem script  00143442193e1bb70916e914552172cd4e2dbc9df811
    output script  a914f2c6272a69e900a6c703ce55cede85dce4544dc087
    address        3PpgpssV7mcAGpZRWiCWhodUTnjpoSZg7a

Save privkey, and the redeemScript for later

echo "L52XzL2cMkHxqxBXRyEpnPQZGUs3uKiL3R11XbAdHigRzDozKZeW" > wif
echo "00143442193e1bb70916e914552172cd4e2dbc9df811" > rs

## 2. Generate a fake transaction paying to address

python 2_create_coinbase_tx.py 3PpgpssV7mcAGpZRWiCWhodUTnjpoSZg7a

    creating coinbase transaction to 3PpgpssV7mcAGpZRWiCWhodUTnjpoSZg7a
    Here is the tx as hex:
    01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff00ffffffff0100f2052a0100000017a914f2c6272a69e900a6c703ce55cede85dce4544dc08700000000
    
Save the transaction for later:

echo "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff00ffffffff0100f2052a0100000017a914f2c6272a69e900a6c703ce55cede85dce4544dc08700000000" > tx

## 3. Create transaction spending from address

Create a transaction to move coins from our address, to a different address (35Xih3Qy63awXV7zWkLHsjWWLqAhxBWREP)
The transaction will not be signed yet.

python 3_create_unsigned_tx.py ./tx 0 35Xih3Qy63awXV7zWkLHsjWWLqAhxBWREP

    here is the transaction: 0100000001dde254099f5ee6b9abdbdfa81d56bcf8d9085c18b5a4ec4e30bc80ea271b09120000000000ffffffff01f0ca052a0100000017a914f2c6272a69e900a6c703ce55cede85dce4544dc0870000000000f2052a0100000017a914f2c6272a69e900a6c703ce55cede85dce4544dc087

Save the unsigned transaction for later:

echo "0100000001dde254099f5ee6b9abdbdfa81d56bcf8d9085c18b5a4ec4e30bc80ea271b09120000000000ffffffff01f0ca052a0100000017a914f2c6272a69e900a6c703ce55cede85dce4544dc0870000000000f2052a0100000017a914f2c6272a69e900a6c703ce55cede85dce4544dc087" > unsigned
    
## 4. Sign transaction spending from address

python 4_sign_tx.py unsigned wif rs 

    tx 80296533e8c993c171a6132ad7d611af57891d7ba0f955b32f11a649283ffe52 now has 0 bad signature(s)
    Here is the tx as hex:
    01000000000101dde254099f5ee6b9abdbdfa81d56bcf8d9085c18b5a4ec4e30bc80ea271b091200000000171600143442193e1bb70916e914552172cd4e2dbc9df811ffffffff01f0ca052a0100000017a914f2c6272a69e900a6c703ce55cede85dce4544dc0870248304502210095b2ced110d7e5bdbec5b04d98ac30595de3b01927954876825bf763a1af37780220522ee1dac2e81a6ef9ca2ffd6fab31caaebe20d2be8d514df144be6b2ae9856901210339a36013301597daef41fbe593a02cc513d0b55527ec2df1050e2e8ff49c85c200000000