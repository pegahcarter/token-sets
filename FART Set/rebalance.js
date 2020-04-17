const BigNumber = require('bignumber.js');
const Web3 = require('web3');
const YAML = require('yaml');
const fs = require('fs');
const SetProtocol = require('setprotocol.js').default;
const HDWalletProvider = require('@truffle/hdwallet-provider');
const CoinGecko = require('coingecko-api');
const mathjs = require('mathjs');
const ccxt = require('ccxt');
const sma = require('sma');
const axios = require('axios');

const file = fs.readFileSync('../config.yaml', 'utf8')
const env = YAML.parse(file)

const PUBLIC_KEY = env['addresses']['mainnet']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['mainnet']['PRIVATE_KEY']
const MANAGER_ADDRESS = env['setProtocol']['MANAGER']
const TRADING_POOL_ADDRESS = env['setProtocol']['TRADING_POOL']
const INFURA_URL_HTTPS = env['INFURA']['mainnet']['HTTPS'] + env['INFURA']['ID']
const MAINNET_CONFIG = env['setProtocol']['mainnet']
const wiggleRoom = 0.1
const allocations = {
  'bull': 0.9,
  'neutral': 0.5,
  'bear': 0.1
};

let web3 = new Web3(new HDWalletProvider(PRIVATE_KEY, INFURA_URL_HTTPS));
const setProtocol = new SetProtocol(web3, MAINNET_CONFIG);
const CoinGeckoClient = new CoinGecko();


;(async () => {

  let signal = await getSignal();
  let currentAllocation = await getCurrentAllocation();
  let signalAllocation = allocations[signal];

  // Only trigger a rebalance if the weight difference is large enough
  if (Math.abs(currentAllocation - signalAllocation) > wiggleRoom) {

    let newAllocation = formatAllocation(signalAllocation);
    let gasPrices = await fetchGasPrices();
    let gasPriceUsed = Math.floor((gasPrices.average + gasPrices.fast) / 2);
    let txData = {
      from: PUBLIC_KEY,
      gas: 2500000,
      gasPrice: gasPriceUsed
    }

    const txHash = await setProtocol.socialTrading.updateAllocationAsync(
      MANAGER_ADDRESS,
      TRADING_POOL_ADDRESS,
      newAllocation,
      '0x00',
      txData
    );

    const txReceipt = await setProtocol.awaitTransactionMinedAsync(txHash, undefined, 2400000);

    if (txReceipt.status) {
      console.log('Transaction accepted.');

      let axiosConfig = {
        method: 'post',
        url: 'https://api.tokensets.com/public/v1/trading_pools/fart-1/feed_post',
        headers: {
          'X-SET-TRADER-API-KEY': SET_API_KEY,
        },
        data: {
          transaction_hash: txHash,
          text: `Signal: "${signal}".  Adjusting ETH allocation to ${(signalAllocation*100).toFixed(0)}%.`
        }
      }
      // Post rebalance to Token Sets Feed
      await axios(axiosConfig);
    }

    return true;
  } else {
    console.log('No rebalance needed');
    return false;
  }
})()



async function getCurrentAllocation() {

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

  let [ethWeight, cdaiWeight] = mathjs.divide(componentValues, mathjs.sum(componentValues));

  return ethWeight;
};


async function getSignal() {

  const ohlcv = await new ccxt.binance().fetchOHLCV('ETH/USDT', '1h')

  closePrices = ohlcv.map(x => x[4])
  let sma50 = sma(closePrices, 50)
  let sma100 = sma(closePrices, 100)
  let sma200 = sma(closePrices, 200)

  let current50 = parseFloat(sma50[sma50.length - 1])
  let current100 = parseFloat(sma100[sma100.length - 1])
  let current200 = parseFloat(sma200[sma200.length - 1])

  if (current50 > current100 && current100 > current200) {
    signal = 'bull'
  } else if (current50 < current100 && current100 < current200) {
    signal = 'bear'
  } else {
    signal = 'neutral'
  }

  return signal;
};


const formatAllocation = (allocation) => {
  allocationBigNumber = new BigNumber(allocation)
  const allocationInWei = web3.utils.toWei(allocationBigNumber.toString(), 'ether');
  return new BigNumber(allocationInWei);
};


async function fetchGasPrices() {
    return  (await fetch('https://api.tokensets.com/v1/gas_estimates')).json();
};
