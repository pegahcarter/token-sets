// Fetch recent hourly ETH prices
const ccxt = require('ccxt');
const sma = require('sma');


(async () => {
  const ohlcv = await new ccxt.binance().fetchOHLCV('ETH/USDT', '1h')

  closePrices = ohlcv.map(x => x[4])

  let sma50 = sma(closePrices, 50)
  let sma100 = sma(closePrices, 100)
  let sma200 = sma(closePrices, 200)

  console.log(parseFloat(sma50[sma50.length - 1]));
  console.log(parseFloat(sma100[sma100.length - 1]));
  console.log(parseFloat(sma200[sma200.length - 1]));

})();
