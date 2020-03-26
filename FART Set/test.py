# Testing out weighting
import pandas as pd
import numpy as np

from TAcharts.indicators import sma, rolling, rsi
from TAcharts.utils import apply_across
from TAcharts.wrappers import pd_series_to_np_array

from signals import signals
from is_rebalance import is_rebalance


prices = pd.read_csv('../data/ETH-USDT.csv', usecols=['date', 'close']).rename({'close': 'ETH'}, axis=1)

# Indices of rebalancing - used first index to test
rebalance = is_rebalance(prices['date'], weekday='Saturday', hour=10)
rebalance_indices = np.flatnonzero(rebalance)


ma_50 = sma(prices['ETH'], n=50)
ma_100 = sma(prices['ETH'], n=100)
ma_200 = sma(prices['ETH'], n=200)

bullish = (ma_50 > ma_100) & (ma_100 > ma_200)
# bullish_2 = rsi(prices['ETH'], n=14) > 50
bearish = (ma_50 < ma_100) & (ma_100 < ma_200)

# bull_trades = signals(rebalance, bullish)
# bear_trades = signals(rebalance, bearish)

# Bullish signals
%timeit bull_indices = np.flatnonzero(apply_across(rebalance, bullish, fn='min'))

bear_indices = np.flatnonzero(apply_across(rebalance, bearish, fn='min'))






len(bullish)







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
