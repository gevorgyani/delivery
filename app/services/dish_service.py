from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.crud.crud_dishes import dish_crud
from app.schemas.dish import DishCreate, DishUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_dishes(db: AsyncSession, restaurant_id: int):
    return await dish_crud.get_dishes(db, restaurant_id)


async def create_dish(db: AsyncSession, restaurant_id: int, dish_id: DishCreate):
    return await dish_crud.create_dish(db, restaurant_id=restaurant_id, dish_id=dish_id)


async def update_dish(db: AsyncSession, restaurant_id: int, dish_id: int, dish_update: DishUpdate):
    db_dish = await dish_crud.get_dish_by_id(db, restaurant_id, dish_id)
    if not db_dish:
        return None
    dishes_update = dish_update.dict(
        exclude_unset=True)
    return await dish_crud.update_dish(db, dishes_update, db_dish)


async def delete_dish(db: AsyncSession, restaurant_id: int, dish_id: int):
    db_dish = await dish_crud.get_dish_by_id(db, restaurant_id, dish_id)
    if not db_dish:
        return None
    return await dish_crud.delete_dish(db, db_dish)
