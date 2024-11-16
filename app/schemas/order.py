from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel



#описание схем данных, которые используются для передачи данных через апи
class OrderBase(BaseModel):
    #user_id: int
    #dish_id: int
    status: str

    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    dish_id: int


class OrderUpdate(OrderBase):
    status: str


class OrderInDB(OrderBase):
    id: int
    user_id: int
    dish_id: int
    updated_at: datetime
    order_date: datetime
    is_deleted: bool = False

    class Config:
        orm_mode = True