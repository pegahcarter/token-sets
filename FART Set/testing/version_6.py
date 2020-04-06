# Version 6
# Optimize code from pandas DataFrame to dict
import pandas as pd
import numpy as np
from datetime import datetime


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
def simulate(coins, allocation, wiggle_room, df):

    start_prices = [df[0][coin] for coin in coins]
    portfolio = Portfolio(coins, start_prices)

    nonrebalanced_netval = []
    rebalanced_netval = []

    for index, row in enumerate(df):

        current_prices = [df[index][coin] for coin in coins]
        dollar_values = portfolio.units * current_prices
        net_dollar_value = sum(dollar_values)

        # Rebalance if needed to
        if row['rebalance']:
            weights_current = dollar_values / net_dollar_value
            weights_preferred = allocation[row['signal']]

            trade_weights = (weights_preferred - weights_current) / 2
            is_trade_actionable = max(trade_weights) > wiggle_room

            if is_trade_actionable:
                trade_dollar_values = trade_weights * net_dollar_value
                trade_units = trade_dollar_values / current_prices
                trade_units_after_slippage = [
                    (1-portfolio.SLIPPAGE)*t if t > 0 else t for t in trade_units
                ]
                portfolio.units += trade_units

        # Append net_dollar_value
        nonrebalanced_netval.append(sum(current_prices * portfolio.start_units))
        rebalanced_netval.append(net_dollar_value)

    cum_performance = sum(np.subtract(rebalanced_netval, nonrebalanced_netval) / nonrebalanced_netval)

    return cum_performance


# ------------------------------------------------------------------------------

df = pd.read_csv('../backtests/example.csv')
df['date'] = pd.to_datetime(df['date'])
# Convert to list of dicts
df = df.to_dict(orient='records')

# Let's say we want 100 day windows with 50 day overlap
# Well, since we're using hours, let's convert into days and go that way
window_len = 24 * 100
overlap = 24 * 50

dfs = split_df(df, overlap, window_len)


results = []

for allocation in allocation_lst:
    for wiggle_room in wiggle_room_lst:
        result = {
            'wiggle_room': wiggle_room,
            'allocation': '/'.join(str(x) for x in allocation['bull']),
        }

        # Add result for each split dataframe
        for df_split in dfs:
            start = datetime.strftime(df_split[0]['date'], '%Y.%m.%d')
            end = datetime.strftime(df_split[-1]['date'], '%Y.%m.%d')

            performance = simulate(coins, allocation, wiggle_room, df_split)

            result[start + ' - ' + end] = performance

        # Save result to results
        results.append(result)


# Convert dict to dataframe
df_results = pd.DataFrame.from_records(results)
df_results['sum'] = df_results.drop(['wiggle_room', 'allocation'], axis=1).sum(axis=1)


# Save dataframe
df_results.to_csv('../backtests/performance-cumulative.csv', index=False)
