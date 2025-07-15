from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from services.group_service import create_group_service, get_group_service, delete_group_service

group_routes = Blueprint('group_routes', __name__)

@group_routes.route('/create_group', methods=['POST'])
def create_group():
    group_data = request.json
    group_id = create_group_service(group_data)
    return jsonify({
        "group_id": group_id
    }), 201

@group_routes.route('/get_group/<group_id>', methods=['GET'])
def get_group(group_id):
    group = get_group_service(group_id)
    return jsonify({
        "group": group
    }), 200

@group_routes.route('/delete_group/<group_id>', methods=['DELETE'])
def delete_group(group_id):
    confirm = request.args.get('confirm')

    if confirm != "true":
        return jsonify({
            "error": "Confirmation is required"
        }), 400

    delete_group_service(group_id)
    return jsonify({
        "message": "Group deleted successfully"
    }), 200