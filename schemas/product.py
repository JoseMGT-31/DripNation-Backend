from pydantic import BaseModel
from fastapi import Form
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    description: str
    category: Optional[str] = None
    price: float
    stock: int
    image_url: Optional[str] = None

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        description: str = Form(...),
        category: Optional[str] = Form(None),
        price: float = Form(...),
        stock: int = Form(...),
        image_url: Optional[str] = Form(None),
    ) -> "ProductCreate":
        return cls(name=name, description=description, category=category, price=price, stock=stock, image_url=image_url)
