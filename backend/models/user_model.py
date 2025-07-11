# Data/model layer for user data access
from datetime import datetime
from firebase.firestore_client import db
from models.group_model import get_group_by_key, update_group


def create_user(user_data):
    group = get_group_by_key(user_data["group_id"])

    if not group:
        return {"error": "group not found"}, 404

    group["users"].append(user_data)
    update_group(user_data["group_id"], group)

    return to_dict(user_data)

def get_user_by_id(group, user_id):
    for user in group["users"]:
        if user["user_id"] == user_id:
            return user
    return None

def update_user(user_id, user_data):
    doc_ref = db.collection("groups").document(user_data["group_id"]).get()
    group_data = doc_ref.to_dict()
    if not group_data:
        return {"error": "group not found"}, 404

    for user in group_data["users"]:
        if user["user_id"] == user_id:
            user["name"] = user_data["name"]
            user["password"] = user_data["password"]
            user["is_public"] = user_data["is_public"]
            user["received_messages"] = user_data["received_messages"]
            user["sent_messages"] = user_data["sent_messages"]
            user["updated_at"] = datetime.now()
            break
    update_group(user_data["group_id"], group_data)
    return {"message": "user updated successfully"}, 200

def to_dict(user_data):
    return {
        "name": user_data["name"],
        "password": user_data["password"],
        "created_at": user_data["created_at"],
        "updated_at": user_data["updated_at"],
        "group_id": user_data["group_id"],
        "is_public": user_data["is_public"],
        "user_id": user_data["user_id"]
    }