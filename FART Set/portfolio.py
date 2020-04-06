import numpy as np


class Portfolio:

    INITIAL_CAPITAL = 10000
    SLIPPAGE = 0.006

    def __init__(self, assets, start_prices):

        amt_each = self.INITIAL_CAPITAL / len(assets)
        units = np.divide(amt_each, start_prices)

        self.start_prices = start_prices
        self.units = units
        self.start_units = units.copy()

        self.trade_count = 0
