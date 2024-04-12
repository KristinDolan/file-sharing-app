import os

class Config:
    # Secret key, upload folder, and logging configuration...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

    # SQLite database URI (replace 'app.db' with your desired database file name)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Uploads configuration (replace with your desired upload directory)
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', '.csv', '.xlsx', '.py', '.html', '.js', '.css'}

    # Logging configuration
    LOG_FILE = 'app.log'