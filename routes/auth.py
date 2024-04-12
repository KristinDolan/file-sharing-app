from flask import Blueprint, render_template, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Handle user registration logic
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Handle user login logic
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    # Handle user logout logic
    return redirect(url_for('index'))