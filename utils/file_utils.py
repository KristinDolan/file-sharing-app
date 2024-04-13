def upload_file(file):
    # Upload the file to the server or a cloud storage service
    pass

def download_file(file_id):
    # Download the file from the server or a cloud storage service
    pass

def allowed_file(filename):
    # Check if the file extension is allowed
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx', 'py', 'html', 'js', 'css', 'scss'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
