from web3.auto.infura import w3
from solc import compile_standard
import yaml

with open('config.yaml', 'r') as myfile:
    config = yaml.load(myfile, Loader=yaml.Loader)

PUBLIC_KEY = config['addresses']['demo']['PUBLIC_KEY']
PRIVATE_KEY = config['addresses']['demo']['PRIVATE_KEY']

w3.isConnected()

# ------------------------------------------------------------------------------------

# my_address = w3.ens.address('fartset.eth')
w3.eth.getBalance(PUBLIC_KEY)
w3.eth.defaultAccount = PUBLIC_KEY

transaction = {
    'to': w3.ens.address('fartset.eth'),
    'value': 123,
    'gas': 21000,
    'gasPrice': 9 * 10**9,
    'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
}

signed = w3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

# Send transaction
response = w3.eth.sendRawTransaction(signed.rawTransaction)  # HexBytes('0xc2cc8d9584e711580a44dccc18c37e587f3be722c0a03b57e7eb08820ff6d94c')
