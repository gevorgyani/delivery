from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.crud.crud_restaurant import restaurant_crud
from app.schemas.restaurants import RestaurantsCreate, RestaurantsUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_menu(db: AsyncSession, limit: int, offset: int) -> object:
    return await restaurant_crud.get_restaurants_in_db(db, limit=limit, offset=offset)