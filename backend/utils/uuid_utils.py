import uuid

def is_valid_uuid(value: str) -> bool:
    try:
        uuid_obj = uuid.UUID(value)
        return str(uuid_obj) == value
    except ValueError:
        return False