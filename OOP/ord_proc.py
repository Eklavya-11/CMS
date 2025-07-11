"""
Advanced concepts:
- Event bus pattern
- Async coroutines
- Weak references
- Python 3.10 match-case
"""
import asyncio
from weakref import WeakSet
from dataclasses import dataclass
from enum import Enum

class EventType(Enum):
    ORDER_CREATED = 1
    ORDER_UPDATED = 2

@dataclass
class OrderEvent:
    event_type: EventType
    order_id: int
    payload: dict

class EventBus:
    def __init__(self):
        self._subscribers = defaultdict(WeakSet)
        
    def subscribe(self, event_type: EventType, callback):
        self._subscribers[event_type].add(callback)
        
    async def publish(self, event: OrderEvent):
        await asyncio.gather(
            *(callback(event) 
              for callback in self._subscribers[event.event_type])
        )

class NotificationService:
    async def send_update(self, event: OrderEvent):
        match event.event_type:
            case EventType.ORDER_CREATED:
                print(f"📬 New order #{event.order_id}")
            case EventType.ORDER_UPDATED:
                print(f"🔄 Order update #{event.order_id}: {event.payload}")

# Usage
async def main():
    bus = EventBus()
    bus.subscribe(EventType.ORDER_CREATED, NotificationService().send_update)
    
    await bus.publish(OrderEvent(
        EventType.ORDER_CREATED,
        order_id=101,
        payload={"items": ["Burger", "Fries"]}
    ))

asyncio.run(main())
