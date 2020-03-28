# Testing out weighting
import pandas as pd
import numpy as np
import itertools

from TAcharts.indicators import sma, rolling, rsi
from TAcharts.utils import apply_across
from TAcharts.wrappers import pd_series_to_np_array

from signals import signals
from is_rebalance import is_rebalance


prices = pd.read_csv('../data/ETH-USDT.csv', usecols=['date', 'close']).rename({'close': 'ETH'}, axis=1)

# Indices of rebalancing - used first index to test
rebalance = is_rebalance(prices['date'], weekday='Saturday', hour=10)
rebalance_indices = np.flatnonzero(rebalance)











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
