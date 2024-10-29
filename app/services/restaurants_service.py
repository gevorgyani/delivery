from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.crud.crud_restaurant import restaurant_crud
from app.schemas.restaurants import RestaurantsCreate, RestaurantsUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_restaurants(db: AsyncSession, limit: int, offset: int) -> object:
    return await restaurant_crud.get_restaurants_in_db(db, limit=limit, offset=offset)


async def create_restaurant_service(db: AsyncSession, restaurant: RestaurantsCreate):
    restaurant_data = restaurant.dict()
    return await restaurant_crud.create(db, restaurant_data)


async def update_restaurant_service(db: AsyncSession, restaurant_id: int, restaurant_update: RestaurantsUpdate):
    db_restaurant = await restaurant_crud.get_restaurant_by_id(db, restaurant_id)  # по id получаем заметку
    if not db_restaurant:
        return None
    update_restaurant = restaurant_update.dict(
        exclude_unset=True)  # exclude_unset позволяет все сделать как ключ к значению
    return await restaurant_crud.update_restaurant_in_db(db, update_restaurant, db_restaurant)


async def delete_restaurant_service(db: AsyncSession, restaurant_id: int):
    db_restaurant = await restaurant_crud.get_restaurant_by_id(db, restaurant_id)
    if not db_restaurant:
        return None
    return await restaurant_crud.delete_restaurant_in_db(db, db_restaurant)
