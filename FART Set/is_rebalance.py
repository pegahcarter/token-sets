# Add boolean value to rebalance based on weekday and hour
import pandas as pd


def is_rebalance(dates, weekday='Saturday', hour=10):

    is_weekday = pd.DatetimeIndex(dates).day_name() == weekday
    is_hour = pd.to_datetime(dates).apply(lambda x: x.hour == hour and x.minute == 0)

    return is_weekday & is_hour
