# Code to create signals
import pandas as pd
import numpy as np
import itertools

from TAcharts.indicators import sma
from TAcharts.utils import apply_across

from is_rebalance import is_rebalance


def signals(src, rebalance, n_fast, n_mid, n_slow):

    ma_fast = sma(src, n=n_fast)
    ma_mid = sma(src, n=n_mid)
    ma_slow = sma(src, n=n_slow)

    bull = (ma_fast > ma_mid) & (ma_mid > ma_slow)
    bear = (ma_fast < ma_mid) & (ma_mid < ma_slow)

    rebalance_indices = np.flatnonzero(rebalance)
    bull_indices = np.flatnonzero(apply_across(rebalance, bull, fn='min'))
    bear_indices = np.flatnonzero(apply_across(rebalance, bear, fn='min'))

    _signals = dict(zip(rebalance_indices, itertools.repeat('neutral')))

    _signals.update(zip(bull_indices, itertools.repeat('bull')))
    _signals.update(zip(bear_indices, itertools.repeat('bear')))

    return pd.Series(_signals)



if __name__ == '__main__':

    df = pd.read_csv('../../data/ETH-USDT.csv', usecols=['date', 'open']).rename({'open': 'ETH'}, axis=1)
    df['USD'] = 1
    df['rebalance_daily'] = is_rebalance(df['date'], day=None, hour=10)
    df['rebalance_weekly'] = is_rebalance(df['date'], day='Saturday', hour=10)

    df['signal'] = signals(df['ETH'], df['rebalance_daily'], 50, 100, 200)
    df.to_csv('../backtests/signals.csv', index=False)
