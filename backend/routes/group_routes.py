from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from services.group_service import create_group_service

group_routes = Blueprint('group_routes', __name__)

@group_routes.route('/create_group', methods=['POST'])
def create_group():
    group_data = request.json
    group_id = create_group_service(group_data)
    return jsonify({
        "group_id": group_id
    }), 201

@group_routes.route('/get_group/<unique_key>', methods=['GET'])
def get_group(unique_key):
    group = []
    return jsonify({
        "group": group
    }), 200

@group_routes.route('/delete_group/<unique_key>', methods=['DELETE'])
def delete_group(unique_key):
    return jsonify({
        "message": "Group deleted successfully"
    }), 200