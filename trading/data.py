from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Bar:
    timestamp: datetime
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: float


class DataProvider(ABC):
    @abstractmethod
    def get_latest_bar(self, symbol: str) -> Optional[Bar]:
        pass

    @abstractmethod
    def get_current_price(self, symbol: str) -> Optional[float]:
        pass
