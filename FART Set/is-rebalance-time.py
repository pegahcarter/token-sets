# Add boolean value to rebalance based on day with least volatility (Saturday) at 10:00 UTC (for now)

import pandas as pd

ethbtc = pd.read_csv('../data/ethbtc.csv')

ethbtc['Saturday'] = pd.DatetimeIndex(ethbtc['date']).day_name() == 'Saturday'
ethbtc['10 UTC'] = pd.to_datetime(ethbtc['date']).apply(lambda x: x.hour == 10 and x.minute == 0)
ethbtc['Rebalance'] = ethbtc['Saturday'] & ethbtc['10 UTC']

ethbtc['Rebalance'].value_counts()

ethbtc.to_csv('../data/ethbtc_extra_cols.csv', index=False)
