from datetime import datetime
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator, constr, Field
from typing import Optional, List
from pydantic import BaseModel
from app.crud.crud_user import user_crud


#описание схем данных, которые используются для передачи данных через апи
class RestaurantsBase(BaseModel):
    name: str
    description: Optional[str] = None
    location: str

    class Config:
        orm_mode = True


class RestaurantsCreate(RestaurantsBase):
    pass


class RestaurantsUpdate(RestaurantsBase):
    # нам позволяет описывать схемы , которые мы потом будем применять к эндпоинтам
    # указываем названия полей, которые будем принимать при создании ресторана
    # этот класс используем в качестве схемы, чтобы мы потом могли работать с
    # моделями этого класса и доставать инфу из них, что то типо словаря
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None


class RestaurantsInDB(RestaurantsBase):
    # класс, который отвечает за сохранение данных в бд, указываем в каком формате хотим сохранить инфу в бд
    id: int
    created_at: datetime
    updated_at: datetime
    is_deleted: bool = False

    class Config:
        orm_mode = True