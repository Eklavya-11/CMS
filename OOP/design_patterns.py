"""
Enterprise Design Patterns:
- Repository pattern
- Unit of Work
- Specification pattern
- CQRS light implementation
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, List, Optional
from datetime import date

T = TypeVar('T')
ID = TypeVar('ID')

class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, item: T) -> bool:
        pass
    
    def __and__(self, other: 'Specification') -> 'AndSpecification':
        return AndSpecification(self, other)

@dataclass
class AndSpecification(Specification):
    first: Specification
    second: Specification
    
    def is_satisfied_by(self, item: T) -> bool:
        return self.first.is_satisfied_by(item) and self.second.is_satisfied_by(item)

class Repository(Generic[T, ID]):
    @abstractmethod
    def get_by_id(self, id: ID) -> Optional[T]:
        pass
    
    @abstractmethod
    def find(self, spec: Specification) -> List[T]:
        pass

class UnitOfWork(ABC):
    def __enter__(self) -> 'UnitOfWork':
        return self
        
    def __exit__(self, *args):
        self.rollback()
    
    @abstractmethod
    def commit(self):
        pass
    
    @abstractmethod
    def rollback(self):
        pass

# Concrete Implementations
class MenuItem:
    def __init__(self, id: int, name: str, is_vegetarian: bool):
        self.id = id
        self.name = name
        self.is_vegetarian = is_vegetarian

class VegetarianSpecification(Specification):
    def is_satisfied_by(self, item: MenuItem) -> bool:
        return item.is_vegetarian

class MenuRepository(Repository[MenuItem, int]):
    def __init__(self):
        self._items = {
            1: MenuItem(1, "Veg Burger", True),
            2: MenuItem(2, "Chicken Pizza", False)
        }
    
    def get_by_id(self, id: int) -> Optional[MenuItem]:
        return self._items.get(id)
    
    def find(self, spec: Specification) -> List[MenuItem]:
        return [item for item in self._items.values() if spec.is_satisfied_by(item)]

# Usage
repo = MenuRepository()
vegetarian_items = repo.find(VegetarianSpecification())
print(f"Found {len(vegetarian_items)} vegetarian items")
