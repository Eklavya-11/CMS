"""
Data science-ready Python:
- NumPy arrays
- Generator expressions
- Memory views
- Statistical operations
"""
import numpy as np
from collections.abc import Generator

def analyze_orders(orders: Generator[dict, None, None]) -> dict[str, float]:
    # Convert to memory-efficient numpy arrays
    amounts = np.fromiter(
        (o['amount'] for o in orders), 
        dtype=np.float32
    )
    
    return {
        'mean': float(np.mean(amounts)),
        'median': float(np.median(amounts)),
        'std_dev': float(np.std(amounts)),
        'total': float(np.sum(amounts)),
        'peak_hour': np.argmax(np.bincount([
            o['hour'] for o in orders
        ]))
    }

# Usage
orders = (
    {'amount': 12.99, 'hour': 12},
    {'amount': 8.50, 'hour': 18},
    {'amount': 24.30, 'hour': 12}
)

print(analyze_orders(orders))
