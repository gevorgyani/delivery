from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship

from app.core.db import Base


class Dish(Base):
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_deleted = Column(Boolean, default=False)
