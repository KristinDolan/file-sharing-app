from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import database models
from models import User

# Create the database tables
with app.app_context():
    db.create_all()

# Migrate functionality for db updates
migrate = Migrate(app, db)


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/file/upload')
def file_upload():
    return render_template('file_upload.html')

if __name__ == '__main__':
    app.run(debug=True)