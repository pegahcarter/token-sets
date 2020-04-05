# Simulate rebalancing
from portfolio import Portfolio


def simulate(coins, allocation, wiggle_room, df):

    start_prices = df[coins].iloc[0]
    portfolio = Portfolio(coins, start_prices)
    rebalanced_netval = []

    for index, row in df.iterrows():

        current_prices = row[coins]
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

        # Append net_dollar_value for each interval
        rebalanced_netval.append(net_dollar_value)

    # Nonrebalanced net dollar value for each interval
    nonrebalanced_netval = (portfolio.start_units * df[coins]).sum(axis=1)

    # Take the cumulative distance between rebalanced and nonrebalanced portfolios
    cum_performance = sum((rebalanced_netval - nonrebalanced_netval) / nonrebalanced_netval)

    return cum_performance
