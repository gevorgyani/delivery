from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.crud_base import CRUDBase
from app.models.restaurant import Restaurant


class CRUDRestaurant(CRUDBase):
    @staticmethod
    async def get_restaurants_in_db(db: AsyncSession, limit: int, offset: int):
        query = select(Restaurant).where(Restaurant.is_deleted == False).limit(limit).offset(offset).order_by(Restaurant.id)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_restaurant_by_id(db: AsyncSession, restaurant_id: int):
        query = select(Restaurant).where(Restaurant.id == restaurant_id, Restaurant.is_deleted == False)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @staticmethod
    async def update_restaurant_in_db(db: AsyncSession, db_restaurant: Restaurant, update_restaurant: dict):
        for key, value in update_restaurant.items():
            setattr(db_restaurant, key, value)  #
        db_restaurant.updated_at = datetime.utcnow()
        await db.commit()
        return db_restaurant

    @staticmethod
    async def delete_restaurant_in_db(db: AsyncSession, db_restaurant: Restaurant):
        db_restaurant.is_deleted = True
        await db.commit()
        return db_restaurant


restaurant_crud = CRUDRestaurant(Restaurant)