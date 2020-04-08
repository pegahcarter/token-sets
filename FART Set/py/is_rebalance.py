# Add boolean value to rebalance based on day and hour
import pandas as pd


# NOTE: default day and hour determined from `Determine Rebalance Day and Hour.ipynb`
def is_rebalance(dates, day='Saturday', hour=10):

    is_day = pd.DatetimeIndex(dates).day_name() == day
    is_hour = pd.to_datetime(dates).apply(lambda x: x.hour == hour and x.minute == 0)

    return is_day & is_hour
