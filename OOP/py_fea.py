"""
Demonstrates:
- Pattern Matching (Python 3.10+)
- Type Unions
- Context Managers
- Walrus Operator
"""
from contextlib import contextmanager
from typing import Union

class User:
    def __init__(self, role: str):
        self.role = role

@contextmanager
def database_connection(db_url: str):
    """Context manager for DB connections"""
    print(f"Connecting to {db_url}")
    yield {"connection": "active"}
    print("Connection closed")

def process_order(order_data: dict, user: User) -> Union[str, float]:
    """Process order with pattern matching"""
    match (order_data.get("status"), user.role):
        case ("pending", "admin"):
            return "Admin override"
        case ("completed", _):
            if discount := order_data.get("discount"):
                return f"Applied {discount}% discount"
            return order_data["total"]
        case _:
            raise ValueError("Invalid order state")

# Usage
with database_connection("mysql://localhost") as conn:
    user = User("admin")
    result = process_order({"status": "pending", "total": 49.99}, user)
    print(f"Result: {result}")
