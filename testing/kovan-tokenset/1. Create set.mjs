// https://docs.setprotocol.com/#/tutorials#getting-testnet-erc20-tokens
// import BigNumber from 'bignumber.js';
// import ethers from "ethers";
// import YAML from 'yaml';
// import fs from 'fs';
// import SetProtocol from 'setprotocol.js';

const BigNumber = require('bignumber.js');
const ethers = require("ethers");
const YAML = require('yaml');
const fs = require('fs');
const SetProtocol = require('setprotocol.js').default;


const file = fs.readFileSync('../config.yaml', 'utf8')
const env = YAML.parse(file)


const PUBLIC_KEY = env['addresses']['demo']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['demo']['PRIVATE_KEY']
const INFURA_URL = env['INFURA']['kovan']['HTTPS'] + env['INFURA']['ID']
const KOVAN_CONFIG = env['configSetProtocol']['kovan']['config']

let provider = new ethers.providers.JsonRpcProvider(INFURA_URL);
let wallet = new ethers.Wallet(PRIVATE_KEY, provider);

const setProtocol = new SetProtocol(wallet, KOVAN_CONFIG)


async function createStableSet() {
  const addressTrueUSD = '0xadb015d61f4beb2a712d237d9d4c5b75bafefd7b';
  const addressDAI = '0x1d82471142F0aeEEc9FC375fC975629056c26ceE'
  const componentAddresses = [addressTrueUSD, addressDAI]

  const { units, naturalUnit } = await setProtocol.calculateSetUnitsAsync(
    componentAddresses,
    [new BigNumber(1), new BigNumber(1)],
    [new BigNumber(0.5), new BigNumber(0.5)],
    new BigNumber(1),
  );
  const name = 'Fart Set';
  const symbol = 'FART';
  const txOpts = {
    from: PUBLIC_KEY,
    gas: 4000000,
    gasPrice: 8000000000,
  };

  const txHash = await setProtocol.createSetAsync(
    componentAddresses,
    units,
    naturalUnit,
    name,
    symbol,
    txOpts,
  );
  const address = await setProtocol.getSetAddressFromCreateTxHashAsync(txHash);
  return address
};



// setProtocol.calculateSetUnitsAsync(
//   componentAddresses,
//   [new BigNumber(1), new BigNumber(1)],     // trueUSD and Dai are each $1
//   [new BigNumber(0.5), new BigNumber(0.5)], // Each coin has a 50% allocation
//   new BigNumber(1)                          // StableSet will have a 1 target price
// ).then((resolve) => {
//   let {units, naturalUnit} = resolve;
//   const name = 'Fart Set';
//   const symbol = 'FART';
//   const txOpts = {
//     from: PUBLIC_KEY,
//     gas: 4000000,
//     gasPrice: 8000000000,
//   }
// });
