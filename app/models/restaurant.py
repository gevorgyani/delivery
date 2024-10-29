from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Restaurant(Base):
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=False)
    #один ко многим
    dishes = relationship('Dish', back_populates='restaurant')
    orders = relationship('Order', back_populates='restaurant')
    reviews = relationship('Review', back_populates='restaurant')