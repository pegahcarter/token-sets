import pandas as pd
import matplotlib.pyplot as plt

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
# df_performance = pd.read_csv('backtests/performance.csv')
# num_windows = len(df_performance.columns) - 1


df_signals = pd.read_csv('backtests/signals.csv').to_dict(orient='records')


fig = plt.figure(figsize=(20, 20))

# df = split_df(df_signals, overlap, window_len)[0]
for i, df in enumerate(split_df(df_signals, overlap, window_len)):

    rebalanced, eth, _ = simulate(assets, allocation, wiggle_room, df)

    results = pd.DataFrame({'Rebalanced Net Value': rebalanced, 'ETH Net Value': eth})

    ax = fig.add_subplot(5, 3, i+1)
    ax.plot(results)

    ax.set_title(f"{df[0]['date'][:df[0]['date'].find(' ')]} - {df[-1]['date'][:df[-1]['date'].find(' ')]}")
    ax.set_xticks([])

plt.show()
