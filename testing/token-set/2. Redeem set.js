const BigNumber = require('bignumber.js');
const ethers = require("ethers");
const Web3 = require('web3');
const YAML = require('yaml');
const fs = require('fs');
const SetProtocol = require('setprotocol.js').default;
const HDWalletProvider = require('@truffle/hdwallet-provider');


const file = fs.readFileSync('../config.yaml', 'utf8')
const env = YAML.parse(file)

const PUBLIC_KEY = env['addresses']['demo']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['demo']['PRIVATE_KEY']
const INFURA_URL_HTTPS = env['INFURA']['kovan']['HTTPS'] + env['INFURA']['ID']
const INFURA_URL_WS = env['INFURA']['kovan']['WS'] + env['INFURA']['ID']
const KOVAN_CONFIG = env['configSetProtocol']['kovan']['config']

let web3 = new Web3(new HDWalletProvider(PRIVATE_KEY, INFURA_URL_HTTPS));
const setProtocol = new SetProtocol(web3, KOVAN_CONFIG)

const setAddress = '0x869b8ad1ca9fb33ae0f8f9095574b1439a984891'
const addressTrueUSD = '0xadb015d61f4beb2a712d237d9d4c5b75bafefd7b';
const addressDAI = '0x1d82471142F0aeEEc9FC375fC975629056c26ceE'
const componentAddresses = [addressTrueUSD, addressDAI]
const name = 'Fart Set';
const symbol = 'FART';
const txOpts = {
  from: PUBLIC_KEY,
  gas: 4000000,
  gasPrice: 8000000000,
};


const redeemSet = async function() {
  // Redeem half a token
  const quantity = new BigNumber(0.5 * 10 ** 18);
  const withdraw = true;
  const tokensToExclude = [];

  const txHash = await setProtocol.redeemAsync(
    setAddress,
    quantity,
    withdraw,
    tokensToExclude,
    txOpts,
  );

  return txHash;
};

redeemSet().then(console.log);
