async function trade(ratio) {
    if (!conf.live) {
        console.log("> Trading disabled.");
        return false;
    }

    await updateAllocation(ratio);

    return true;
}

async function updateAllocation(ratio) {
    let newAllocation = new BigNumber(Math.round(ratio * 100) * (10 ** 16));
    var gasPrices = await fetchGasPrices();
    console.log('Gas price: ', Math.floor((gasPrices.average + gasPrices.fast) / 2));
    try {
        const txHash = await setProtocol.socialTrading.updateAllocationAsync(
        process.env.MANAGER_ADDRESS,
        process.env.TRADING_POOL_ADDRESS,
        newAllocation,
        '0x00',
        {
            from: process.env.FROM_ACCOUNT,
            gas: 2500000,
            gasPrice: Math.floor((gasPrices.average + gasPrices.fast) / 2),
        });
        console.log(`Tx hash: ${txHash}`);
        try {
            const txReceipt = await setProtocol.awaitTransactionMinedAsync(txHash, undefined, 2400000);
            console.log('Transaction mined in block', txReceipt.blockNumber);
            if (txReceipt.status) {
                console.log('Transaction executed.')
                try {
                    let axiosConfig = {
                        method: 'post',
                        url: process.env.SET_API_HOST + '/public/v1/trading_pools/' + setId + '/feed_post',
                        headers: {
                            'X-SET-TRADER-API-KEY': process.env.SET_API_KEY,
                        },
                        data: {
                            transaction_hash: txHash,
                            text: 'Target allocation: ' + Math.round(ratio * 100) + '% ETH. '
                        }
                    };
                    console.log('Rebalancing info posting to: ' + axiosConfig.url);
                    await axios(axiosConfig);
                } catch (error) {
                    console.log('Problems posting rebalancing info: ' + error)
                }
            }
            else {
                console.log('FAILED TRANSACTION! ', txReceipt );
            }
        }
        catch (error) {
            console.log('Transaction is running long or failed: ', error);
        };
    }
    catch (error) {
        console.log('Error occured when transaction was being prepared:', error);
    }
};

async function fetchGasPrices() {
    return  (await fetch('https://api.tokensets.com/v1/gas_estimates')).json();
};
