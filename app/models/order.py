import enum
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship

from app.core.db import Base


# class OrderStatus(enum.Enum):
#     pending = "pending"
#     in_process = "in_process"
#     delivered = "delivered"
#     canceled = "canceled"


class Order(Base):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    dish_id = Column(Integer, ForeignKey('dish.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    # status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    status = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
