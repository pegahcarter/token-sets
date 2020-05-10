# Add boolean value to rebalance based on day and hour
import pandas as pd
import numpy as np



# NOTE: default day and hour determined from `Determine Rebalance Day and Hour.ipynb`
def is_rebalance(dates):

    _dates = pd.DatetimeIndex(dates)

    # 1. Rebalance once/day
    once_day = list(map(lambda x: x.hour == 1 and x.minute == 0, _dates))
    

    # 2. Rebalance once/week
    once_week = (_dates.day_name() == 'Saturday') & (once_day)


    # 3. Rebalance once/month
    month_set = set(range(1, 13))
    once_month = []

    for hr, week in zip(_dates, once_week):
        if hr.month == 1 and 12 not in month_set:
            month_set = set(range(1, 13))
        
        if (hr.month in month_set) and (week):
            month_set.remove(hr.month)
            once_month.append(True)
        else:
            once_month.append(False)


    # 4. Rebalance once/quarter
    quarter_set = set([1, 4, 7, 10])
    once_quarter = []

    for month in once_month:
        if hr.month == 1 and 10 not in quarter_set:
            quarter_set = set([1, 4, 7, 10])
        
        if (hr.month in quarter_set) and (month):
            quarter_set.remove(hr.month)
            once_quarter.append(True)
        else:
            once_quarter.append(False)


    # 5. Rebalance never!
    once_never = [False for _ in _dates]

    
    # Transpose to later pipeline into DataFrame
    t = np.transpose([once_day, once_week, once_month, once_quarter, once_never])

    return t
