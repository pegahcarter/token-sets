// https://docs.setprotocol.com/#/tutorials#getting-testnet-erc20-tokens
// import BigNumber from 'bignumber.js';
// import ethers from "ethers";
// import YAML from 'yaml';
// import fs from 'fs';
// import SetProtocol from 'setprotocol.js';

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

let provider = new Web3(new HDWalletProvider(PRIVATE_KEY, INFURA_URL_HTTPS));

// let provider = new ethers.providers.JsonRpcProvider(INFURA_URL_HTTPS);
// let wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// let provider = new Web3(new Web3.providers.WebsocketProvider(INFURA_URL_WS));
// provider.eth.accounts.wallet.create();
// provider.eth.accounts.wallet.add(PRIVATE_KEY);

const setProtocol = new SetProtocol(provider, KOVAN_CONFIG)
// const setProtocol = new SetProtocol(wallet, KOVAN_CONFIG)

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


// VERSION 1
async function createSet() {
  const { units, naturalUnit } = await setProtocol.calculateSetUnitsAsync(
    componentAddresses,
    [new BigNumber(1), new BigNumber(1)],
    [new BigNumber(0.75), new BigNumber(0.25)],
    new BigNumber(100),  // $100 start token price
  );
  const txHash = await setProtocol.createSetAsync(
    componentAddresses,
    units,
    naturalUnit,
    name,
    symbol,
    txOpts,
  );
  console.log(txHash);
  return await setProtocol.getSetAddressFromCreateTxHashAsync(txHash);
};

const setAddress = createSet();
