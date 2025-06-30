from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime, date

group_routes = Blueprint('group_routes', __name__)

@group_routes.route('/create_group', methods=['POST'])
def create_group():
    group = {
        "id": 0,
        "name": "",
        "unique_key": 0,
        "users": []
    }

    return jsonify({
        "message": "Group created successfully",
        "group": group
    }), 200

@group_routes.route('/get_group/<unique_key>', methods=['POST'])
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