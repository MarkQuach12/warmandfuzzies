# Data/model layer for message data access
from firebase.firestore_client import db
from models.group_model import get_group_by_key
from models.user_model import get_user_by_id, update_user
from datetime import datetime

def create_message(message_data):
    group = get_group_by_key(message_data["group_id"])

    if not group:
        return {"error": "group not found"}, 404

    # user to receive the message
    user = get_user_by_id(group, message_data["receiver_user_id"])

    if not user:
        return {"error": "receiver user not found"}, 404
    receiver_message_data = message_data.copy()
    del receiver_message_data["receiver_user_id"]
    user["received_messages"].append(receiver_message_data)
    update_user(user["user_id"], user)

    # the user who sent the message
    user = get_user_by_id(group, message_data["sender_user_id"])
    if not user:
        return {"error": "sender user not found"}, 404
    sender_message_data = message_data.copy()
    del sender_message_data["sender_user_id"]
    user["sent_messages"].append(sender_message_data)
    update_user(user["user_id"], user)

    return {"message": "message created successfully"}

def get_messages_by_user(group_id, user_id, message_type):
    group = get_group_by_key(group_id)

    if not group:
        return {"error": "group not found"}, 404

    user = get_user_by_id(group, user_id)

    if not user:
        return {"error": "user not found"}, 404

    if message_type == "sent":
        return user["sent_messages"]
    elif message_type == "received":
        return user["received_messages"]
    else:
        return {"error": "message_type is invalid"}, 400