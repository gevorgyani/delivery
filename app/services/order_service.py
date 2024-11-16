from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.crud.crud_order import order_crud
from app.schemas.order import OrderUpdate, OrderCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_order(db: AsyncSession, order_id: int):
    return await order_crud.get_order(db, order_id)


async def create_order(db: AsyncSession, order: OrderCreate, user_id: int):
    return await order_crud.create_order(db, order, user_id)


async def update_order(db: AsyncSession, order_id: int, status: OrderUpdate):
    db_order = await order_crud.get_order(db, order_id)
    print(db_order)
    if not db_order:
        return None
    #print("Обновление заказа с:", orders_update)
    #print("Текущий db_order:", db_order)
    return await order_crud.update(db_obj=db_order, obj_in=status, session=db)


async def delete_order(db: AsyncSession, order_id: int):
    db_order = await order_crud.get_order(db, order_id)
    if not db_order:
        return None
    return await order_crud.delete_order(db, db_order)
