from flask import render_template, jsonify, request
from app import app
from app.controllers.user_ctrl import get_users, create_user

# Home Page
@app.route('/')
def index():
    return "hello world!"

# API Endpoint to Get Users
@app.route('/api/users', methods=['GET'])
def api_get_users():
    users = get_users()
    return jsonify(users)

# API Endpoint to Create User
@app.route('/api/user', methods=['POST'])
def api_create_user():
    user_data = request.get_json()
    new_user = create_user(user_data)
    return jsonify(new_user), 201
