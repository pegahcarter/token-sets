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

for i in range(0, len(test) - window_len, overlap - 1):
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
# NOTE: windows might not overlap - raise an Exception
num_windows = 3
window_len = 5

overlap = int((window_len * num_windows - len(test)) / (num_windows - 1))

for i in range(0, len(test) - window_len + 1, overlap + 1):
    print(test[i:i+window_len])




# ------------------------------------------------------------------------------
# First function to wrap all three options

def foo(myList, overlap=None, num_windows=None, window_len=None):

    if [overlap, num_windows, window_len].count(None) > 1:
        raise Exception('Must enter two keyword arguments')

    if overlap is None:
        overlap = int((window_len * num_windows - len(myList)) / (num_windows - 1))
        if overlap < 0:
            raise Exception('Error: no overlap in prices')

    if window_len is None:
        window_len = int((len(myList) + overlap * (num_windows - 1)) / num_windows)

    for x in range(0, len(myList) - window_len, overlap - 1):
        print(myList[x:x+window_len])


foo(test, overlap=3, window_len=5)

foo(test, num_windows=3, window_len=5)







def foo(myList, **kwargs):
    #
    # if len(set(['overlap', 'num_windows', 'window_len']) - set(kwargs)) > 1:
    #     raise Exception('Enter at least two of the following keyword arguments: overlap, num_windows', 'window_len')
    #
    # if 'window_len' not in kwargs:
    #     kwargs['window_len'] = int((len(myList) + kwargs['overlap'] * (kwargs['num_windows'] - 1)))
    # elif 'overlap' not in kwargs:
    #     kwargs['overlap']
