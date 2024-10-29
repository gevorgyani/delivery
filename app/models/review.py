from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Review(Base):
    user_id = Column(Integer, nullable=False)  # Здесь также может быть связь с моделью User
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    restaurant = relationship('Restaurant', back_populates='review')