# Testing out weighting
import pandas as pd
import numpy as np


from is_rebalance import is_rebalance
from TAcharts.indicators import tsi



coins = ['ETH', 'DAI']

p = Portfolio(coins)
p.start_units

# Load prices for our own testing
prices = pd.read_csv('../data/combined.csv')

rebalance = is_rebalance(prices['date'], weekday='Saturday', hour=10)

# Indices of rebalancing - used first index to test
rebalance_indices = np.where(rebalance)[0]
rebalance_index = rebalance_indices[0]

slow, fast = 25, 13
prices['TSI'] = tsi(prices['ETH'], slow=slow, fast=fast)

prices.iloc[rebalance_indices][:10]
