# Code to create signals
import pandas as pd
import numpy as np
from is_rebalance import is_rebalance


def signals(dates, prices, n_1=50, n_2=100, n_3=200):

    m1 = prices.rolling(n_1).mean().fillna(0)
    m2 = prices.rolling(n_2).mean().fillna(0)
    m3 = prices.rolling(n_3).mean().fillna(0)

    bullish = (m1 > m2) & (m2 > m3)
    bearish = (m1 < m2) & (m2 < m3)

    _is_rebalance = is_rebalance(dates)
    data = np.insert(_is_rebalance, 0, [bullish, bearish], axis=1)
    
    _signals = pd.DataFrame(
        index=dates,
        data=data,
        columns=['Bullish', 'Bearish', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Never']
    )

    _signals.to_csv('/home/carter/Documents/token-sets/FART/backtests/signals.csv')

    return
