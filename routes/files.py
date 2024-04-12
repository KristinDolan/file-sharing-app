from flask import Blueprint, render_template, request

files_bp = Blueprint('files', __name__)

@files_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Handle file upload logic
        return render_template('upload_success.html')
    return render_template('upload.html')

@files_bp.route('/download/<file_id>')
def download(file_id):
    # Handle file download logic
    return render_template('download.html')

@files_bp.route('/delete/<file_id>')
def delete(file_id):
    # Handle file deletion logic
    return render_template('delete_success.html')