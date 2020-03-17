# Determine which day is best to rebalance based on lowest volatility
import pandas as pd
import numpy as np
import TAcharts

from datetime import timedelta
from TAcharts.utils import group_candles

ethbtc_30m = pd.read_csv('../data/ethbtc.csv')

ethbtc_1d = group_candles(ethbtc_30m, interval=48)

ethbtc_1d['pct_change'] = (ethbtc_1d['high'] - ethbtc_1d['low']) / ethbtc_1d['open']

ethbtc_1d['weekday'] = pd.DatetimeIndex(ethbtc_1d['date']).day_name()

ethbtc_1d = ethbtc_1d.groupby('weekday')['pct_change'].mean().sort_values(ascending=False)


print(ethbtc_1d)
