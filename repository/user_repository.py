from models.user import UserDB
from db import db

def get_user_by_email(email) -> UserDB | None:
    user = db.users.find_one({"email": email})
    if not user:
        return None
    
    user["id"] = str(user["_id"])
    del user["_id"]
    return UserDB(**user)


def create_user(email, password_hash, role, created_at, updated_at) -> UserDB:
    user_formated = {
        "email" : email,
        "password_hash" : password_hash,
        "role" : role,
        "created_at" : created_at,
        "updated_at" : updated_at
    }

    id = db.users.insert_one(user_formated)
    db.users.find_one({"_id": id})