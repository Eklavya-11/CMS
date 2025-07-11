"""
Demonstrates:
- Async/Await
- Context Managers
- Custom Exceptions
- Generators
"""
import asyncio
from contextlib import asynccontextmanager
from datetime import datetime

class InventoryError(Exception):
    """Custom exception for inventory issues"""
    pass

class AsyncInventory:
    def __init__(self):
        self.stock = {}
        self.lock = asyncio.Lock()
    
    async def update_stock(self, item_id: int, quantity: int):
        async with self.lock:  # Thread-safe operation
            self.stock[item_id] = self.stock.get(item_id, 0) + quantity
    
    @asynccontextmanager
    async def reserve_items(self, items: dict):
        """Context manager for inventory reservation"""
        try:
            await self._check_availability(items)
            yield
        except InventoryError as e:
            print(f"Reservation failed: {e}")
            raise
    
    async def _check_availability(self, items: dict):
        async with self.lock:
            for item_id, qty in items.items():
                if self.stock.get(item_id, 0) < qty:
                    raise InventoryError(f"Insufficient stock for item {item_id}")

async def demo_inventory():
    inventory = AsyncInventory()
    await inventory.update_stock(101, 50)
    
    try:
        async with inventory.reserve_items({101: 3}):
            print("Items reserved successfully")
            # Process order here
    except InventoryError:
        print("Order cancelled due to stock issues")

asyncio.run(demo_inventory())
