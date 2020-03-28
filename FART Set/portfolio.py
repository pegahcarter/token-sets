import pandas as pd
import numpy as np



class Portfolio:

    INITIAL_CAPITAL = 10000
    SLIPPAGE = 0.008

    def __init__(self, coins):

        self.coins = coins
        hist_prices = pd.read_csv('../data/prices.csv', usecols=['date'] + coins)
        self.dates = hist_prices.pop('date')
        self.hist_prices = hist_prices.values
        prices = self.hist_prices[0]
        amt_each = self.INITIAL_CAPITAL / len(coins)
        units = np.divide(amt_each, prices)

        self.start_prices = prices
        self.start_units = units.copy()
        self.units = units

        self.trade_count = 0
