# Add boolean value to rebalance based on day with least volatility (Saturday) at 10:00 UTC (for now)

import pandas as pd
from TAcharts.utils import group_candles

ethbtc_1h = group_candles(pd.read_csv('../data/ethbtc.csv'), interval=2)

ethbtc_1h['Saturday'] = pd.DatetimeIndex(ethbtc_1h['date']).day_name() == 'Saturday'
ethbtc_1h['10 UTC'] = pd.to_datetime(ethbtc_1h['date']).apply(lambda x: x.hour == 10 and x.minute == 0)
ethbtc_1h['Rebalance'] = ethbtc_1h['Saturday'] & ethbtc_1h['10 UTC']

ethbtc_1h['Rebalance'].value_counts()
