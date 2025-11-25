def product_dict(data) -> dict:
    return {
        "id": str(data["_id"]),
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "stock": data["stock"],
        "created_at": data.get("created_at"),
        "image_url": data.get("image_url") if data.get("image_url") else None,
    }
