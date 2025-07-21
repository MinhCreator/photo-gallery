from module.image_load import get_image_path
from flask import render_template, redirect


def add_gallery(app):
# gallery
    @app.route("/gallery")
    def gallery():
        path = get_image_path("static/image_class")
        other_path = get_image_path("static/upload_image")
        return render_template("gallery.html", img=path+other_path)
    def redirect_to_gallery():
        return redirect("gallery")
    app.add_url_rule("/","gallery", view_func=gallery)