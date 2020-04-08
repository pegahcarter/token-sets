import numpy as np
import pandas as pd
from datetime import datetime

from is_rebalance import is_rebalance
from signals import signals
from split_df import split_df
from simulate import simulate

# ------------------------------------------------------------------------------
# VARIABLES

# We want 150 day windows with 100 day overlap
# Since our dataframe is in hours, multiply by 24
window_len = 24 * 150
overlap = 24 * 100

# Assets traded
assets = ['ETH', 'USD']

# Moving average intervals used
moving_averages = [50, 100, 200]

# Potential ETH to DAI allocations from bullish signals
bull_allocation = [
    [0.85, 0.15],
    [0.80, 0.20],
    [0.75, 0.25],
    [0.70, 0.30],
    [0.65, 0.35]
]

# List of allocations used, with the inverse allocation for bearish signals
allocation_lst = [{'bull': b,
                   'neutral': [0.50, 0.50],
                   'bear': b[::-1]}
                  for b in bull_allocation]


# Minimum difference in weighting needed to rebalance without a new signal
# This prevents unnecessary rebalancing
wiggle_room_lst = np.arange(0, 0.21, 0.02)

# ------------------------------------------------------------------------------


def main():

    df = pd.read_csv('../data/ETH-USDT.csv', usecols=['date', 'close']).rename({'close':'ETH'}, axis=1)
    df['date'] = pd.to_datetime(df['date'])
    df['USD'] = 1

    df['rebalance'] = is_rebalance(df['date'])
    df['signal'] = signals(df['ETH'], df['rebalance'], *moving_averages)

    df.to_csv('../backtests/signals.csv', index=False)

    df = df.to_dict(orient='records')
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

                _, _, performance = simulate(assets, allocation, wiggle_room, df_split)

                result[start + ' - ' + end] = performance

            # Save result to results
            results.append(result)


    # Convert dict to dataframe
    df_results = pd.DataFrame.from_records(results)
    df_results['sum'] = df_results.drop(['wiggle_room', 'allocation'], axis=1).sum(axis=1)

    # Save dataframe
    df_results.sort_values('sum', ascending=False).to_csv('../backtests/performance.csv', index=False)


if __name__ == '__main__':
    main()
