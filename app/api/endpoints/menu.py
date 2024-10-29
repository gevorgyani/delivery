from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.schemas import dish
from app.schemas.dish import DishInDB, DishCreate, DishUpdate
from app.services import dish

router = APIRouter()


@router.get("/{restaurant_id}/menu/", response_model=List[DishInDB])
async def get_menu(restaurant_id: int, db: AsyncSession = Depends(get_async_session)):
    menu = await dish.get_dishes(db, restaurant_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu


@router.post("/{restaurant_id}/menu/", response_model=DishInDB)
async def create_dish(restaurant_id: int, dish: DishCreate, db: AsyncSession = Depends(get_async_session)):
    return await dish.create_dish(db, restaurant_id, dish)


@router.put("/{restaurant_id}/menu/{dish_id}/", response_model=DishInDB)
async def update_dish(restaurant_id: int, dish_id: int, dish: DishUpdate,
                      db: AsyncSession = Depends(get_async_session)):
    updated_dish = await dish.update_dish(db, restaurant_id, dish_id, dish)
    if updated_dish is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return updated_dish


@router.delete("/{restaurant_id}/menu/{dish_id}/", response_model=dict)
async def delete_dish(restaurant_id: int, dish_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await dish.delete_dish(db, restaurant_id, dish_id)
    if not result:
        raise HTTPException(status_code=404, detail="Dish not found")
    return {"message": "Dish deleted successfully"}