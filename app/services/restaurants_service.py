from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.crud.crud_restaurant import restaurant_crud
from app.schemas.restaurants import RestaurantsCreate, RestaurantsUpdate, RestaurantsBase

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_restaurants(db: AsyncSession, limit: int, offset: int) -> object:
    return await restaurant_crud.get_restaurants_in_db(db, limit=limit, offset=offset)


async def get_restaurant_by_id(db: AsyncSession, restaurant_id: int):
    return await restaurant_crud.get_restaurant_by_id(db, restaurant_id)


async def create_restaurant_service(obj_in: RestaurantsCreate,
        session: AsyncSession):
    return await restaurant_crud.create(session=session, obj_in=obj_in)


async def update_restaurant_service(db: AsyncSession, restaurant_id: int, restaurant_data: RestaurantsUpdate):
    db_restaurant = await restaurant_crud.get_restaurant_by_id(db, restaurant_id)  # по id получаем ресторан
    if not db_restaurant:
        return None
    update_restaurant = restaurant_data.dict(
        exclude_unset=True)  # exclude_unset позволяет все сделать как ключ к значению
    return await restaurant_crud.update_restaurant_in_db(db, db_restaurant, update_restaurant)


async def delete_restaurant_service(db: AsyncSession, restaurant_id: int) -> RestaurantsBase:
    db_restaurant = await restaurant_crud.get_restaurant_by_id(db, restaurant_id)
    if not db_restaurant:
        return None
    return await restaurant_crud.delete_restaurant_in_db(db, db_restaurant)
