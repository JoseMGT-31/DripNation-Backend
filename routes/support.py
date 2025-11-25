from fastapi import APIRouter, HTTPException
from datetime import datetime
from db import db, to_object_id
from models.support import support_dict
from schemas.support import SupportCreate, SupportOut

router = APIRouter(prefix="/supports", tags=["Support"])


@router.post("/", response_model=SupportOut)
async def create_support(data: SupportCreate):
    doc = {**data.dict(exclude_none=True), "created_at": datetime.utcnow()}
    res = await db.supports.insert_one(doc)
    saved = await db.supports.find_one({"_id": res.inserted_id})
    return support_dict(saved)


@router.get("/", response_model=list[SupportOut])
async def list_supports():
    items = await db.supports.find().to_list(100)
    return [support_dict(i) for i in items]


@router.get("/{support_id}", response_model=SupportOut)
async def get_support(support_id: str):
    s = await db.supports.find_one({"_id": to_object_id(support_id)})
    if not s:
        raise HTTPException(404, "Not found")
    return support_dict(s)


@router.put("/{support_id}")
async def update_support(support_id: str, data: SupportCreate):
    await db.supports.update_one({"_id": to_object_id(support_id)}, {"$set": data.dict(exclude_none=True)})
    return {"status": "ok"}


@router.delete("/{support_id}")
async def delete_support(support_id: str):
    res = await db.supports.delete_one({"_id": to_object_id(support_id)})
    if res.deleted_count == 0:
        raise HTTPException(404, "Not found")
    return {"status": "deleted"}
