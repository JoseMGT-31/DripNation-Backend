from datetime import datetime

def user_dict(data) -> dict:
    return {
        "id": str(data["_id"]),
        "username": data["username"],
        "email": data["email"],
        "role": data["role"],
        "created_at": data["created_at"],
    }