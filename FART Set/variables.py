# Common variables used
import pandas as pd

coins = ['ETH', 'DAI']

prices = pd.read_csv('../data/ETH-USDT.csv', usecols=['date', 'open']).rename({'open': 'ETH'}, axis=1)
prices['DAI'] = 1

coin_prices = prices[coins].values
start_prices = coin_prices[0]
end_prices = coin_prices[-1]

allocations = {
    'bull': [0.75, 0.25],
    'neutral': [0.50, 0.50],
    'bear': [0.25, 0.75]
}

wiggle_room = 0.05

moving_averages = [50, 100, 200]
