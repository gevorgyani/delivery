from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import restaurant
from app.schemas.restaurants import RestaurantsInDB, RestaurantsCreate, RestaurantsUpdate, RestaurantsBase
from app.core.db import get_async_session
from app.services import restaurants_service
router = APIRouter()


@router.get("/", response_model=List[RestaurantsBase])
async def get_restaurants(
        limit: int = Query(10, le=30),  #по умолчанию 10 максимум 30
        offset: int = Query(0),
        db: AsyncSession = Depends(get_async_session)):
    restaurants = await restaurants_service.get_restaurants(db, limit=limit, offset=offset)
    return restaurants


@router.post("/", response_model=RestaurantsBase)
async def create_restaurants_endpoint(restaurants: RestaurantsCreate, db: AsyncSession = Depends(get_async_session)):
    return await restaurants_service.create_restaurant_service(session=db, obj_in=restaurants)


@router.get("/{restaurant_id}/", response_model=RestaurantsBase)
async def search_by_id(restaurant_id: int, db: AsyncSession = Depends(get_async_session)):
    restaurant_result = await restaurants_service.get_restaurant_by_id(db, restaurant_id)
    if not restaurant_result:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant_result


@router.put("/{restaurant_id}", response_model=RestaurantsBase)
async def update_restaurant_endpoint(restaurant_id: int, restaurant_data: RestaurantsUpdate, db: AsyncSession = Depends(get_async_session)):
    db_restaurant = await restaurants_service.update_restaurant_service(db, restaurant_id, restaurant_data)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.delete("/{restaurant_id}", response_model=dict)
async def delete_note_endpoint(restaurant_id: int, db: AsyncSession = Depends(get_async_session)):
    db_restaurant = await restaurants_service.delete_restaurant_service(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return {"message": "Restaurant as deleted successfully"}



