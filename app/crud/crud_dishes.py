from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.crud_base import CRUDBase
from app.models import Restaurant
from app.models.dish import Dish
from app.schemas.dish import DishCreate, DishUpdate


class CRUDDish(CRUDBase):
    @staticmethod
    async def get_dishes(db: AsyncSession, restaurant_id: int):
        query = select(Dish).where(Dish.restaurant_id == restaurant_id, Restaurant.is_deleted == False)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_dish_by_id(db: AsyncSession, restaurant_id: int, dish_id: int):
        query = select(Dish).where(Dish.id == dish_id, Dish.restaurant_id == restaurant_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @staticmethod
    async def create_dish(db: AsyncSession, restaurant_id: int, dish_id: DishCreate):
        db_dish = Dish(**dish_id.dict(), restaurant_id=restaurant_id)
        db.add(db_dish)
        await db.commit()  # подтверждение операции
        return db_dish

    @staticmethod
    async def update_dish(db: AsyncSession, dishes_update: dict, db_dish: Dish):
        for key, value in dishes_update.items():
            setattr(db_dish, key, value)  #
        db_dish.updated_at = datetime.utcnow()
        await db.commit()
        return db_dish

    @staticmethod
    async def delete_dish(db: AsyncSession, db_dish: Dish):
        db_dish.is_deleted = True
        await db.commit()
        return db_dish



dish_crud = CRUDDish(Dish)