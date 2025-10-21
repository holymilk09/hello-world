from datetime import datetime
from typing import List
from .data import DataProvider
from .strategy import Strategy, Signal
from .broker import Broker, Order, OrderType
from .portfolio import Portfolio


class TradingEngine:
    def __init__(self, data_provider: DataProvider, strategy: Strategy,
                 broker: Broker, portfolio: Portfolio, symbols: List[str]):
        self.data_provider = data_provider
        self.strategy = strategy
        self.broker = broker
        self.portfolio = portfolio
        self.symbols = symbols

    def run_iteration(self):
        for symbol in self.symbols:
            bar = self.data_provider.get_latest_bar(symbol)
            if not bar:
                continue
            signal = self.strategy.generate_signal(symbol, bar)
            if signal == Signal.HOLD:
                continue
            current_price = self.data_provider.get_current_price(symbol)
            if not current_price:
                continue
            position_size = self.strategy.calculate_position_size(
                symbol, signal, self.broker.get_cash_balance()
            )
            if position_size == 0:
                continue
            quantity = position_size if signal == Signal.BUY else -position_size
            order = Order(symbol=symbol, quantity=quantity,
                         order_type=OrderType.MARKET, timestamp=datetime.now())
            if self.broker.execute_order(order):
                self.portfolio.update_position(symbol, quantity, current_price)

    def get_portfolio_value(self) -> float:
        current_prices = {s: self.data_provider.get_current_price(s) or 0
                         for s in self.symbols}
        return self.portfolio.total_value(current_prices)
