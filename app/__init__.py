from flask import Flask
from config import Config
from flask_cors import CORS
from app.models import db  # 引入 db 對象

# Initialize the app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy db object
db.init_app(app)

# Create the tables (if they don't exist)
with app.app_context():
    db.create_all()

# Enable CORS
CORS(app)

# Import the routes
from app import routes
