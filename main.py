from web3 import Web3
from web3.middleware import geth_poa_middleware
from os.path import join
import json

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

checksum_addr = Web3.toChecksumAddress('0xd84c7249af903d2e7f6ae66626f97f09f8bcb59f') #CONTRACT ADDRESS

abi = {}
with open(join("abi_test", "c.json")) as psc_abi:
    abi = json.load(psc_abi)
pcs_contract = w3.eth.contract(address=checksum_addr, abi=abi)

nonce = w3.eth.getTransactionCount('0xF22402Dff34CDDB791bc939A3bB7329383A11e2D') #YOUR BSC ADDRESS

tx = pcs_contract.functions.claimFunding().buildTransaction({
     'chainId': 56,
     'from': '0xF22402Dff34CDDB791bc939A3bB7329383A11e2D',
     'nonce': nonce,
      })

private_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" #YOUR BSC ADDRESS PRIVATE KEY

signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)


send = w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
print(send)
