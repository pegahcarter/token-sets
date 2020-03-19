### Version 1
import pandas as pd
import numpy as np

from TAcharts.indicators import sma

from is_rebalance import is_rebalance
from portfolio import Portfolio


coins = ['ETH', 'BTC']

p = Portfolio(coins)
p.start_units


# Indices of rebalancing - used first index to test
rebalance = is_rebalance(p.dates, weekday='Saturday', hour=10)
rebalance_indices = np.where(rebalance)[0]
rebalance_index = rebalance_indices[0]


# Load prices for our own testing
prices = pd.read_csv('../data/combined.csv')

slow, fast = 100, 52
n = 14

# prices['TSI_ETH'] = tsi(prices['ETH'], slow=slow, fast=fast)
# prices['TSI_BTC'] = tsi(prices['BTC'], slow=slow, fast=fast)
# prices['RSI_ETH'] = rsi(prices['ETH'], n=n)
# prices['RSI_BTC'] = rsi(prices['BTC'], n=n)
# prices['MACD_ETH'] = macd(prices['ETH'], slow=slow, fast=fast)
# prices['MACD_BTC'] = macd(prices['BTC'], slow=slow, fast=fast)
# prices['MACD_ROC_ETH'] = roc(prices['MACD_ETH'], n=4)
# prices['MACD_ROC_BTC'] = roc(prices['MACD_BTC'], n=4)

prices.iloc[rebalance_indices][:10]
