### Version 1
import pandas as pd
import numpy as np

from TAcharts.indicators import sma

from is_rebalance import is_rebalance
from portfolio import Portfolio


coins = ['ETH', 'DAI']
wiggle_room = 0.05
allocations = {
    'bull': [0.75, 0.25],
    'neutral': [0.50, 0.50],
    'bear': [0.25, 0.75]
}


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

signals = {}
trade_count = 0

for index in rebalance_indices:

    # Determine signal
    if bullish[index]:
        signal = 'bull'
    elif bearish[index]:
        signal = 'bear'
    else:
        signal = 'neutral'
    signals[index] = signal

    # Calculate weighting based on current prices
    current_prices = p.hist_prices[index]
    dollar_values = p.units * current_prices

    weights_current = dollar_values / sum(dollar_values)
    weights_preferred = allocations[signal]

    # Calculate weight to trade on each side
    trade_weights = (weights_preferred - weights_current) / 2
    is_trade_actionable = sum(abs(trade_weight) > wiggle_room for trade_weight in trade_weights) == len(coins)

    if is_trade_actionable:

        trade_dollar_values = trade_weights * sum(dollar_values)

        trade_units = trade_dollar_values / current_prices
        # NOTE: Divide slippage by two to account for 50% slippage on each side
        trade_units_after_slippage = (1 - p.SLIPPAGE / 2) * trade_units

        p.units += trade_units_after_slippage
        trade_count += 1


# Compare portfolio start_units ending dollar value vs rebalanced units
end_prices = p.hist_prices[-1]

# End value of 50/50
sum(p.start_units * end_prices)
# End value of 100% ETH
p.start_units[0]*2 * end_prices[0]
# End value of rebalanced
sum(p.units * end_prices)
