import os
from dotenv import load_dotenv
import motor.motor_asyncio
from bson import ObjectId

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

def to_object_id(id: str) -> ObjectId:
    return ObjectId(id)
