from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


#описание схем данных, которые используются для передачи данных через апи
class OrderBase(BaseModel):
    user_id: int
    dish_id: int
    order_date: datetime
    status: Optional[str] = None


class OrderCreate(BaseModel):
    dish_id: int


class OrderUpdate(OrderBase):
    # нам позволяет описывать схемы , которые мы потом будем применять к эндпоинтам
    # указываем названия полей, которые будем принимать при создании ресторана
    # этот класс используем в качестве схемы, чтобы мы потом могли работать с
    # моделями этого класса и доставать инфу из них, что то типо словаря
    status: Optional[str] = None


class OrderInDB(OrderBase):
    # класс, который отвечает за сохранение данных в бд, указываем в каком формате хотим сохранить инфу в бд
    id: int
    created_at: datetime
    updated_at: datetime
    is_deleted: bool = False

    class Config:
        orm_mode = True