## 2020.03.18

### Version 1
* `Bullish = 25 MA > 50 MA > 100 MA`
* `Bearish = 25 MA < 50 MA < 100 MA`
* `Scenario: Coin A is based in Coin B (Coin A/Coin B)`
  * If bullish:
    * Allocate 25% of Coin B to Coin A
  * If bearish:
    * Allocate 25% of coin A to Coin B
  * If neutral:
    * Rebalance to 50-50 weighting (based on USD val)
* `Scenario: Coin A and Coin B are based in USD (Coin A/USD, Coin B/USD)`
  * If coin A is bullish and coin B is neutral:
    * Allocate 25% of coin B to coin A
  * If coin A is bearish and coin B is neutral:
    * Allocate 25% of coin B to coin A
  * If coin A and coin B are both neutral, bullish, or bearish:
    * Rebalance to 50-50 weighting
