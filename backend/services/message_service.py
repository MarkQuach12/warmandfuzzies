from models.message_model import create_message, get_messages_by_user
from datetime import datetime
from utils.uuid_utils import is_valid_uuid

def add_message_service(data):
    # Missing fields: user_id, content, is_anon
    if "receiver_user_id" not in data:
        return {"error": "receiver_user_id is required"}, 400
    if "sender_user_id" not in data:
        return {"error": "sender_user_id is required"}, 400
    if "content" not in data:
        return {"error": "content is required"}, 400
    if "is_anon" not in data:
        return {"error": "is_anon is required"}, 400
    if "group_id" not in data:
        return {"error": "group_id is required"}, 400

    message_data = {
        "content": data["content"],
        "is_anon": data["is_anon"],
        "created_at": datetime.now(),
        "group_id": data["group_id"],
        "receiver_user_id": data["receiver_user_id"],
        "sender_user_id": data["sender_user_id"]
    }

    return create_message(message_data)

def get_messages_service(group_id, user_id, message_type):
    if not user_id:
        return {"error": "user_id is required"}, 400

    if not group_id:
        return {"error": "group_id is required"}, 400

    if message_type not in ["sent", "received"]:
        return {"error": "message_type is invalid"}, 400

    if not group_id.isalnum():
        return {"error": "group_id is invalid"}, 400

    if not is_valid_uuid(user_id):
        return {"error": "user_id is invalid"}, 400

    return get_messages_by_user(group_id, user_id, message_type)