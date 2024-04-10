from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 不需要傳入 app，之後在 app/__init__.py 中初始化

from .user import User  # 如果你的 User 模型定義在 user.py 中，確保引入正確的路徑
