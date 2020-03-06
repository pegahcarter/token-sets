

class Portfolio:

    coins = ['ETH', 'BTC', 'DAI']
    initial_capital = 100
    trade_count = 0
    slippage = 0

    def __init__(self, *args, **kwargs):
        self.available_capital = self.initial_capital
        self.positions = []


    # Add slippage
    def calc_slippage(self, *args, **kwargs):
        pass

    # Open a position
    def open(self, *args, **kwargs):
        pass

    # Close a position
    def close(self, *args, **kwargs):
        pass
