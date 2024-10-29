from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.order import OrderInDB, OrderCreate, OrderUpdate
from app.schemas.restaurants import RestaurantsInDB, RestaurantsCreate, RestaurantsUpdate
from app.core.db import get_async_session
from app.services import order

router = APIRouter()


@router.get("/orders/{order_id}/", response_model=OrderInDB)
async def get_order(order_id: int,
                    db: AsyncSession = Depends(get_async_session)):
    orders = await order.get_order(db, order_id)
    return orders


@router.post("/", response_model=OrderInDB)
async def create_order(orders: OrderCreate, db: AsyncSession = Depends(get_async_session)):
    return await order.create_order(db, orders)


@router.put("/{order_id}/status", response_model=OrderInDB)
async def update_order(order_id: int, status_update: OrderUpdate, db: AsyncSession = Depends(get_async_session)):
    db_order = await order.update_order(db, order_id, status_update)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.delete("/{order_id}/", response_model=dict)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_async_session)):
    db_order = await order.delete_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order as deleted successfully"}
