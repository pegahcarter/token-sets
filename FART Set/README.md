## FART-Set

### Intro
This repository contains all code for backtesting for the [FART Set](https://set-beta.tokensets.com/set/fart).

#### Description
* `Bullish = 50 MA > 100 MA > 200 MA`
  * 85% ETH - 15% DAI
* `Bearish = 50 MA < 100 MA < 200 MA`
  * 15% DAI - 85% ETH
* `Neutral = neither Bullish nor Bearish`
  * 50% ETH - 50% DAI


## FART-Set

### Intro
This repository contains all code for backtesting for the [FART Set](https://set-beta.tokensets.com/set/fart).

#### Description
Welcome to Fart Set!  

First things first: FART is built with __100% clarity and transparency.__   With Token Sets,  performance for each set is based on an underlying trading strategy for cryptocurrency.  While most Sets are traded by the private decision of the Set Founder, FART combines consistent rebalancing with honest automation and robust backtesting for a strategy you can trust.

Fart Set works similarly to a portfolio holding 50% Ethereum and 50% USD.  The goal with FART is to capture a significant portion of the upside while reducing volatility and total drawdown.  At the same time every week, FART has the potential to adjust weighting based on a bullish or bearish signal.  These signals are:

- bull: 50-hour SMA > 100-hour SMA > 200-hour SMA
- bear: 50-hour SMA < 100-hour SMA < 200-hour SMA
(Note: SMA is the simple moving average based on the close)

If there is a signal, Fart Set will rebalance based on the optimal weighting distribution calculated in the public backtests.






Backtests and code used for rebalancing are available here.



Investing in cryptocurrenies is risky and could result in large gains and/or losses. Past results do not guarantee future returns. Only use with money you can afford to lose.
