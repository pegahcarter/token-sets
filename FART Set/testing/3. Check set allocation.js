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

const PUBLIC_KEY = env['addresses']['mainnet']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['mainnet']['PRIVATE_KEY']
const MANAGER_ADDRESS = env['setProtocol']['MANAGER']
const TRADING_POOL_ADDRESS = env['setProtocol']['TRADING_POOL']
const INFURA_URL_HTTPS = env['INFURA']['mainnet']['HTTPS'] + env['INFURA']['ID']
const MAINNET_CONFIG = env['setProtocol']['mainnet']

let web3 = new Web3(new HDWalletProvider(PRIVATE_KEY, INFURA_URL_HTTPS));
const setProtocol = new SetProtocol(web3, MAINNET_CONFIG)

const CoinGeckoClient = new CoinGecko();

;(async () => {

  let baseSetAddress = await setProtocol.setToken.getComponentsAsync(TRADING_POOL_ADDRESS);
  let setDetails = await setProtocol.setToken.getDetailsAsync(baseSetAddress[0]);

  let componentAddresses = setDetails['components'].map(x => x['address'])
  let componentUnits = setDetails['components'].map(x => x['unit'].toNumber());

  let componentPricesResponse = await CoinGeckoClient.simple.fetchTokenPrice({
    contract_addresses: componentAddresses,
    vs_currencies: 'usd'
  });
  let componentPrices = Object.values(componentPricesResponse['data']).map(x => x['usd']);

  // Update USDC with units
  let componentValues = [componentPrices[0], componentPrices[1] * componentUnits[1]/1000];

  let [ethWeight, cdaiWeight] = mathjs.divide(componentValues, mathjs.sum(componentValues))

})()
