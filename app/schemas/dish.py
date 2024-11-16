from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


#описание схем данных, которые используются для передачи данных через апи
class DishBase(BaseModel):
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    # нам позволяет описывать схемы , которые мы потом будем применять к эндпоинтам
    # указываем названия полей, которые будем принимать при создании ресторана
    # этот класс используем в качестве схемы, чтобы мы потом могли работать с
    # моделями этого класса и доставать инфу из них, что то типо словаря
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class DishInDB(DishBase):
    # класс, который отвечает за сохранение данных в бд, указываем в каком формате хотим сохранить инфу в бд
    restaurant_id: int
    created_at: datetime
    updated_at: datetime
    is_deleted: bool = False



class DishOut(DishBase):
    id: int
    restaurant_id: int

    class Config:
        orm_mode = True
