"""
Demonstrates:
- Memoization
- Property Caching
- LRU Caching
"""
from functools import lru_cache
from time import sleep

class MenuService:
    def __init__(self):
        self._menu = None
    
    @property
    def menu(self):
        """Cached property"""
        if self._menu is None:
            print("Loading menu from database...")
            sleep(2)  # Simulate DB call
            self._menu = self._load_menu()
        return self._menu
    
    @lru_cache(maxsize=32)
    def get_item(self, item_id: int):
        """LRU-cached item lookup"""
        print(f"Fetching item {item_id}...")
        sleep(1)
        return next((item for item in self.menu if item["id"] == item_id), None)
    
    def _load_menu(self):
        return [
            {"id": 1, "name": "Burger", "price": 8.99},
            {"id": 2, "name": "Pizza", "price": 11.99}
        ]

# Usage
service = MenuService()
print(service.menu)  # Loads once
print(service.get_item(1))  # Cached subsequent calls
