from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime, date

message_routes = Blueprint('message_routes', __name__)

@message_routes.route('/add_message', methods=['GET'])
def add_message():
    return jsonify({
        "message_id": str(uuid.uuid4()),
        "sender_id": 0,
        "receiver_id": 0,
        "content": "",
        "timestamp": datetime.now()
    }), 200

@message_routes.route('/get_messages/<user_id>', methods=['GET'])
def get_messages(user_id):
    messages = []
    
    return jsonify({
        "messages": messages
    }), 200
