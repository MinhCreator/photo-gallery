from flask import send_from_directory

def file_download(app):
# download
    @app.route('/download/<filename>')
    def download_file(filename, UPLOAD_FOLDER):
        return send_from_directory(UPLOAD_FOLDER, filename)
