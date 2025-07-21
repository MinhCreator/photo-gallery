from flask import render_template, request, redirect, url_for, flash
import os
from module.file_checker import check_exist


def upload(app):
# upload only use by admin
    @app.route('/upload_form')
    def upload_form():
        return render_template('upload.html', files=os.listdir(app.config["UPLOAD_FOLDER"]))
        
    @app.route("/upload", methods=["POST", "GET"])
    def upload():
        default_path = app.config["UPLOAD_FOLDER"] #'./static/upload_image/'
        if request.method == "POST":
            get_list_img = request.files.getlist('img_file')
            for imgs_file in get_list_img:
                if imgs_file.filename == "":
                    flash("No selected file", "warning")
                    return redirect(url_for('upload'))
                if check_exist(default_path + imgs_file.filename):
                    flash("File is exists on server", "warning")
                    return redirect(url_for('upload'))
                else:
                    imgs_file.save(os.path.join(app.config["UPLOAD_FOLDER"], imgs_file.filename))
                    flash("Images uploaded successfully", "success")
            # print(imgs_file.filename)
        return redirect(url_for('upload_form'))

        # return render_template('upload.html', files=os.listdir(UPLOAD_FOLDER))
    app.add_url_rule("/","upload_form", view_func=upload_form)
