"""
Demonstrates:
- Abstract Base Classes
- Strategy Pattern
- Type Hints
- Dependency Injection
- Dataclasses
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    CANCELLED = auto()

@dataclass
class MenuItem:
    """Immutable menu item with validation"""
    id: int
    name: str
    price: float
    description: str = ""
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

class PaymentStrategy(ABC):
    """Strategy Pattern for payments"""
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount:.2f}")
        return True

class DigitalWalletPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Processing digital wallet payment of ${amount:.2f}")
        return True

class Order:
    """Main order class with state management"""
    def __init__(
        self, 
        order_id: int, 
        items: List[MenuItem], 
        payment_strategy: PaymentStrategy
    ):
        self.order_id = order_id
        self.items = items
        self._status = OrderStatus.PENDING
        self._payment_strategy = payment_strategy
    
    @property
    def total(self) -> float:
        return sum(item.price for item in self.items)
    
    @property
    def status(self) -> OrderStatus:
        return self._status
    
    def process_order(self) -> None:
        """Template method pattern"""
        self._validate_order()
        if self._payment_strategy.pay(self.total):
            self._status = OrderStatus.PROCESSING
            self._fulfill_order()
    
    def _validate_order(self) -> None:
        if not self.items:
            raise ValueError("Order must contain items")
    
    def _fulfill_order(self) -> None:
        print(f"Order {self.order_id} is being prepared")
        self._status = OrderStatus.COMPLETED

# Usage Example
if __name__ == "__main__":
    items = [
        MenuItem(1, "Burger", 8.99),
        MenuItem(2, "Fries", 3.49)
    ]
    
    order = Order(
        order_id=101,
        items=items,
        payment_strategy=CreditCardPayment()
    )
    
    order.process_order()
    print(f"Order status: {order.status.name}")
