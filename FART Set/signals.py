# Code to create signals

def signals(src, rebalance_indices, n_fast, n_mid, n_slow):

    ma_fast = sma(src, n=n_fast)
    ma_mid = sma(src, n=n_mid)
    ma_slow = sma(src, n=n_slow)

    bull = (ma_fast > ma_mid) & (ma_mid > ma_slow)
    bear = (ma_fast < ma_mid) & (ma_mid < ma_slow)

    bull_indices = np.flatnonzero(apply_across(rebalance, bull, fn='min'))
    bear_indices = np.flatnonzero(apply_across(rebalance, bear, fn='min'))

    _signals = dict(zip(rebalance_indices, itertools.repeat('neutral')))
    _signals.update(zip(bull_indices, itertools.repeat('bull')))
    _signals.update(zip(bear_indices, itertools.repeat('bear')))

    return _signals
