const ethers = require("ethers");
const YAML = require('yaml');
const fs = require('fs');
const solc = require('solc');

const file = fs.readFileSync('./config.yaml', 'utf8')
const env = YAML.parse(file)

const PUBLIC_KEY = env['addresses']['demo']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['demo']['PRIVATE_KEY']

const INFURA_URL = env['INFURA']['kovan']['HTTPS'] + env['INFURA']['ID']

const ABI = JSON.parse(fs.readFileSync('ABI_kovan.json', 'utf8'))
let contractAddress = '0x00c6fc47a63e7e0408a2d7FFc308BDD038088cf3'

// -----------------------------------------------------------------------------
// Basic

// Connect a wallet to Kovan
// let provider = new ethers.providers.InfuraProvider("kovan", env['INFURA']['ID']);
let provider = new ethers.providers.JsonRpcProvider(INFURA_URL);

let wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Return ETH balance of address
// provider.getBalance(PUBLIC_KEY).then(balance => {
//   let etherString = ethers.utils.formatEther(balance);
//   console.log(etherString);
// });

// -----------------------------------------------------------------------------
// Transactions

// Send a transaction
let transaction = {
    to: '0xDA0dD08e37958F5D78c59De7fD05C66461E2b908',
    // nonce: 0,
    gasLimit: 21000,
    gasPrice: 5 * 10**9,
    // data: "0x",
    value: ethers.utils.parseEther('0.05')
    // chainId: 3
};

// let sendTransactionPromise = wallet.sendTransaction(transaction);
//
// sendTransactionPromise.then((tx) => {
//   console.log(tx);
// });

// -----------------------------------------------------------------------------
// Contracts

// Get contract code
// let codePromise =  provider.getCode(contractAddress);

// codePromise.then((results) => {
//   console.log(results);
// });

// Connect to a contract
let contract = new ethers.Contract(contractAddress, ABI, provider);

let contractPromise = contract.owner();

contractPromise.then((results) => {
  console.log(results);
});
