from pydantic import BaseModel


class SendOTP(BaseModel):
    whatsapp_number: str


class VerifyOTP(BaseModel):
    whatsapp_number: str
    otp: str


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image: str


class OrderCreate(BaseModel):
    total_amount: float