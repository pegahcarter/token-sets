# Quick merge of BTC.csv and ETH.csv
import pandas as pd

eth = pd.read_csv('ETH.csv')
btc = pd.read_csv('BTC.csv')

prices = eth[['date', 'close']].rename({'close': 'ETH'}, axis=1)
prices['BTC'] = btc['close']

prices.to_csv('combined.csv', index=False)
