from web3 import Web3
from solc import compile_standard
import yaml
import json

with open('ABI.json', 'r') as myfile:
    ABI = json.load(myfile)

with open('config.yaml', 'r') as myfile:
    config = yaml.load(myfile, Loader=yaml.Loader)

PUBLIC_KEY = config['addresses']['demo']['PUBLIC_KEY']
PRIVATE_KEY = config['addresses']['demo']['PRIVATE_KEY']

web = Web3(Web3.HTTPProvider(config['INFURA']))
# ------------------------------------------------------------------------------------
# Basic

web.isConnected()

my_address = web.ens.address('fartset.eth')

web.eth.getBalance(PUBLIC_KEY)
web.eth.defaultAccount = PUBLIC_KEY


# ------------------------------------------------------------------------------------
# Transactions

# -------------------------------------------
# Good transactions

transaction = {
    'to': web.ens.address('fartset.eth'),
    'value': 123,
    'gas': 21000,
    'gasPrice': 9 * 10**9,
    'nonce': web.eth.getTransactionCount(web.eth.defaultAccount)
}

signed = web.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)
response = web.eth.sendRawTransaction(signed.rawTransaction)  # HexBytes('0xc2cc8d9584e711580a44dccc18c37e587f3be722c0a03b57e7eb08820ff6d94c')

receipt = web.eth.getTransactionReceipt(response)

# -------------------------------------------
# Bad transactions (TODO)

# gasPrice too low
transaction.update(**{'gasPrice': 0.1 * 10**9, 'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)})


# ------------------------------------------------------------------------------------
# Contracts

# ENS smart contract
multisig_address = '0x3a6c6641E967c8CeCd017e3E3e5Ab566f0840F67'

contract = web.eth.contract(web.toChecksumAddress(ens_address), abi=ABI)


contract.all_functions()
