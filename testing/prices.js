// Fetch recent hourly ETH prices
const ccxt = require('ccxt');
const sma = require('sma');


(async () => {
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

})();
