# Version 4
# Saving results to dataframe
import pandas as pd
import numpy as np
from datetime import datetime

coins = ['ETH', 'DAI']
allocations = {
    'bull': [0.75, 0.25],
    'neutral': [0.50, 0.50],
    'bear': [0.25, 0.75]
}
wiggle_room = 0.05



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


# Split dataframe into chunks
def split_df(array, overlap, window_len):

    array_split = []

    for x in range(0, len(array) - window_len + 1, overlap - 1):
        array_split.append(array[x:x+window_len])

    return array_split


# Simulate function
def simulate(coins, allocations, df):

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


df = pd.read_csv('../backtests/example.csv')
df['date'] = pd.to_datetime(df['date'])


# Let's say we want 100 day windows with 50 day overlap
# Well, since we're using hours, let's convert into days and go that way
window_len = 24 * 100
overlap = 24 * 50

dfs = split_df(df, overlap, window_len)

df_0 = dfs[0]



type(df_0['date'].iat[0])

datetime.strftime(df_0['date'].iat[0])


p = simulate(coins, allocations, dfs[0])



bull_allocations = [
    [0.90, 0.10],
    [0.85, 0.15],
    [0.80, 0.20],
    [0.75, 0.25],
    [0.70, 0.30],
    [0.65, 0.35],
    [0.60, 0.40]
]
allocations_lst = [{'bull': b,
                   'neutral': [0.50, 0.50],
                   'bear': b[::-1]}
                  for b in bull_allocations]


print(p)
