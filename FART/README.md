## Introduction
Welcome to [Fart Set](https://set-beta.tokensets.com/set/fart-1)!

Today, most Token Sets are managed by the Set founder on a non-transparent, almost secretive basis. This forces the Set holder to place their trust in a system they know little or possibly nothing about.

The Fart Set is built on a dynamic algorithm that has been designed to capitalize on market volatility while ensuring safe handling of Set holders assets; it combines consistent rebalancing with honest automation and robust backtesting for a strategy you can trust.

*__FART is built with 100% clarity and transparency.__*

### Signals
FART can adjust weighting based on a bullish or bearish signal once per week.  These signals are:

- bull: 50-hour SMA > 100-hour SMA > 200-hour SMA
- bear: 50-hour SMA < 100-hour SMA < 200-hour SMA

(Note: SMA is the simple moving average based on the hourly close)

FART has a neutral weight of 50% Ethereum and 50% cDAI. Depending on the signal, % of Ethereum in the Set can range between 90% and 10%. ([1](https://github.com/carlfarterson/token-sets/blob/master/FART%20Set/Determining%20Allocation%20and%20Wiggle%20Room.ipynb))

### Description
The goal of FART is to enable strategic exposure to Ethereum in which traders have the opportunity to capture a majority of an up market while providing lower volatility, lower risk and drawdown. ([2](https://github.com/carlfarterson/token-sets/blob/master/FART%20Set/Analysis.ipynb))


| Average Volatility % over 30 days ||
|---| --|
|100% ETH | 62.83% |
|FART | 24.82% |
|**Change** |**-60.5%**|


|Absolute Max Drawdown % over 6 months||
|--|--|
|100% ETH| 84.68%|
|FART| 48.77%|
|**Change**| **-42.4%**|

|Average Max Drawdown % over 6 months||
|--|--|
|100% ETH|  64.06%|
|FART| 34.47%|
|**Change**| **-46.2%**|

An additional objective of FART is to reduce risk of being stuck in an underperforming position, which would force the trader to sell at a loss. ([2](https://github.com/carlfarterson/token-sets/blob/master/FART%20Set/Analysis.ipynb))

|Average probability of selling at a loss over 6 months||
|--|--|
|100% ETH| 54.39%|
|FART|  49.98%|
|**Change**| **-8.1%**|

|Average End Profit % over 6 months||
|--|--|
|100% ETH| 11.96%|
|FART| 16.13%|

**Note:**
Interest earned from cDAI, performance fees, and streaming fees have not yet been factored into backtests.  Stay tuned for the announcement of improved models!

### Improvements on FART Set vs. Robo Sets
- When given a signal, FART can rebalance based on optimal weighting allocations determined from backtests. (1)

- To guard against unnecessary rebalancing, when a similar should appear the following week rebalancing only occurs when current weightings are outside of the optimal allocation. ([3](https://github.com/carlfarterson/token-sets/blob/master/FART%20Set/Determining%20Allocation%20and%20Wiggle%20Room.ipynb))

- FART rebalances on the same day and hour each week, determined by the lowest average historic volatility.  Rebalancing at a stable price point lowers slippage and prevents a sudden change in signal. ([3](https://github.com/carlfarterson/token-sets/blob/master/FART%20Set/Determining%20Rebalance%20Day%20and%20Hour.ipynb))



### [Want to add FART to your portfolio?](https://set-beta.tokensets.com/set/fart-1)

#### Additional Resources:
- [Backtests based on one timeframe can be misleading](https://github.com/carlfarterson/notebooks/blob/master/2.%20Backtests%20Can%20Be%20Misleading.ipynb)
- [Python tools for your own technical analysis](https://pypi.org/project/TAcharts/)
