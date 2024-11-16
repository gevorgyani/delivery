from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.schemas.order import OrderInDB, OrderCreate, OrderUpdate
from app.core.db import get_async_session
from app.services import order_service
from app.core.security import get_current_user

router = APIRouter()


@router.get("/orders/{order_id}/", response_model=OrderInDB)
async def get_order(order_id: int,
                    db: AsyncSession = Depends(get_async_session),
                    current_user: User = Depends(get_current_user)):
    order = await order_service.get_order(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/")
async def create_order(orders: OrderCreate,
                       db: AsyncSession = Depends(get_async_session),
                       current_user: User = Depends(get_current_user)):
    return await order_service.create_order(db, orders, user_id=current_user.id)


@router.put("/{order_id}/status")
async def update_order(order_id: int,
                       status: OrderUpdate,
                       db: AsyncSession = Depends(get_async_session),
                       current_user: User = Depends(get_current_user)):
    db_order = await order_service.update_order(db, order_id=order_id, status=status)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.delete("/{order_id}/", response_model=dict)
async def delete_order(order_id: int,
                       db: AsyncSession = Depends(get_async_session),
                       current_user: User = Depends(get_current_user)):
    db_order = await order_service.delete_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order as deleted successfully"}
