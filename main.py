from flask import Flask, render_template, url_for, redirect, request, jsonify, make_response, send_from_directory, flash
from module.image_load import *
from module.handler_error import genericErrorHandler
from module.file_checker import *
from module.secret_gen import final_gen
import os

app = Flask("Memorable Gallery")
UPLOAD_FOLDER = 'static/upload_image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = final_gen()

# home
@app.route("/home")
def home():
    return render_template("home.html", home=app.name)
def redirect_to_home():
    return redirect("home")
app.add_url_rule("/", "home", view_func=home)

# gallery
@app.route("/gallery")
def gallery():
    path = get_image_path("static/image_class")
    other_path = get_image_path("static/upload_image")
    return render_template("gallery.html", img=path+other_path)
def redirect_to_gallery():
    return redirect("gallery")
app.add_url_rule("/","gallery", view_func=gallery)


# uploading file but this feature is used by admin only
@app.route("/upload_file")
def upload_file():
    return render_template('upload.html')
def redirect_to_upload_file():
    return redirect("upload_file")
app.add_url_rule("/","upload_file", view_func=upload_file)

@app.route("/upload_file", methods=["POST", "GET"])
def upload_file():
    default_path ='./static/upload_image/'
    if request.method == "POST":
        for imgs_file in request.files.getlist('img_file'):
            if imgs_file.filename == "":
                flash("No selected file", "warning")
                return redirect(url_for('upload_file'))
            if check_exist(default_path + imgs_file.filename):
                flash("File is exists on server", "warning")
                return redirect(url_for('upload_file'))
            else:
                imgs_file.save(os.path.join(app.config["UPLOAD_FOLDER"], imgs_file.filename))
                flash("Images uploaded successfully", "success")
            # print(imgs_file.filename)
        return redirect(url_for('upload_file'))

    return render_template('upload.html', files=os.listdir(UPLOAD_FOLDER))


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash("File deleted successfully", "success")
    return redirect(url_for('upload_file'))


# error handlers
# register error handlers
for errCode in [400, 401, 403, 404]:
    app.register_error_handler(errCode, genericErrorHandler)

# custom error handlers for 500 and 501 code
@app.errorhandler(501)
@app.errorhandler(500)
def serverError(error):
    return render_template("error_message.html", error_message="Oops,some Internal Error occured...", error_name=error.name, error_code=error.code), error.code

# if run debug mode please replace app.run() by app.run(debug=True)
if __name__ == "__main__":
    app.run()
