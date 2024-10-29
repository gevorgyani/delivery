from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.core.db import Base


class Order(Base):
    user_id = Column(Integer, nullable=False)  # Здесь может быть связь с моделью User
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False)
    restaurant = relationship('Restaurant', back_populates='order')
