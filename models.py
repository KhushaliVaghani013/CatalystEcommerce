from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    whatsapp_number = Column(String, unique=True)
    is_verified = Column(Boolean, default=False)


class OTPVerification(Base):
    __tablename__ = "otp_verification"

    id = Column(Integer, primary_key=True, index=True)
    whatsapp_number = Column(String)
    otp = Column(String)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    image = Column(String)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Float)
    status = Column(String, default="Pending")

    user = relationship("User")