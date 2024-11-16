from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.crud_base import CRUDBase
from app.models import Order

from app.schemas.order import OrderCreate


class CRUDOrder(CRUDBase):
    @staticmethod
    async def get_order(db: AsyncSession, order_id: int):
        query = select(Order).where(Order.id == order_id)
        result = await db.execute(query)
        #return result.scalar_one_or_none()
        order = result.scalar_one_or_none()
        print(f"Полученный заказ: {order}")
        return order

    @staticmethod
    async def create_order(db: AsyncSession, order: OrderCreate, user_id: int):
        db_order = Order(**order.dict(), user_id=user_id, updated_at=datetime.utcnow())
        db.add(db_order)
        await db.commit()  # подтверждение операции
        await db.refresh(db_order)
        return db_order

    @staticmethod
    async def update_order(db: AsyncSession, new_status: str, db_order):
        db_order.status = new_status
        db.add(db_order)
        await db.commit()
        await db.refresh(db_order)
        return db_order

    @staticmethod
    async def delete_order(db: AsyncSession, db_order: Order):
        db_order.is_deleted = True
        await db.commit()
        return db_order



order_crud = CRUDOrder(Order)