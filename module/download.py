from flask import send_from_directory

def file_download(app):
# download
    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
