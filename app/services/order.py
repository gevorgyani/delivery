from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.crud.crud_order import order_crud
from app.schemas.order import OrderUpdate, OrderCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_order(db: AsyncSession, order_id: int):
    return await order_crud.get_order(db, order_id)


async def create_order(db: AsyncSession, order_id: int, order: OrderCreate):
    return await order_crud.create_order(db, order_id, order)


async def update_order(db: AsyncSession, order_id: int, order_update: OrderUpdate):
    db_order = await order_crud.get_order(db, order_id)
    if not db_order:
        return None
    orders_update = order_update.dict(
        exclude_unset=True)
    return await order_crud.update_order(db, db_order, orders_update)


async def delete_order(db: AsyncSession, order_id: int):
    db_order = await order_crud.get_order(db, order_id)
    if not db_order:
        return None
    return await order_crud.delete_order(db, db_order)
