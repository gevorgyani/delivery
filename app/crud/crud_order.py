from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.crud_base import CRUDBase
from app.models import Order
from app.models.dish import Dish
from app.schemas.order import OrderCreate


class CRUDOrder(CRUDBase):
    @staticmethod
    async def get_order(db: AsyncSession, order_id: int):
        query = select(Dish).where(Order.order_id == order_id, Order.is_deleted == False)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def create_order(db: AsyncSession, order: OrderCreate):
        db_order = Dish(**order.dict())
        db.add(db_order)
        await db.commit()  # подтверждение операции
        return db_order

    @staticmethod
    async def update_order(db: AsyncSession, orders_update: dict, db_order: Order):
        for key, value in orders_update.items():
            setattr(db_order, key, value)  #
        db_order.updated_at = datetime.utcnow()
        await db.commit()
        return db_order

    @staticmethod
    async def delete_order(db: AsyncSession, db_order: Order):
        db_order.is_deleted = True
        await db.commit()
        return db_order



order_crud = CRUDOrder(Order)