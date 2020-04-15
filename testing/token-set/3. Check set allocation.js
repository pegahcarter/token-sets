const BigNumber = require('bignumber.js');
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
const KOVAN_CONFIG = env['configSetProtocol']['kovan']['config']

let web3 = new Web3(new HDWalletProvider(PRIVATE_KEY, INFURA_URL_HTTPS));
const setProtocol = new SetProtocol(web3, KOVAN_CONFIG)

;(async () => {
  let setDetails = await setProtocol.setToken.getDetailsAsync('0x869b8ad1ca9fb33ae0f8f9095574b1439a984891');

  let componentAddresses = setDetails['components'].map(x => x['address'])
  let componentUnits = setDetails['components'].map(x => x['unit'].toNumber());

})()
