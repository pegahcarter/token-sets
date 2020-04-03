# Common variables used
import pandas as pd
import numpy as np

coins = ['ETH', 'DAI']


bull_allocation = [
    [0.90, 0.10],
    [0.85, 0.15],
    [0.80, 0.20],
    [0.75, 0.25],
    [0.70, 0.30],
    [0.65, 0.35],
    [0.60, 0.40]
]

allocation_lst = [{'bull': b,
                   'neutral': [0.50, 0.50],
                   'bear': b[::-1]}
                  for b in bull_allocations]



allocation = {
    'bull': [0.75, 0.25],
    'neutral': [0.50, 0.50],
    'bear': [0.25, 0.75]
}

wiggle_room_lst = np.arange(0, 0.17, 0.02)

moving_averages = [50, 100, 200]
