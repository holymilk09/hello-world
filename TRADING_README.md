# Trading Algorithm Foundation

A robust, modular foundation for building trading algorithms in Python (140 lines of code).

## Architecture

The foundation follows a clean separation of concerns with 5 core components:

### Core Components

1. **DataProvider** (`trading/data.py`)
   - Abstract interface for market data
   - Provides price bars and current prices
   - Easily swappable for live/backtest/paper trading

2. **Strategy** (`trading/strategy.py`)
   - Base class for trading strategies
   - Generates trading signals (BUY/SELL/HOLD)
   - Calculates position sizes

3. **Broker** (`trading/broker.py`)
   - Interface for order execution
   - Handles market and limit orders
   - Manages cash balance

4. **Portfolio** (`trading/portfolio.py`)
   - Tracks positions and cash
   - Calculates total portfolio value
   - Manages position updates with average pricing

5. **TradingEngine** (`trading/engine.py`)
   - Orchestrates all components
   - Runs trading iterations
   - Coordinates data → strategy → broker → portfolio flow

## Usage

```python
from trading import (
    DataProvider, Strategy, Signal, Broker,
    Portfolio, TradingEngine
)

# 1. Extend base classes with your implementations
class MyDataProvider(DataProvider):
    # Implement get_latest_bar() and get_current_price()
    pass

class MyStrategy(Strategy):
    # Implement generate_signal() and calculate_position_size()
    pass

class MyBroker(Broker):
    # Implement execute_order() and get_cash_balance()
    pass

# 2. Initialize components
data = MyDataProvider()
strategy = MyStrategy()
broker = MyBroker(initial_cash=10000)
portfolio = Portfolio(initial_capital=10000)

# 3. Create and run engine
engine = TradingEngine(data, strategy, broker, portfolio, ["AAPL", "GOOGL"])
engine.run_iteration()
portfolio_value = engine.get_portfolio_value()
```

## Example

See `example.py` for a complete working example with mock implementations.

Run: `python3 example.py`

## Design Principles

- **Modularity**: Each component has a single responsibility
- **Extensibility**: Abstract base classes for easy customization
- **Testability**: Components can be tested independently
- **Simplicity**: Minimal but functional implementation

## Next Steps

Build on this foundation by:
- Adding risk management rules
- Implementing backtesting engine
- Creating specific trading strategies
- Adding performance analytics
- Integrating with real brokers/data sources
