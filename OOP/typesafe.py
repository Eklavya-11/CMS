"""
Modern API development:
- Pydantic models
- Strict type checking
- JSON schema generation
- Custom validators
"""
from pydantic import BaseModel, validator, Field
from datetime import datetime
from typing import Literal

class MenuItemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    category: Literal["food", "beverage", "dessert"]
    tags: list[str] = []
    
    @validator('price')
    def round_price(cls, v):
        return round(v, 2)

class MenuItemResponse(MenuItemCreate):
    id: int
    created_at: datetime
    updated_at: datetime | None
    
    class Config:
        json_schema = {
            "example": {
                "id": 1,
                "name": "Cheeseburger",
                "price": 9.99,
                "category": "food",
                "created_at": "2023-01-01T12:00:00Z"
            }
        }

# Usage
item = MenuItemCreate(
    name="Pizza",
    price=12.50,
    category="food"
)

print(item.model_dump_json(indent=2))
