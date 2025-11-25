from pydantic import BaseModel
from fastapi import Form
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    image_url: Optional[str] = None

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        description: str = Form(...),
        price: float = Form(...),
        stock: int = Form(...),
        image_url: Optional[str] = Form(None),
    ) -> "ProductCreate":
        return cls(name=name, description=description, price=price, stock=stock, image_url=image_url)
