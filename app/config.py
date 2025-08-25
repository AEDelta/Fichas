import os
from secrets import token_hex

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", token_hex(16))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "instance", "uploads")
