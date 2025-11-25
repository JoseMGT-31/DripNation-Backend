from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: str

class Login(BaseModel):
    email: EmailStr
    password: str

class RoleUpdate(BaseModel):
    role: str