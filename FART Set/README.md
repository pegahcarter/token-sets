# FART Set
## By: Carter Carlson
### Description
This repository contains all code used to backtest and maintain the [FART Set](https://set-beta.tokensets.com/set/fart).


#### Introduction
Welcome to Fart Set!  

Most Sets are traded by the private decision of the Set Founder, putting your trust in a system that you know little or even nothing about. FART combines consistent rebalancing with honest automation and robust backtesting for a strategy you can trust.  

The algorithm behind FART is highly dynamic and therefore able to capitalize on the volatility of the market while still ensuring safe handling of your assets. FART is a weighted portfolio of 50% Ethereum and 50% USD with fluctuating % ETH held depending on market trends. FART provides traders an opportunity to capture the majority of upwards price movement with lower risk, volatility, and drawdown.

Consistent returns enable traders to exit their positions at any time without the risk of being stuck in an underperforming position and selling at a loss. Where humans naturally fail, FART naturally capitalizes.


#### Signals
At the same time every week, FART has the potential to adjust weighting based on a bullish or bearish signal.  These signals are:

- bull: 50-hour SMA > 100-hour SMA > 200-hour SMA
- bear: 50-hour SMA < 100-hour SMA < 200-hour SMA
(Note: SMA is the simple moving average based on the hourly close)


#### Improvements on Fart Set vs. Robo Sets
- If there is a signal, FART will rebalance based on the optimal weighting allocation determined from backtests (backtest link here).
- If the same signal shows up the following week, rebalancing will only occur if the current weights are far enough away from the optimal allocation (backtest link here).  This prevents unnecessary rebalancing.
- FART rebalances on the same day and hour each week, determined by the lowest average historic volatility (backtest link here).  Rebalancing at a stable price point lowers slippage and prevents a sudden change in signal.


FART is built with 100% clarity and transparency.
