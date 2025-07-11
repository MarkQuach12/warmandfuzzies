from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime, date
from services.message_service import add_message_service

message_routes = Blueprint('message_routes', __name__)

@message_routes.route('/add_message', methods=['POST'])
def add_message():
    message_data = request.json
    message_id = add_message_service(message_data)
    return jsonify({
        "message_id": message_id
    }), 201

@message_routes.route('/get_messages/<user_id>', methods=['GET'])
def get_messages(user_id):
    messages = []
    return jsonify({
        "messages": messages
    }), 200
