from flask import Blueprint, request, jsonify
from . import db
from sqlalchemy import or_
from .models import User, Task, Item, Comment, RefreshToken
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required,
    get_jwt_identity
)

api_bp = Blueprint('api', __name__)

@api_bp.route('/register', methods=['POST'])
def register_user():
    print("🔥 REGISTER ROUTE HIT")
    data = request.get_json()

    if not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({'error': 'Missing fields'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400

    user = User(
        username=data['username'],
        email=data['email'],
        age=data.get('age')  # Optional: only if your model supports it
    )

    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201
