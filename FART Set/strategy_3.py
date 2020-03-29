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

for i in range(0, len(test) - window_len + 1, overlap + 1):
    print(test[i:i+window_len])

# -----------------------------------
# Option 2
overlap = 3
num_windows = 2

window_len = int((len(test) + overlap * (num_windows - 1)) / num_windows)

for i in range(0, len(test) - window_len + 1, overlap + 1):
    print(test[i:i+window_len])


# -----------------------------------
# Option 3
# NOTE: windows might not overlap
window_len = 5
num_windows = 3

overlap = int((window_len * num_windows - len(test)) / (num_windows - 1))

for i in range(0, len(test) - window_len + 1, overlap + 1):
    print(test[i:i+window_len])
