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


const createSet = async function() {
  const { units, naturalUnit } = await setProtocol.calculateSetUnitsAsync(
    componentAddresses,
    [new BigNumber(1), new BigNumber(1)],
    [new BigNumber(0.75), new BigNumber(0.25)],
    new BigNumber(50),  // $50 start token price
  );
  const txHash = await setProtocol.createSetAsync(
    componentAddresses,
    units,
    naturalUnit,
    name,
    symbol,
    txOpts,
  );
  return await setProtocol.getSetAddressFromCreateTxHashAsync(txHash);
};


const approveTokensForTransfer = (tokenAddresses) => {
  tokenAddresses.forEach(async function(address) {
    await setProtocol.setUnlimitedTransferProxyAllowanceAsync(
      address, { gas: 4000000, gasPrice: 6000000000 },
    );
  });
};


const issueSet = async function(setAddress) {
  // Issue 1x Set which equals 50 * 10 ** 18 base units.
  const issueQuantity = new BigNumber(10 ** 18);

  // Check that our issue quantity is divisible by the natural unit.
  const isMultipleOfNaturalUnit = await setProtocol.setToken.isMultipleOfNaturalUnitAsync(setAddress, issueQuantity);

  if (isMultipleOfNaturalUnit) {
    try {
      return await setProtocol.issueAsync(
        setAddress,
        issueQuantity,
        txOpts,
      );
    } catch (err) {
      throw new Error(`Error when issuing a new Set token: ${err}`);
    }
  }
  throw new Error(`Issue quantity is not multiple of natural unit. Confirm that your issue quantity is divisible by the natural unit.`);
};



createSet().then((setAddress) => {
  console.log(setAddress); // 0x869b8ad1ca9fb33ae0f8f9095574b1439a984891
  // Approve all component tokens for transfer to Set Protocol contracts
  approveTokensForTransfer(componentAddresses);
  // Issue one unit of our Set
  issueSet(setAddress).then(console.log);  /// 0x67af8476c231d30a80e200a48e9138703477581555cc0edc1719eae96cc4e30e
});
