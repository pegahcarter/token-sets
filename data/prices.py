# Code to fetch OHLCV data used for backtests
import pandas as pd

from datetime import datetime, timedelta

import ccxt
import time


poloniex = ccxt.poloniex()
start_date = datetime(year=2017, month=8, day=1, hour=0)
ticker = 'ETH/BTC'

# Master list used to store all OHLCV data
df = []


# Run until March 1, 2019
while start_date < datetime(year=2020, month=3, day=1, hour=0):

    # Fetch 500 hours of OHLCV data
    data = poloniex.fetch_ohlcv(
        ticker,
        '30m',
        limit=500,
        since=int(time.mktime(start_date.timetuple())*1000)
    )

    # Add results to master list
    df.extend(data)

    # Determine the last hour of OHLCV data pulled
    last_hour_pulled = datetime.fromtimestamp(data[-1][0]/1000)

    # Increment last hour pulled by an hour for our next set of 500 hourly OHLCV data
    # start_date = last_hour_pulled + timedelta(hours=1)
    start_date = last_hour_pulled + timedelta(minutes=30)

    # Pause to prevent reaching an API limit
    time.sleep(.1)


# Convert master list to pandas DataFrame
df = pd.DataFrame(df, columns=['date', 'open', 'high', 'low', 'close', 'volume'])

# Modify `date` datatype from millisecond timestamp to datetime object
df['date'] = df['date'].apply(lambda x: datetime.fromtimestamp(x/1000))

# Remove any OHLCV data after Feb 29, 2020 that may have been pulled in the last
#   batch of 500 hours
df = df[df['date'] < datetime(year=2020, month=3, day=1, hour=0)]

# Save DataFrame to CSV
df.to_csv('ethbtc.csv', index=False)
