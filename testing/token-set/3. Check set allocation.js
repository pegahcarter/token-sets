const BigNumber = require('bignumber.js');
const Web3 = require('web3');
const YAML = require('yaml');
const fs = require('fs');
const SetProtocol = require('setprotocol.js').default;
const HDWalletProvider = require('@truffle/hdwallet-provider');
const CoinGecko = require('coingecko-api');
const mathjs = require('mathjs');

const file = fs.readFileSync('../config.yaml', 'utf8')
const env = YAML.parse(file)

const PUBLIC_KEY = env['addresses']['demo']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['demo']['PRIVATE_KEY']
const INFURA_URL_HTTPS = env['INFURA']['mainnet']['HTTPS'] + env['INFURA']['ID']
const MAINNET_CONFIG = env['configSetProtocol']['mainnet']

let web3 = new Web3(new HDWalletProvider(PRIVATE_KEY, INFURA_URL_HTTPS));
const setProtocol = new SetProtocol(web3, MAINNET_CONFIG)

const CoinGeckoClient = new CoinGecko();

;(async () => {
  // NOTE: this address from the getComponents() function of the Set contract (0xffee21b4bb7084a9416205544101ae9f472c7159)
  let setDetails = await setProtocol.setToken.getDetailsAsync('0xf9958a0d54721d48d75d9fd65af29a1ed406ca4d');

  console.log(setDetails);

  let componentAddresses = setDetails['components'].map(x => x['address'])
  let componentUnits = setDetails['components'].map(x => x['unit'].toNumber());

  // let componentPricesResponse = await CoinGeckoClient.simple.fetchTokenPrice({
  //   contract_addresses: componentAddresses,
  //   vs_currencies: 'usd'
  // });
  //
  // let componentPrices = Object.values(componentPricesResponse['data']).map(x => x['usd']);
  //
  // console.log(componentAddresses);
  // console.log(componentUnits);
  // console.log(componentPrices)

  let test = await setProtocol.setToken.getUnitsAsync('0xf9958a0d54721d48d75d9fd65af29a1ed406ca4d');
  console.log(test);

  // const componentValues = mathjs.multiply(componentUnits, componentPrices)
  // console.log(componentValues);

})()
