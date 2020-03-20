### Version 1
import pandas as pd
import numpy as np

from TAcharts.indicators import sma

from is_rebalance import is_rebalance
from portfolio import Portfolio


coins = ['ETH', 'DAI']

p = Portfolio(coins)
p.start_units


# Indices of rebalancing - used first index to test
rebalance = is_rebalance(p.dates, weekday='Saturday', hour=10)
rebalance_indices = np.where(rebalance)[0]


# Load prices for our own testing
prices = pd.read_csv('../data/combined.csv')

sma_slow = sma(prices['ETH'], n=200)
sma_mid = sma(prices['ETH'], n=100)
sma_fast = sma(prices['ETH'], n=50)

# Determine if ETH/BTC is bullish/bearish based on moving average support/resistance
bullish = (sma_fast > sma_mid) & (sma_mid > sma_slow)
bearish = (sma_fast < sma_mid) & (sma_mid < sma_slow)

# Record result at each rebalance period
signals = {}
for i in rebalance_indices:
    if bullish[i]:
        signals[i] = 'bull'
    elif bearish[i]:
        signals[i] = 'bear'
    else:
        signals[i] = 'neutral'

# ------------------------------------------------------------------------------
# this section to figure out how to complete first rebalance
# NOTE: 'bull' = 75% allocated to ETH
signal_0 = list(signals.items())[0]
index, signal = signal_0

# Figure out weighting based on current dollar value
d_vals = p.units * p.hist_prices[index]

weights_current = d_vals / sum(d_vals)
weight_current_eth, weight_current_dai = weights_current

weights_bull = [0.75, 0.25]
weight_bull_eth, weight_bull_dai = weights_bull

trade_weight = (weight_bull_eth - weight_current_eth) / 2
trade_dval = trade_weight * sum(d_vals)


trade_weights = (weights_bull - weights_current) / 2
trade_dvals = trade_weights * sum(d_vals)



delta_per_weight * sum(d_vals)





# ------------------------------------------------------------------------------
