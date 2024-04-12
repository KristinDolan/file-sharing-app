from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

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