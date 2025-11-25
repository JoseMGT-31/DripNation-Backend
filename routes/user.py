from fastapi import APIRouter, HTTPException, Depends
from schemas.user import UserCreate, UserOut, Login, RoleUpdate
from core.security import hash_password, verify_password, create_token
from db import db, to_object_id
from models.user import user_dict
from datetime import datetime

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    exists = await db.users.find_one({"email": user.email})
    if exists:
        raise HTTPException(400, "Email already registered")

    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hash_password(user.password),
        "role": "user",
        "created_at": datetime.utcnow()
    }
    res = await db.users.insert_one(new_user)
    saved = await db.users.find_one({"_id": res.inserted_id})
    return user_dict(saved)


@router.post("/login")
async def login(data: Login):
    user = await db.users.find_one({"email": data.email})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"id": str(user["_id"]), "role": user["role"]})
    return {"token": token}


@router.get("/", response_model=list[UserOut])
async def get_users():
    users = await db.users.find().to_list(100)
    return [user_dict(u) for u in users]


@router.patch("/{user_id}/role")
async def update_role(user_id: str, data: RoleUpdate):
    await db.users.update_one(
        {"_id": to_object_id(user_id)},
        {"$set": {"role": data.role}}
    )
    return {"status": "ok"}