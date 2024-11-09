from fastapi import APIRouter
from app.api.endpoints import auth_router
from app.api.endpoints import restaurants_router, menu_router, orders_router

main_router = APIRouter()
main_router.include_router(auth_router, tags=['Authentication'], prefix='/auth')
main_router.include_router(restaurants_router, tags=['Restaurants'], prefix='/restaurants')
# Маршрутизация для работы с меню и блюдами
main_router.include_router(menu_router, tags=['Menu'], prefix='/menu')

# Маршрутизация для работы с заказами
main_router.include_router(orders_router, tags=['Orders'], prefix='/orders')

# Маршрутизация для работы с отзывами и рейтингами
# main_router.include_router(reviews_router, tags=['Reviews'], prefix='/reviews')