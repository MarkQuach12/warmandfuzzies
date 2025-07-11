from models.group_model import create_group, get_group_by_key, delete_group_by_key
from datetime import datetime
# Service layer for group-related business logic

def create_group_service(data):
    if "name" not in data:
        return {"error": "name is required"}, 400

    group_data = {
        "name": data["name"],
        "users": [],
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    return create_group(group_data)

def get_group_service(unique_key):
    # TODO: Implement get group logic
    return {}

def delete_group_service(unique_key):
    # TODO: Implement delete group logic
    return {}