from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime, date
from services.message_service import add_message_service, get_messages_service

message_routes = Blueprint('message_routes', __name__)

@message_routes.route('/add_message', methods=['POST'])
def add_message():
    message_data = request.json
    message_id = add_message_service(message_data)
    return jsonify({
        "message_id": message_id
    }), 201

@message_routes.route('/get_sent_messages/<group_id>/<user_id>', methods=['GET'])
def get_sent_messages(group_id, user_id):
    messages = get_messages_service(group_id, user_id, "sent")
    return jsonify({
        "sent_messages": messages
    }), 200

@message_routes.route('/get_received_messages/<group_id>/<user_id>', methods=['GET'])
def get_received_messages(group_id, user_id):
    messages = get_messages_service(group_id, user_id, "received")
    return jsonify({
        "received_messages": messages
    }), 200
