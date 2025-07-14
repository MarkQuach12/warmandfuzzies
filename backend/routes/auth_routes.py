from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from services.auth_service import signup_service

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/signup', methods=['POST'])
def signup():
    user_data = request.json
    user_id = signup_service(user_data)
    return jsonify({
        "user_id": user_id
    }), 201

@auth_routes.route('/login', methods=['POST'])
def login():
    return jsonify({}), 200

@auth_routes.route('/logout', methods=['POST'])
def logout():
    return jsonify({}), 200

@auth_routes.route('/profile/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({
        "user_id": user_id,
        "username": "",
        "received_messages": [],
        "sent_messages": [],
        "is_public": True
    }), 200

@auth_routes.route('/update_profile/<user_id>', methods=['PUT'])
def update_profile(user_id):
    return jsonify({
        "user_id": user_id,
        "username": "",
        "received_messages": [],
        "sent_messages": [],
        "is_public": True
    }), 200