from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import restaurant
from app.schemas.restaurants import RestaurantsInDB, RestaurantsCreate, RestaurantsUpdate
from app.core.db import get_async_session
from app.services import restaurants_service
from app.crud import crud_restaurant
router = APIRouter()


@router.get("/restaurants/", response_model=List[RestaurantsInDB])
async def get_restaurants(
        limit: int = Query(10, le=30),  #по умолчанию 10 максимум 30
        offset: int = Query(0),
        db: AsyncSession = Depends(get_async_session)):
    restaurants = await restaurants_service.get_restaurants(db, limit=limit, offset=offset)
    return restaurants


@router.post("/", response_model=RestaurantsInDB)
async def create_restaurants_endpoint(restaurants: RestaurantsCreate, db: AsyncSession = Depends(get_async_session)):
    return await restaurants_service.create_restaurant_service(db, restaurants)


@router.get("/{restaurant_id}/", response_model=RestaurantsInDB)
async def search_by_id(restaurant_id: int, db: AsyncSession = Depends(get_async_session)):
    restaurant = await crud_restaurant.get_restaurant_by_id(db, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@router.put("/{restaurant_id}", response_model=RestaurantsInDB)
async def update_restaurant_endpoint(restaurant_id: int, restaurant: RestaurantsUpdate, db: AsyncSession = Depends(get_async_session)):
    db_restaurant = await restaurants_service.update_restaurant_service(db, restaurant_id, restaurant)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.delete("/{restaurant_id}", response_model=dict)
async def delete_note_endpoint(restaurant_id: int, db: AsyncSession = Depends(get_async_session)):
    db_restaurant = await restaurants_service.delete_restaurant_service(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return {"message": "Restaurant as deleted successfully"}



