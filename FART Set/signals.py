# Code to create signals
from TAcharts.indicators import ema, sma
from TAcharts.utils import crossover

import numpy as np
import pandas as pd

from datetime import datetime

# Load data
ethbtc = pd.read_csv('../data/ethbtc.csv')

close = ethbtc['close'].values

# Create moving averages
ema_slow = ema(close, n=50)
ma_mid = sma(close, n=25)
ema_fast = ema(close, n=10)
ma_base = sma(close, n=200)

df_signals = {}

for i in crossover(ema_fast, ma_mid):
    signal = None

    # Possible long
    if close[i] > ma_base[i]:
        if ema_slow[i] > ma_base[i] \
        and ma_mid[i] > ema_slow[i] \
        and ema_fast[i] > ma_mid[i]:
            signal = 'long'
    # Possible short
    else:    # close[i] < ma_base[i]
        if ema_slow[i] < ma_base[i] \
        and ma_mid[i] < ema_slow[i] \
        and ema_fast[i] < ma_mid[i]:
            signal = 'short'

    if signal:
        df_signals[i] = signal
