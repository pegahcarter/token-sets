## Introduction

Welcome to [Fart Set](https://set-beta.tokensets.com/set/fart-1)!

FART is built to capture the majority of ETH upside while reducing ETH exposure in times of uncertainty.  Instead of experiencing 100% of price movement (both up and down), at the best of times FART may maintain up to 90% ETH allocation.  At the worst of times, FART may maintain only 10% ETH allocation.  This way, in case of an down/up trend, FART will smartly adjust to lower your risk and shield your portfolio against the (often) wild volatility of Ethereum price discovery.

### Signals
Once per week, FART can adjust ETH weighting based on bullish or bearish signals.  For this trading algorithm, the optimal day and hour for rebalancing can be found [HERE], and the optimal rebalance frequency can be found [HERE].

FART's underlying algorithm is straightfoward and utilizes three hourly moving averages- the 50-hour, 100-hour, and 200-hour.
- Bullish: 50 > 100 > 200
- Bearish: 50 < 100 < 200

Examples for how this bullish/bearish stance works can be found [HERE].

### Weighting
What is not allocated in ETH is allocated in the interest-bearing stablecoin cDAI.

Neutrally, FART will remain with a 50% ETH / 50% cDAI weighting.  In a week of a bullish signal, FART will re-allocate to 90% ETH / 10% cDAI.  For bearish, 10% ETH / 90% cDAI.

The backtests I've written to determine optimal portfolio weighting can be found [HERE].

### Performance

| Average Volatility % over 30 days |            |
| --------------------------------- | ---------- |
| 100% ETH                          | 62.83%     |
| FART                              | 24.82%     |
| **Change**                        | **-60.5%** |

| Absolute Max Drawdown % over 6 months |            |
| ------------------------------------- | ---------- |
| 100% ETH                              | 84.68%     |
| FART                                  | 48.77%     |
| **Change**                            | **-42.4%** |

| Average Max Drawdown % over 6 months |            |
| ------------------------------------ | ---------- |
| 100% ETH                             | 64.06%     |
| FART                                 | 34.47%     |
| **Change**                           | **-46.2%** |


### [Want to add FART to your portfolio?](https://tokensets.com/set/fart-1)

#### Additional Resources:

- [Backtests based on one timeframe can be misleading](https://github.com/carlfarterson/notebooks/blob/master/2.%20Backtests%20Can%20Be%20Misleading.ipynb)
- [Python tools for your own technical analysis](https://pypi.org/project/TAcharts/)
