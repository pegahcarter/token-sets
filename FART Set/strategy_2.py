# Version 2
# Improve portfolio class and loop through wiggle_room
import pandas as pd
import numpy as np

from TAcharts.indicators import sma

from is_rebalance import is_rebalance
from portfolio import Portfolio
from signals import signals
from variables import *


class Portfolio:

    INITIAL_CAPITAL = 10000
    SLIPPAGE = 0.006

    def __init__(self, coins):

        amt_each = self.INITIAL_CAPITAL / len(coins)
        units = np.divide(amt_each, start_prices)

        self.units = units
        self.start_units = units.copy()

        self.trade_count = 0


p = Portfolio(coins)


rebalance = is_rebalance(prices['date'], weekday='Saturday', hour=10)
rebalance_signals = signals(prices['ETH'], rebalance, *moving_averages)


for index, signal in rebalance_signals.items():

    # Calculate weighting based on current prices
    current_prices = coin_prices[index]
    dollar_values = p.units * current_prices

    weights_current = dollar_values / sum(dollar_values)
    weights_preferred = allocations[signal]

    # Calculate weight to trade on each side
    trade_weights = (weights_preferred - weights_current) / 2
    is_trade_actionable = sum(abs(trade_weight) > wiggle_room for trade_weight in trade_weights) == len(coins)

    if is_trade_actionable:

        trade_dollar_values = trade_weights * sum(dollar_values)

        trade_units = trade_dollar_values / current_prices
        # apply slippage to side purchased
        # trade_units_after_slippage = [(1 - p.SLIPPAGE) * t else t for t in trade_units]

        # p.units += trade_units_after_slippage
        p.units += trade_units
        p.trade_count += 1


# Compare portfolio start_units ending dollar value vs rebalanced units
# End value of 50/50
sum(p.start_units * end_prices)
# End value of 100% ETH
p.start_units[0]*2 * end_prices[0]
# End value of rebalanced
sum(p.units * end_prices)
