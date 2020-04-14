const Web3 = require('web3');
const YAML = require('yaml');
const fs = require('fs');
const HDWalletProvider = require('@truffle/hdwallet-provider');
const abi = require('human-standard-token-abi');

const file = fs.readFileSync('./config.yaml', 'utf8')
const env = YAML.parse(file)

const PUBLIC_KEY = env['addresses']['demo']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['demo']['PRIVATE_KEY']
const INFURA_URL_HTTPS = env['INFURA']['kovan']['HTTPS'] + env['INFURA']['ID']
const INFURA_URL_WS = env['INFURA']['kovan']['WS'] + env['INFURA']['ID']
const KOVAN_CONFIG = env['configSetProtocol']['kovan']['config']
// -----------------------------------------------------------------------------
// Basic

let web3 = new Web3(new HDWalletProvider(PRIVATE_KEY, INFURA_URL_HTTPS));

// Return information on an ERC20
let erc20Address = '0x1d82471142f0aeeec9fc375fc975629056c26cee'
let contract = new web3.eth.Contract(abi, erc20Address);

async function foo() {
  let tokenName = await contract.methods.name().call();
  let tokenSymbol = await contract.methods.symbol().call({from: PUBLIC_KEY});
  let tokenBalance = await contract.methods.balanceOf(PUBLIC_KEY).call();

  console.log(tokenName);
  console.log(tokenSymbol);
  console.log(tokenBalance.toString(10));
};

foo();
