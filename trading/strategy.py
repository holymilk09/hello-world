from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any


class Signal(Enum):
    BUY = 1
    SELL = -1
    HOLD = 0


class Strategy(ABC):
    def __init__(self, params: Dict[str, Any] = None):
        self.params = params or {}

    @abstractmethod
    def generate_signal(self, symbol: str, data: Any) -> Signal:
        pass

    @abstractmethod
    def calculate_position_size(self, symbol: str, signal: Signal, capital: float) -> float:
        pass
