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

def get_group_service(group_id):
    if not group_id:
        return {"error": "group_id is required"}, 400

    if not group_id.isalnum():
        return {"error": "group_id is invalid"}, 400

    return get_group_by_key(group_id)

def delete_group_service(group_id):
    if not group_id:
        return {"error": "group_id is required"}, 400

    if not group_id.isalnum():
        return {"error": "group_id is invalid"}, 400

    return delete_group_by_key(group_id)