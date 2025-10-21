from dataclasses import dataclass
from typing import Dict


@dataclass
class Position:
    symbol: str
    quantity: float
    avg_price: float

    def update(self, quantity: float, price: float):
        if self.quantity + quantity == 0:
            self.avg_price = 0
            self.quantity = 0
        else:
            total_cost = (self.quantity * self.avg_price) + (quantity * price)
            self.quantity += quantity
            self.avg_price = total_cost / self.quantity if self.quantity != 0 else 0


class Portfolio:
    def __init__(self, initial_capital: float):
        self.cash = initial_capital
        self.positions: Dict[str, Position] = {}

    def update_position(self, symbol: str, quantity: float, price: float):
        self.cash -= quantity * price
        if symbol in self.positions:
            self.positions[symbol].update(quantity, price)
            if self.positions[symbol].quantity == 0:
                del self.positions[symbol]
        elif quantity != 0:
            self.positions[symbol] = Position(symbol, quantity, price)

    def total_value(self, current_prices: Dict[str, float]) -> float:
        positions_value = sum(
            pos.quantity * current_prices.get(pos.symbol, pos.avg_price)
            for pos in self.positions.values()
        )
        return self.cash + positions_value
