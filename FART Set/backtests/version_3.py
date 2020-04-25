# Version 3
# Create multiple timeframes from the same dataset
import pandas as pd
import numpy as np

from TAcharts.indicators import sma
from datetime import datetime, timedelta

from is_rebalance import is_rebalance
from portfolio import Portfolio
from signals import signals
from variables import *


class Portfolio:

    INITIAL_CAPITAL = 10000
    SLIPPAGE = 0.006

    def __init__(self, coins, start_prices):

        amt_each = self.INITIAL_CAPITAL / len(coins)
        units = np.divide(amt_each, start_prices)

        self.start_prices = start_prices
        self.units = units
        self.start_units = units.copy()

        self.trade_count = 0


# First function to wrap option 1
def split_df(array, overlap, window_len):

    array_split = []

    for x in range(0, len(array) - window_len + 1, overlap - 1):
        array_split.append(array[x:x+window_len])

    return array_split


# Simulate function
def simulate(coins, df):

    start_prices = df[coins].iloc[0]
    portfolio = Portfolio(coins, start_prices)

    for index, row in df.dropna().iterrows():

        # Weighting based on current prices
        current_prices = row[coins]
        dollar_values = portfolio.units * current_prices

        weights_current = dollar_values / sum(dollar_values)
        weights_preferred = allocations[row['signal']]

        trade_weights = (weights_preferred - weights_current) / 2
        is_trade_actionable = sum(abs(trade_weight) > wiggle_room for trade_weight in trade_weights) == len(coins)

        if is_trade_actionable:
            trade_dollar_values = trade_weights * sum(dollar_values)
            trade_units = trade_dollar_values / current_prices
            trade_units_after_slippage = [
                (1-portfolio.SLIPPAGE)*t if t > 0 else t for t in trade_units
            ]

            portfolio.units += trade_units
            portfolio.trade_count += 1

    end_prices = df[coins].iloc[-1]

    # End of non-rebalanced portfolio
    end_val_nonrebalanced = sum(portfolio.start_units * end_prices)
    end_val_rebalanced = sum(portfolio.units * end_prices)

    return (end_val_rebalanced - end_val_nonrebalanced) / end_val_nonrebalanced

# ------------------------------------------------------------------------------


df = pd.read_csv('../data/rebalance_signals.csv')
df['date'] = pd.to_datetime(df['date'])

# Figuring out how to split up prices dataset
day_diff = df['date'].iat[-1] - df['date'].iat[0]

# Let's say we want 100 day windows with 50 day overlap
# Well, since we're using hours, let's convert into days and go that way
window_len = 24 * 100
overlap = 24 * 50

dfs = split_df(df, overlap, window_len)

p = simulate(coins, dfs[0])


print(p)


# ------------------------------------------------------------------------------
# NOTE: testing below
# Create rolling window from a list

test = list(range(11))
# -----------------------------------
# Option 1
# NOTE: best option
overlap = 3
window_len = 5

for i in range(0, len(test) - window_len + 1, overlap - 1):
    print(test[i:i+window_len])

# -----------------------------------
# Option 2
overlap = 3
num_windows = 3

window_len = (len(test) + (overlap - 1) * num_windows) // num_windows

for i in range(0, len(test) - window_len + 1, overlap - 1):
    print(test[i:i+window_len])

# -----------------------------------
# Option 3 - TODO:
# NOTE: windows might not overlap - raise an Exception
num_windows = 3
window_len = 5

# TODO: fix the math behind this
overlap = (window_len * num_windows - len(test)) // (num_windows - 1)

for i in range(0, len(test) - window_len, overlap - 1):
    print(test[i:i+window_len])
