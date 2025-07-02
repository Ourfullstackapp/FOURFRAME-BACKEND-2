from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ✅ Enable CORS for development frontend (React on localhost:3001)
    # Add more allowed origins for production if needed
    CORS(app, origins=["http://localhost:3001", "https://fourframe-frontend.onrender.com"])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import models so Flask-Migrate can detect them
    from . import models

    # Register blueprints
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
