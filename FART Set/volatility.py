import pandas as pd

from datetime import datetime

from py.split_df import split_df
from py.simulate import simulate
from py.portfolio import Portfolio

# ------------------------------------------------------------------------------
# Variables
assets = ['ETH', 'USD']

# We'll use 180 day windows (6 months) with 120 day overlap (4 months)
# Since our dataframe is in hours, multiply by 24
window_len = 24 * 180
overlap = 24 * 120

allocation = {
    'bull': [0.85, 0.15],
    'neutral': [0.50, 0.50],
    'bear': [0.15, 0.85]
}

wiggle_room = 0.12

# ------------------------------------------------------------------------------
# Analysis
df = pd.read_csv('backtests/signals.csv').to_dict(orient='records')


df_window = split_df(signals, overlap, window_len)[0]
# for df_window in split_df(df, overlap, window_len)

    rebalanced, eth, _ = simulate(assets, allocation, wiggle_room, df_window)


    test = pd.DataFrame({'Rebalanced Net Value': rebalanced, 'ETH Net Value': eth})
