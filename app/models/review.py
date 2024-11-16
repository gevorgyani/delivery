from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from datetime import datetime
from app.core.db import Base


class Review(Base):
    user_id = Column(Integer, nullable=False)  # Здесь также может быть связь с моделью User
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_deleted = Column(Boolean, default=False)