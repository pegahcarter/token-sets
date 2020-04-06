# FART Set
## By: Carter Carlson
### Description
This repository contains all code used to backtest and maintain the [FART Set](https://set-beta.tokensets.com/set/fart).


#### Introduction
Welcome to Fart Set!  

First things first: FART is built with __100% clarity and transparency.__   With Token Sets,  performance for each Set is based on an underlying trading strategy for cryptocurrency.  While most Sets are traded by the private decision of the Set Founder, FART combines consistent rebalancing with honest automation and robust backtesting for a strategy you can trust.

Cryptocurrency markets are highly volatile! FART provides traders an opportunity to capture
the majority of upwards price movement with lower risk, volatility, and drawdown.  FART acts
like a portfolio of 50% Ethereum and 50% USD most of the time, increasing ETH held
during bullish signals and decreasing ETH held during bearish signals.


#### Signals
At the same time every week, FART has the potential to adjust weighting based on a bullish or bearish signal.  These signals are:

- bull: 50-hour SMA > 100-hour SMA > 200-hour SMA
- bear: 50-hour SMA < 100-hour SMA < 200-hour SMA
(Note: SMA is the simple moving average based on the hourly close)


#### Improvements on Fart Set vs. Robo Sets
- If there is a signal, FART will rebalance based on the optimal weighting allocation
determined from backtests.
- If the same signal shows up the following week, rebalancing will only occur if
the current weights are far enough away from the optimal allocation.  This prevents
unnecessary rebalancing.
- FART rebalances on the same day and hour each week, determined by the lowest average
historic volatility.  Rebalancing at a stable price point lowers slippage and prevents
a sudden change in signal.
