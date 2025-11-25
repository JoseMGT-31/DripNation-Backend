from pydantic import BaseModel, EmailStr
from typing import Optional


class SupportCreate(BaseModel):
    nombre: str
    email: EmailStr
    motivo: Optional[str] = None
    solicitud: str


class SupportOut(BaseModel):
    id: str
    nombre: str
    email: EmailStr
    motivo: Optional[str] = None
    solicitud: str
    created_at: Optional[str] = None
