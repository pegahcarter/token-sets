# Common variables used
import numpy as np

# Coins traded
coins = ['ETH', 'DAI']

# Moving average intervals used
moving_averages = [50, 100, 200]

# Potential ETH to DAI allocations from bullish signals
bull_allocation = [
    [0.90, 0.10],
    [0.85, 0.15],
    [0.80, 0.20],
    [0.75, 0.25],
    [0.70, 0.30],
    [0.65, 0.35],
    [0.60, 0.40]
]

# List of allocations used, with the inverse allocation for bearish signals
allocation_lst = [{'bull': b,
                   'neutral': [0.50, 0.50],
                   'bear': b[::-1]}
                  for b in bull_allocation]


# Minimum difference in weighting needed to rebalance without a new signal
# This prevents unnecessary rebalancing
wiggle_room_lst = np.arange(0, 0.16, 0.01)
