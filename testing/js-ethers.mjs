const ethers = require("ethers");
const YAML = require('yaml');
const fs = require('fs');
const solc = require('solc');

const apiAccessToken = ''
const url = 'https://kovan.infura.io/v3/' + apiAccessToken
const PUBLIC_KEY = "0x4279482C96F6Bb49e2D2deA33Ef3F5F03ca69a5d";
const PRIVATE_KEY =
  "E60EB404AE89C74B0CA87754B315FD15249A2A4B73B13451AD6D334615FEDDCF";

const ABI = JSON.parse(fs.readFileSync('ABI_kovan.json', 'utf8'))
let contractAddress = '0x00c6fc47a63e7e0408a2d7FFc308BDD038088cf3'

// -----------------------------------------------------------------------------
// Basic

// Connect a wallet to Kovan
// let provider = new ethers.providers.InfuraProvider("kovan", apiAccessToken);
let provider = new ethers.providers.JsonRpcProvider(url);

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
