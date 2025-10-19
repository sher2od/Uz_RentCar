from sqlalchemy import Column, Integer, ForeignKey, Enum as SqlEnum, Date
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum

class OrderStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    cancelled = "cancelled"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    order_date = Column(Date)
    status = Column(SqlEnum(OrderStatus), default=OrderStatus.pending)

    car = relationship("Car", back_populates="orders")
    user = relationship("User", back_populates="orders")
