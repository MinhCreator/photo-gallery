from flask import redirect, url_for, flash
import os


def delete_file(app):
# delete
    @app.route('/delete/<filename>', methods=['POST'])
    def delete_file(filename):
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            flash("File deleted successfully", "success")
        return redirect(url_for('upload'))