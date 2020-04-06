# Simulate rebalancing
from portfolio import Portfolio


def simulate(coins, allocation, wiggle_room, df):

    start_prices = [df[0][coin] for coin in coins]
    portfolio = Portfolio(coins, start_prices)

    eth_netval = []
    rebalanced_netval = []

    for index, row in enumerate(df):

        current_prices = [df[index][coin] for coin in coins]
        dollar_values = portfolio.units * current_prices
        net_dollar_value = sum(dollar_values)

        # Rebalance if needed to
        if row['rebalance']:
            weights_current = dollar_values / net_dollar_value
            weights_preferred = allocation[row['signal']]

            trade_weights = (weights_preferred - weights_current) / 2
            is_trade_actionable = max(trade_weights) > wiggle_room

            if is_trade_actionable:
                trade_dollar_values = trade_weights * net_dollar_value
                trade_units = trade_dollar_values / current_prices
                trade_units_after_slippage = [
                    (1-portfolio.SLIPPAGE)*t if t > 0 else t for t in trade_units
                ]
                portfolio.units += trade_units

        # Append net_dollar_value
        rebalanced_netval.append(net_dollar_value)
        eth_netval.append(portfolio.start_units[coins.index('ETH')] * len(coins) * current_prices[coins.index('ETH')])

    # Take the cumulative distance between rebalanced and nonrebalanced portfolios
    cum_performance = sum(np.subtract(rebalanced_netval, eth_netval) / eth_netval)

    return rebalanced_netval, eth_netval, cum_performance
