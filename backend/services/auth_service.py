from tokenize import group
from models.user_model import create_user, get_user_by_id, update_user
from models.group_model import get_group_by_key
from datetime import datetime
import uuid

def signup_service(data):
    if "name" not in data:
        return {"error": "name is required"}, 400
    if "password" not in data:
        return {"error": "password is required"}, 400
    if "group_id" not in data:
        return {"error": "group_id is required"}, 400
    if "is_public" not in data:
        return {"error": "is_public is required"}, 400

    user_data = {
        "name": data["name"],
        "password": data["password"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "group_id": data["group_id"],
        "is_public": data["is_public"],
        "received_messages": [],
        "sent_messages": [],
        "user_id": str(uuid.uuid4())
    }

    user = create_user(user_data)
    return user

def login_service(data):
    # TODO: Implement login logic
    return {}

def logout_service(data):
    # TODO: Implement logout logic
    return {}

def get_user_service(group_id, user_id):
    group = get_group_by_key(group_id)
    if not group:
        return {"error": "group not found"}, 404
    user = get_user_by_id(group, user_id)
    return user

def update_profile_service(updated_user_data):
    if "user_id" not in updated_user_data:
        return {"error": "user_id is required"}, 400
    if "group_id" not in updated_user_data:
        return {"error": "group_id is required"}, 400

    user = update_user(updated_user_data["user_id"], updated_user_data)

    return user