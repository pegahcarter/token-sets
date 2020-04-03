# Common variables used
import pandas as pd
import numpy as np

coins = ['ETH', 'DAI']

# prices = pd.read_csv('../data/ETH-USDT.csv', usecols=['date', 'open']).rename({'open': 'ETH'}, axis=1)
# prices['DAI'] = 1

# coin_prices = prices[coins].values
# start_prices = coin_prices[0]
# end_prices = coin_prices[-1]


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



allocations = {
    'bull': [0.75, 0.25],
    'neutral': [0.50, 0.50],
    'bear': [0.25, 0.75]
}

wiggle_room = 0.05
wiggle_room_lst = np.arange(0, 0.06, 0.01)

moving_averages = [50, 100, 200]
