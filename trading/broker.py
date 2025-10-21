from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from datetime import datetime


class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"


@dataclass
class Order:
    symbol: str
    quantity: float
    order_type: OrderType
    timestamp: datetime
    limit_price: Optional[float] = None
    order_id: Optional[str] = None


class Broker(ABC):
    @abstractmethod
    def execute_order(self, order: Order) -> bool:
        pass

    @abstractmethod
    def get_cash_balance(self) -> float:
        pass
