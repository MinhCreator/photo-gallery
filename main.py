from flask import Flask, render_template, url_for, redirect, request, jsonify, make_response
from module.image_load import *
from module.handler_error import genericErrorHandler


app = Flask("Memorable Gallery")

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
    return render_template("gallery.html", img=path)
def redirect_to_gallery():
    return redirect("gallery")
app.add_url_rule("/","gallery", view_func=gallery)

# error handlers
# register error handlers
for errCode in [400, 401, 403, 404]:
    app.register_error_handler(errCode, genericErrorHandler)

# custom error handlers for 500 and 501 code
@app.errorhandler(501)
@app.errorhandler(500)
def serverError(error):
    return render_template("message.html", error_message="Oops,some Internal Error occured...", error_name=error.name, error_code=error.code), error.code

# if run debug mode please replace app.run() by app.run(debug=True)
if __name__ == "__main__":
    app.run()
