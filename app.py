from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from flask_restful import Api
from datetime import datetime
from functools import wraps
import os
from flask_cors import CORS
from config import db
from models import User, Item, Claim, Comment, Reward, Image

app = Flask(name)
CORS(app,
     origins=[
         "http://localhost:3000",
         "https://lost-now-found.vercel.app"
     ],
       supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.secret_key = 'shhh-very-secret'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

def admin_only(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(args, **kwargs):
        user = User.query.get(get_jwt_identity())
        if user.role != "admin":
            return jsonify({"error": "Admin access only"}), 403
        return fn(args, **kwargs)
    return wrapper

def log_admin_action(admin_id, action_desc):
    admin = User.query.get(admin_id)
    print(f"[ADMIN LOG] {datetime.utcnow()} - {admin.username} ({admin.id}) - {action_desc}")
@app.route('/')
def index():
    return "Bruh no need to worry these routes are purfeeect just look into the read me !."

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')
    if not username or not password:
        return jsonify({"error": "Username and password needed"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken"}), 400
    user = User(username=username, email=email, role=role)
    user.password_hash = password
    db.session.add(user)
    db.session.commit()
    token = create_access_token(identity=user.id)
    return jsonify({"user": user.to_dict(), "token": token}), 201