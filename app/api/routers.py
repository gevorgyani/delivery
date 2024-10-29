from fastapi import APIRouter
from app.api.endpoints import auth_router
from app.api.endpoints import restaurants_router

main_router = APIRouter()
main_router.include_router(auth_router, tags=['Authentication'], prefix='/auth')
main_router.include_router(restaurants_router, tags=['Restaurants'], prefix='/restaurants')