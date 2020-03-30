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

prices = pd.read_csv('../data/prices.csv')
prices['date'] = pd.to_datetime(prices['date'])

# First function to wrap option 1

def foo(array, overlap, window_len):

    array_split = []

    for x in range(0, len(array) - window_len + 1, overlap - 1):
        array_split.append(array[x:x+window_len])

    return array_split


# Figuring out how to split up prices dataset
day_diff = prices['date'].iat[-1] - prices['date'].iat[0]

# Let's say we want 100 day windows with 50 day overlap
# Well, since we're using hours, let's convert into days and go that way
window_len = 24 * 100
overlap = 24 * 50

test = foo(prices, overlap, window_len)
len(test)





# ------------------------------------------------------------------------------
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
