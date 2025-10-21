#!/usr/bin/env python3
"""
Example usage of the trading algorithm foundation.
This demonstrates how to extend the base classes.
"""

from datetime import datetime
from trading import (
    DataProvider, Strategy, Signal, Broker, Order,
    Portfolio, TradingEngine, Bar
)


class MockDataProvider(DataProvider):
    """Simple mock data provider for demonstration."""

    def __init__(self):
        self.prices = {"AAPL": 150.0, "GOOGL": 2800.0}

    def get_latest_bar(self, symbol: str):
        price = self.prices.get(symbol, 0)
        return Bar(
            timestamp=datetime.now(),
            symbol=symbol,
            open=price * 0.99,
            high=price * 1.01,
            low=price * 0.98,
            close=price,
            volume=1000000
        )

    def get_current_price(self, symbol: str):
        return self.prices.get(symbol)


class SimpleStrategy(Strategy):
    """Example strategy that buys when price is low."""

    def generate_signal(self, symbol: str, data: Bar) -> Signal:
        if data.close < data.open:
            return Signal.BUY
        elif data.close > data.high * 0.99:
            return Signal.SELL
        return Signal.HOLD

    def calculate_position_size(self, symbol: str, signal: Signal, capital: float) -> float:
        return capital * 0.1 / 150  # Use 10% of capital


class PaperBroker(Broker):
    """Paper trading broker for testing."""

    def __init__(self, initial_cash: float):
        self.cash = initial_cash

    def execute_order(self, order: Order) -> bool:
        print(f"Executed: {order.quantity} shares of {order.symbol}")
        return True

    def get_cash_balance(self) -> float:
        return self.cash


if __name__ == "__main__":
    # Initialize components
    data_provider = MockDataProvider()
    strategy = SimpleStrategy({"threshold": 0.02})
    broker = PaperBroker(10000)
    portfolio = Portfolio(10000)

    # Create engine
    engine = TradingEngine(
        data_provider=data_provider,
        strategy=strategy,
        broker=broker,
        portfolio=portfolio,
        symbols=["AAPL", "GOOGL"]
    )

    # Run a trading iteration
    print("Running trading iteration...")
    engine.run_iteration()

    # Check portfolio value
    portfolio_value = engine.get_portfolio_value()
    print(f"Portfolio value: ${portfolio_value:,.2f}")
