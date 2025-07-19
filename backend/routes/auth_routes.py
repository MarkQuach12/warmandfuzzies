from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from services.auth_service import signup_service, get_user_service, update_profile_service

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

@auth_routes.route('/profile/<group_id>/<user_id>', methods=['GET'])
def get_user(group_id, user_id):
    user = get_user_service(group_id, user_id)
    return jsonify({
        "user": user
    }), 200

@auth_routes.route('/update_profile', methods=['PUT'])
def update_profile():
    updated_user_data = request.json
    user = update_profile_service(updated_user_data)

    return jsonify({
        "user": user
    }), 200