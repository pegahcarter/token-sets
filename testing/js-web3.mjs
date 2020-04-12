import fs from 'fs';
import YAML from 'yaml';
import * as Web3 from 'web3';
import SetProtocol from 'setprotocol.js';


const file = fs.readFileSync('./config.yaml', 'utf8')
var env = YAML.parse(file)


const provider = new Web3(new Web3.providers.WebsocketProvider(env['INFURA']['WS']));


// Add testing address
// web3.eth.accounts.privateKeyToAccount(env['addresses']['demo']['PRIVATE_KEY'])


// var ENS_abi = JSON.parse(fs.readFileSync('ABI.json', 'utf8'))
// var contract = new web3.eth.Contract(ENS_abi, '0xfac7bea255a6990f749363002136af6556b31e04')

const config = {
  coreAddress: '0xf55186CC537E7067EA616F2aaE007b4427a120C8',
  exchangeIssuanceModuleAddress: '0x73dF03B5436C84Cf9d5A758fb756928DCEAf19d7',
  kyberNetworkWrapperAddress: '0x9B3Eb3B22DC2C29e878d7766276a86A8395fB56d',
  protocolViewerAddress: '0x589d4b4d311EFaAc93f0032238BecD6f4D397b0f',
  rebalanceAuctionModuleAddress: '0xe23FB31dD2edacEbF7d92720358bB92445F47fDB',
  rebalancingSetExchangeIssuanceModule: '0xd4240987D6F92B06c8B5068B1E4006A97c47392b',
  rebalancingSetIssuanceModule: '0xcEDA8318522D348f1d1aca48B24629b8FbF09020',
  rebalancingSetTokenFactoryAddress: '0x15518Cdd49d83471e9f85cdCFBD72c8e2a78dDE2',
  setTokenFactoryAddress: '0xE1Cd722575801fE92EEef2CA23396557F7E3B967',
  transferProxyAddress: '0x882d80D3a191859d64477eb78Cca46599307ec1C',
  vaultAddress: '0x5B67871C3a857dE81A1ca0f9F7945e5670D986Dc',
  wrappedEtherAddress: '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
};


var setProtocol = new SetProtocol(web3.currentProvider, config)
