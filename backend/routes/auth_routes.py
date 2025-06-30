from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/signup', methods=['POST'])
def signup():
    return jsonify({
        "user_id": 0,
        "username": "",
        "password": "",
        "received_messages": [],
        "sent_messages": [],
        "is_public": True
    }), 200

@auth_routes.route('/login', methods=['POST'])
def login():
    return jsonify({}), 200