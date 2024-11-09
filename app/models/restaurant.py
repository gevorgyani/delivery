from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Restaurant(Base):
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
