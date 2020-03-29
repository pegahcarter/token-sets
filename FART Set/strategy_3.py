# Version 3
# Create multiple timeframes from the same dataset
import pandas as pd
import numpy as np

from TAcharts.indicators import sma

from is_rebalance import is_rebalance
from portfolio import Portfolio
from signals import signals
from variables import *


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

# ------------------------------------------------------------------------------
# First function to wrap option 1

def foo(array, overlap, window_len):

    for x in range(0, len(array) - window_len + 1, overlap - 1):
        print(array[x:x+window_len])


df = prices[:10]

foo(df, overlap=3, window_len=5)
