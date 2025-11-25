from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from datetime import datetime
from schemas.product import ProductCreate
from db import db, to_object_id
from models.product import product_dict
import os

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=dict)
async def create_product(
    data: ProductCreate = Depends(ProductCreate.as_form),
    file: UploadFile | None = File(None),
):
    # create product doc without image first
    prod = {**data.dict(exclude_none=True), "created_at": datetime.utcnow()}
    res = await db.products.insert_one(prod)

    # handle file upload if provided
    if file:
        images_dir = os.path.join(os.getcwd(), "images")
        os.makedirs(images_dir, exist_ok=True)
        # build filename using the inserted id to avoid collisions
        ext = os.path.splitext(file.filename)[1]
        filename = f"{res.inserted_id}{ext}"
        file_path = os.path.join(images_dir, filename)
        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)
        image_url = f"/images/{filename}"
        await db.products.update_one({"_id": res.inserted_id}, {"$set": {"image_url": image_url}})

    saved = await db.products.find_one({"_id": res.inserted_id})
    return product_dict(saved)


@router.get("/", response_model=list[dict])
async def list_products():
    prods = await db.products.find().to_list(100)
    return [product_dict(p) for p in prods]


@router.get("/{product_id}")
async def get_product(product_id: str):
    p = await db.products.find_one({"_id": to_object_id(product_id)})
    if not p:
        raise HTTPException(404, "Not found")
    return product_dict(p)


@router.put("/{product_id}")
async def update_product(product_id: str, data: ProductCreate):
    await db.products.update_one(
        {"_id": to_object_id(product_id)},
        {"$set": data.dict(exclude_none=True)}
    )
    return {"status": "ok"}


@router.delete("/{product_id}")
async def delete_product(product_id: str):
    await db.products.delete_one({"_id": to_object_id(product_id)})
    return {"status": "deleted"}