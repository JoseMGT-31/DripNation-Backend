def support_dict(data) -> dict:
    return {
        "id": str(data["_id"]),
        "nombre": data.get("nombre"),
        "email": data.get("email"),
        "motivo": data.get("motivo") if data.get("motivo") else None,
        "solicitud": data.get("solicitud"),
        "created_at": data.get("created_at"),
    }
