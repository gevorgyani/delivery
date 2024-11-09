from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.core.db import Base

class Dish(Base):
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)