from flask import Flask, render_template, redirect
from module.handler_error import genericErrorHandler
from module.secret_gen import final_gen
from routes.config_route import configure_route
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask("Memorable Gallery")
upload_folder = 'static/upload_image'
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, upload_folder)
app.secret_key = final_gen()

@app.route("/home")
def home():
    return render_template("home.html", title="Memorable Gallery")
redirect("home")
app.add_url_rule("/","home", view_func=home)

configure_route(app)
# error handlers
# register error handlers
for errCode in [400, 401, 403, 404]:
    app.register_error_handler(errCode, genericErrorHandler)

# custom error handlers for 500 and 501 code
@app.errorhandler(501)
@app.errorhandler(500)
def serverError(error):
    return render_template("error_message.html", error_message="Oops!, some internal error occured...", error_name=error.name, error_code=error.code), error.code

# if run debug mode please replace app.run() by app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
