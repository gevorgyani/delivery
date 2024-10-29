from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.core.db import Base

class Dish(Base):
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    #многие к одному
    restaurant = relationship('Restaurant', back_populates='dish') #в Restaurant указывает на связь с полем restaurant в Dish